# Get the Python code in shape as a Lean 4 / C++26 porting reference

## Context

The user will manually re-implement the algorithms in this repo in Lean 4 and C++26 (stub scaffolding already exists in `cpp/`, `rust/`, `lean4/`). Before that, the Python must be a trustworthy reference: bug-free (per CLAUDE.md), side-effect-free on import, with documented preconditions and tests that pin the semantics the ports must match. A full review found real correctness bugs, import-time side effects, untested modules, and two topics (Select, LinearAlgebra) with no porting scaffolding.

Scope decisions (user was AFK; defaults chosen, revisit if desired): **keep NumPy** (fix dtype bugs, don't migrate to lists), **no renames**, **delete scratch/dead code**, **add Select + LinearAlgebra stub scaffolding**. Per CLAUDE.md, Claude writes no C++/Rust/Lean implementation bodies — stubs and signatures only.

Corrections found during review: `Graph.py`'s `import Queue`/`import Stack` bug was already fixed (commit `0a7a832`); `tests/TEST_COVERAGE_REPORT.md`, `run_all_tests.sh`, and CLAUDE.md "Common Issues" still describe the pre-fix state (stale — update them).

## Phase 0 — Baseline

`source .venv/bin/activate && pytest` — record pass count (expected 101). Note: `requirements.txt` says `numpy>=2.0.0` but `.venv` has 1.26.4; keep code compatible with both, don't upgrade unilaterally.

## Phase 1 — Bug fixes (write/adjust guarding test in the same change; pytest green at each step)

1. **`Sort/Sort.py`**
   - `MergeSort` (~line 125): base case `== 1` → `<= 1` (empty array currently infinite-recurses); move `merged = np.zeros(...)` after the base case and add `dtype=array.dtype` (currently float64 corrupts int arrays).
   - `QuickSort` (line 160): add optional `rng: np.random.Generator | None = None` param, use `rng.integers(left, right)`; thread `rng` through recursive calls. Preserves existing call signature.
   - Delete pointless `swapelement` helper; inline tuple-swap at its two call sites (nothing imports it).
2. **`Sort/MergeSort.py`**: `TypeVar` bound `np.floating` → `np.number[Any]` (currently excludes ints; all tests use ints). Must still pass `mypy --strict`.
3. **`Misc/CountInversions.py`**: same two fixes as Sort.py MergeSort — base case `<= 1` returning `(array, 0)`, `dtype=left.dtype` on merge buffer; delete unused locals.
4. **`RecursiveIntegerMultiplication/` (both files)** — the big one:
   - Recombination `10**(n1)*ac + 10**(n3)*(ad+bc) + bd` → `10**(2*n3)*ac + 10**(n3)*(ad+bc) + bd` (line 33 in Recursive_, lines ~81/107 in Karatsuba_). Split uses `n1//2`, so the high shift must be `2*(n1//2)` — currently wrong for odd digit counts.
   - Align base cases to `if n1 == 1 or n2 == 1: return number1 * number2` in both files (currently `and` vs bare `n1==1`).
   - Karatsuba `getNumDigits`: replace float `np.log10` body with `len(str(abs(int(number))))` (exact for big ints; sign check currently runs *after* log10). `getNum2Multiples`: `int(abs(number)).bit_length()` (bit-exact with existing test expectations).
   - Delete dead imports in both files (`numpy`, `random`, `unittest`, `time`, `sys`); fix `padNumber` docstring (appends trailing zeros, not left-pad).
5. **`Select/Python/RSelect.py` + `DSelect.py`**
   - Both: raise `ValueError` for empty array / out-of-range `ith` at top of `RSelect`/`DSelect`.
   - `DSelect` line 21: `statistics.median` returns a mean for even-sized tail groups → value not in array → `array.index(p)` ValueError. Replace with `sorted(group)[len(group)//2]` upper-median per 5-group; drop `import statistics`.
   - Both `__main__` blocks: remove the `readFromFile` positional (`type=bool` is always truthy; falsy path leaves `array` unbound → NameError); always read `file`.
6. **`DataStructures/Graph.py`**: make `import graphviz` lazy (move inside `print_graph`); `kosaraju`: drop unused `vertex` param, `return numSCC[0]`, docstring noting it labels `vertex.scc` in place. Update the one call site in `tests/test_graph.py`.
7. **`DataStructures/LinkedList.py` + `DoubleLinkedList.py` + `Stack.py`**
   - Sweep `== None`/`!= None` → `is None`/`is not None` (CLAUDE.md requirement).
   - `LinkedList.deleteFromEnd`: also clear `self.tail` when list empties (stale-tail bug). Drop ignored `max/min` params in `LinkedNumber.__init__`.
   - `DoubleLinkedList.__init__`: drop ignored `size` param; **fix `insert(pos=0, ...)` double `self.size += 1`** (insert_at_beginning already increments); `search`: guard empty list before dereferencing `self.head`.
   - `Stack.is_empty`: delete the `print("Stack is empty")` side effect (fires every DFS loop iteration).
8. **`MinimumCut/MinimumCut.py`**: rewrite `select_edge_random` without the bare `except` (leaves `vertex2` unbound → UnboundLocalError) — `random.choice` on keys then on adjacency list; `min_cut` returns `self.countEdges()` (currently None, docstring says int); extract `load_graph(path) -> Graph` from `main()` and default the path to `os.path.join(os.path.dirname(__file__), 'data', 'kargerMinCut.txt')` (current cwd-relative path crashes); delete commented-out blocks.
9. **`LinearAlgebra/Python/MatMul.py`**: delete module-level test vectors (import side effect); `VecDot`/`MatMul` raise `ValueError` on shape mismatch instead of print+None; `np.zeros(..., dtype=np.result_type(A.dtype, B.dtype))`; add type hints + docstrings documenting the square power-of-2 precondition for `RecMatMult`/`strassenRecMat` and the scalar-broadcast base case (load-bearing porting note).
10. **`LinearAlgebra/Python/ModfiedGramShmidt.py`**: wrap `main()` in `__main__` guard (currently runs on import); fix invalid annotation `list[np.array, np.array]` → `tuple[np.ndarray, np.ndarray]` and `return Q, R`. Keep the misspelled filename (no-rename policy); record correct spelling in porting notes.
11. **`Search/Search.py`**: delete the useless module-level `sys.path` hack (repo-root imports come from `tests/conftest.py`); `SecondLargest` 2-element branch: return a new array instead of mutating the caller's input; `closestDistance2DBruteForce`: inner loop starts at `element+1` and drop the `d_2 != 0` skip (coincident points ARE the closest pair, currently silently skipped) — same in `closestSplitPair` (`if d == 0: continue`). Document (not fix) the duplicate-x split fragility in `closestPair` as a precondition ("distinct x-coordinates") — the proper fix is a rewrite best done during the port. Keep the `Rselect` duplicate (index-returning in-place variant vs `Select/`'s value-returning variant) but add a docstring line to each distinguishing them.

