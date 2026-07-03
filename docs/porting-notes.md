# Porting Notes: Python → Lean 4 / C++26

Per-algorithm preconditions, invariants, and termination arguments for manually
re-implementing the Python reference code. Termination arguments matter for Lean
(`termination_by` / structural recursion); preconditions matter everywhere.

General notes:

- The Python code uses NumPy arrays. After the 2026-07 cleanup every merge buffer
  is allocated with `dtype=array.dtype` (or `np.result_type`), so integer inputs
  stay integers — ports should use the element type generically (`T`, `α`).
- The C++ scaffolding in `cpp/` currently sets `CMAKE_CXX_STANDARD 17`; bump it
  to `26` in `cpp/CMakeLists.txt` when you start implementing.
- Randomized algorithms (QuickSort, RSelect, Karger) accept or use a seedable
  RNG in tests; give ports an injectable RNG for cross-language test parity.
- **`docs/lean4-catchable-bugs.md`** catalogs the real bugs fixed in this code
  (buggy versions verbatim) classified by which Lean 4 mechanism catches them
  — port the buggy version first as an exercise before the fixed one.

## Sort

**Reference:** `Sort/MergeSort.py` (typed) is the canonical MergeSort;
`Sort/Sort.py` also has Insertion, Bubble (cocktail variant), Quick.

- **MergeSort** — pure function, returns a new array. Base case `n <= 1`.
  Termination: each recursive call halves the length (`n/2`, `n - n/2`), both
  strictly smaller once `n >= 2`. Merge invariant: `merged[0..k)` is sorted and
  contains exactly the consumed prefixes of `left` and `right`.
  Note the split order quirk: `left = MergeSort(array[mid:])`,
  `right = MergeSort(array[:mid])` (left variable holds the *upper* half) —
  harmless for correctness, but mirror it or normalize it consciously.
- **QuickSort** — in-place, `[left, right)` half-open window. `partition`
  returns the final pivot index; recursion on strictly smaller windows
  (`[left, p)` and `[p+1, right)`) terminates. Optional `rng` parameter
  (a `np.random.Generator`) makes runs reproducible.
- **BubbleSort** — cocktail/shaker variant returning `(array, swap_count)`.
  Termination: `end` decreases / `start` increases every outer iteration.
- **InsertionSort** — CLRS Chapter 2; invariant: `array[0..i)` sorted before
  iteration `i`.

## Search

**Reference:** `Search/Search.py`

- **BinarySearch (iterative/recursive)** — requires a sorted array. Recursion
  terminates because `hi - lo` strictly decreases; returns -1 when absent.
- **SecondLargest** — tournament-style divide and conquer returning
  `[largest, second]`. Pure (does not mutate its input). Single-element input
  returns `-inf` (float sentinel) for the second slot — in a typed port prefer
  `Option`/`optional` instead of the sentinel.
- **Closest pair 2D (`FindclosestPair`/`closestPair`/`closestSplitPair`)** —
  **PRECONDITION: distinct x-coordinates.** The y-sorted list is split by
  `x <= mid_x`, which diverges from the index-based x-split when x-values
  repeat at the median (an all-equal-x input makes the right half empty).
  The correct fix in a port is an index-consistent split. All distances are
  *squared* distances except the `sqrt(delta)` strip-width comparison in
  `closestSplitPair` — keep the squared/true-distance boundary explicit.
  Termination: point set is split into strictly smaller halves; `n <= 3` base
  case goes to brute force. Coincident points are a valid closest pair
  (distance 0) — do not filter `d == 0`.
- **ThreeSum (brute force / sort + binary search)** — counts triplets summing
  to zero; the quick variant searches only indices `> j` to avoid duplicates.
- **`Search.Rselect` vs `Select/Python/RSelect.py`** — two deliberate variants
  of quickselect: `Search.Rselect` is *index-returning, in-place, windowed
  (left/right)*; `Select.RSelect` is *value-returning over sliced copies*.
  Port whichever matches your target idiom (the windowed one maps naturally
  to C++ iterators; the slicing one to functional Lean).

## Select

**Reference:** `Select/Python/RSelect.py`, `Select/Python/DSelect.py`
**Stubs:** `cpp/select/`, `rust/algorithms-select/`, `lean4/Algorithms/Select/Basic.lean`

- Both raise `ValueError` on empty input or `ith` out of `[0, n)`.
- **RSelect** — termination: each recursion drops the pivot, so the slice is
  strictly smaller. Randomized pivot; average O(n).
- **DSelect (median of medians)** — pivot is the **upper median**
  `sorted(group)[len(group)//2]` of each group of ≤ 5. This convention (not
  `statistics.median`, which averages even-sized groups) guarantees the pivot
  is an element of the array. Termination needs the classic 30-70 argument:
  the pivot is ≥ 3/10 and ≤ 7/10 of elements, so recursive calls are on at
  most `7n/10 + O(1)` elements (plus the `n/5` medians list).

## Data Structures

**Reference:** `DataStructures/`

- **Graph** (`Graph.py`) — adjacency via vertex-index lists. Class invariant
  (documented on the class): vertices form a dense index sequence; edges store
  indices into `self.vertices`. `kosaraju()` labels `vertex.scc` in place and
  returns the SCC count; `topological_sort` uses a single-element list as a
  mutable counter cell — in Lean this becomes fold/State, in C++ a by-reference
  counter. Recursive DFS depth is O(V): fine for course inputs, use an explicit
  stack for large graphs. `delete_vertex` does NOT clean up dangling edge
  references (known TODO); `merge_vertices` is `NotImplementedError`.