## Phase 2 — Delete scratch, dead code, stale docs

- Delete `DataStructures/sandbox.py` and `DataStructures/dfs_copy.py` (scratch; execute at import).
- Strip large commented-out blocks: `DataStructures/bfs.py` (lines ~7–30; also fix the `for vertex in g` → `g.get_vertices()` in its `__main__` demo), `dfs.py` (commented kosaraju block), `Queue.py` (commented main).
- Update stale Graph-bug text in `tests/TEST_COVERAGE_REPORT.md`, `tests/run_all_tests.sh` trailing note, and CLAUDE.md "Common Issues".

## Phase 3 — Tests (unittest style matching existing files; pytest picks them up via pytest.ini)

- Strengthen: `test_sort.py` (replace the bug-masking bare `try/except` empty-array test with real assertions; dtype preservation; seeded-QuickSort determinism), `test_count_inversions.py` (empty array, dtype), `test_multiplication.py` (**odd-digit cases** like 123×456 and 12345×67890, 20-digit big-int, negative-input getNumDigits), `test_select.py` (14/23-element arrays forcing even tail groups — crashes old DSelect; ValueError cases), `test_search.py` (coincident points → distance 0; SecondLargest non-mutation; D&C closest pair vs brute force on ≥8 distinct-x points), `test_datastructures.py` (empty-list search, insert(0) size, stale tail, no stdout from `Stack.is_empty`), `test_graph.py` (kosaraju call-site update).
- New: `tests/test_matmul.py` (VecDot/MatMul vs `@`, RecMatMult/Strassen vs np.matmul on 2/4/8-size, shape-mismatch ValueError), `tests/test_gram_schmidt.py` (Q orthonormal, QR≈A, R upper-triangular, ValueError on dependent columns), `tests/test_minimum_cut.py` (unit tests for merge/relabel/self-loop/countEdges; seeded end-to-end vs `MinimumCut/data/input_random_1_6.txt` / matching output file).

## Phase 4 — Stub scaffolding for Select + LinearAlgebra (signatures + TODO bodies only)

Mirror the `cpp/misc` / `rust/algorithms-misc` / `lean4/Algorithms/Misc/Basic.lean` pattern exactly:
- `cpp/select/` (r_select, d_select) and `cpp/linear_algebra/` (mat_mul, rec_mat_mul, strassen, modified_gram_schmidt — spelled correctly): headers with templated declarations, `// TODO: User implements` stub sources, gtest placeholder, CMakeLists; register both in `cpp/CMakeLists.txt`.
- `rust/algorithms-select/` and `rust/algorithms-linear-algebra/`: Cargo.toml + `lib.rs` signatures with placeholder bodies/tests; add to workspace `members`.
- `lean4/Algorithms/Select/Basic.lean` and `lean4/Algorithms/LinearAlgebra/Basic.lean` with `sorry` bodies; import both in `lean4/Algorithms.lean`.
- Flag (don't change): `cpp/CMakeLists.txt` sets C++17; user targets C++26 — note in README/porting doc for the user to bump.

## Phase 5 — Docs

- New `docs/porting-notes.md`: per-algorithm preconditions, invariants, termination arguments (needed for Lean `termination_by`), and known kept limitations (closest-pair distinct-x precondition; DSelect upper-median convention; kosaraju in-place mutation; ModifiedGramSchmidt spelling). Same tone as `docs/python-rust-type-mapping.md`.
- README.md: link the new Select/LinearAlgebra stubs (currently "Coming Soon").
- Refresh `tests/TEST_COVERAGE_REPORT.md` with final counts.

## Verification

```bash
cd /home/nadim/Source/Algorithms && source .venv/bin/activate
pytest                                                   # all pass, ~101 → ~130 tests
python -m mypy Sort/MergeSort.py tests/test_mergesort.py --strict
# Import side-effect check — must print nothing:
python -c "import Sort.Sort, Sort.MergeSort, Misc.CountInversions, Search.Search, MinimumCut.MinimumCut, LinearAlgebra.Python.MatMul, LinearAlgebra.Python.ModfiedGramShmidt, RecursiveIntegerMultiplication.Recursive_IntegerMultiplication, RecursiveIntegerMultiplication.Karatsuba_Integer_Multiplication"
python -c "import sys; sys.path.insert(0,'DataStructures'); import Node, LinkedList, DoubleLinkedList, Stack, Queue, Graph, bfs, dfs"
# Scaffolding sanity:
cmake -S cpp -B cpp/build && cmake --build cpp/build
(cd rust && cargo check)
(cd lean4 && lake build)    # sorry warnings expected, no errors
```