- **SimpleLinkedList / DoubleLinkedList** — `size` is maintained by every
  mutation (insert/delete); `head is None ⇔ tail is None ⇔ size == 0` after the
  2026-07 fixes. Positional ops on the double list walk from head or tail
  depending on `pos < ceil(size/2)` — re-derive the index arithmetic carefully
  when porting; it is off-by-one-prone.
- **Stack / Queue** — adapters over DoubleLinkedList; disallowed operations
  raise `NotImplementedError`. `pop`/`dequeue` on empty return `None`
  (→ `Option`/`optional` in ports).

## Graph Algorithms (BFS / DFS)

Live in `DataStructures/Graph.py` (methods) with demo drivers `bfs.py`/`dfs.py`;
the multi-language trees split them into their own module
(`rust/algorithms-graph`, `lean4/.../GraphAlgorithms`).

- BFS invariant: `distance` is the true shortest hop count when dequeued.
- Topological sort: labels descend from `|V|` as DFS finishes (reverse
  post-order). Kosaraju: topological order of the reversed graph, then DFS in
  that order on the original.

## Integer Multiplication

**Reference:** `RecursiveIntegerMultiplication/`

- Both algorithms split by digits: `number = a * 10^(n//2) + b`, so the
  recombination shift for the high term is `10^(2*(n//2))` — **not** `10^n`,
  which is wrong for odd `n` (fixed 2026-07). With exact base-case
  multiplication the identity holds for ANY digit count; the power-of-2
  padding helpers (`getPaddingsize`/`padNumber`/`unpadNumber`) are
  book-fidelity, not a correctness requirement.
- Base case `n1 == 1 or n2 == 1` multiplies directly. Termination: `n//2 < n`
  for `n >= 2`.
- Digit counting is exact integer logic: `len(str(abs(n)))` and
  `int.bit_length()`. Python ints are arbitrary precision — **C++26 needs a
  big-integer type** (or constrain inputs so intermediate products fit in
  `__int128`); Lean's `Nat` is arbitrary precision like Python.
- Karatsuba subtlety: `p = a + b` may carry into one extra digit; passing
  `n3 = n1//2` for it is still fine because the recursion is exact for any
  actual operand size (the `n` parameters only steer the split).

## Minimum Cut (Karger)

**Reference:** `MinimumCut/MinimumCut.py`
Fixtures: `MinimumCut/data/input_random_N_M.txt` with expected cuts in
matching `output_random_N_M.txt`.

- `Graph` subclasses `dict` (vertex → adjacency list, undirected edges stored
  twice, parallel edges as duplicates). In ports use a plain hash map — do not
  reproduce the inheritance.
- One trial (`min_cut`): while more than 2 vertices remain, pick a random
  incident pair, merge, relabel, drop self-loops; returns
  `countEdges() = total//2` (each edge stored twice). Termination: each
  contraction removes exactly one vertex.
- Edge selection picks a uniform vertex then a uniform incident edge — this is
  NOT uniform over edges (degree bias). It still finds min cuts over enough
  trials but the classic success bound `1 - (1 - 2/n²)^T` assumes uniform edge
  choice; note this if you formalize the probability argument.
- Run many trials and take the minimum; seed the RNG in tests.

## Linear Algebra

**Reference:** `LinearAlgebra/Python/MatMul.py`, `LinearAlgebra/Python/ModfiedGramShmidt.py`
**Stubs:** `cpp/linear_algebra/`, `rust/algorithms-linear-algebra/`, `lean4/Algorithms/LinearAlgebra/Basic.lean`

- The Python filename `ModfiedGramShmidt.py` is a typo kept for history —
  name ports `ModifiedGramSchmidt` / `modified_gram_schmidt`.
- **RecMatMult / strassenRecMat** — PRECONDITION: square matrices with
  power-of-2 dimension (no padding implemented). The 1x1 base case returns a
  *scalar* that NumPy broadcasting assigns into 2D quadrant slices; ports must
  return a 1x1 matrix (or special-case scalars) explicitly. Termination:
  dimension halves each level down to 1.
- **Modified Gram-Schmidt** — returns `(Q, R)`; raises on linearly dependent
  columns (norm below `1e-10`). The "modified" property: each `v` is
  orthogonalized against the *already-computed* `Q` columns sequentially
  (numerically stabler than classical GS). Float tolerance is machine/scale
  dependent — make it a parameter in ports.

## Misc (Count Inversions)

**Reference:** `Misc/CountInversions.py`

- Merge-sort-based counting: when an element of `right` is placed, it forms
  inversions with every remaining element of `left` (`splitInv += len(left) - i`).
  Total = left + right + split inversions. Base case `n <= 1` returns 0.
- Ties: the merge must use `left[i] <= right[j]` so equal elements are taken
  from the LEFT without counting — equal elements are not inversions. The
  original strict `<` fell into the counting branch on ties and overcounted
  on duplicate inputs (`[5,5,5]` → 3 instead of 0; found by the parity
  harness 2026-07-03, fixed the same day). Keep the `<=` when porting.
