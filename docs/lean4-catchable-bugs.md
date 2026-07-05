# Bugs Lean 4 Would Have Caught

This catalog preserves real bugs that lived in this repo's Python code (fixed
2026-07, original versions in git history before that date). Each entry shows
the buggy code verbatim, the fix, and — the point of this document — **which
Lean 4 mechanism catches it and at what stage**.

Use it as an exercise list: when porting each algorithm, first write the buggy
version in Lean and confirm Lean rejects it (or that the correctness theorem
becomes unprovable), then write the fixed version.

There are three tiers, and the difference matters:

| Tier | Mechanism | When it fires | Effort |
|---|---|---|---|
| 1 | Type checker | immediately, while typing | free |
| 2 | Termination checker / totality | at `def`, unless you cheat with `partial` | free-ish |
| 3 | Correctness theorem | only when you state and try to prove a property | you must write the theorem |

Tier 3 is the sobering one: those bugs compile and run fine in Lean too.
Lean only catches them if you do the proving work.

---

## Tier 2: caught by the termination checker

### Bug 1 — MergeSort infinite recursion on empty input

`python/sort/sort.py` (original):

```python
def MergeSort(array):
    merged = np.zeros(array.shape[0])
    if array.shape[0] == 1:        # BUG: no case for shape[0] == 0
        return array
    else:
        left  = MergeSort(array[array.shape[0]//2:])   # n=0: array[0:] = whole array!
        right = MergeSort(array[0:array.shape[0]//2])  # n=0: array[0:0] = []
        ...
```

With an empty array, `n // 2 == 0`, so one recursive call receives the *same*
(empty) array — infinite recursion. Python happily accepts the definition and
only fails at runtime (`RecursionError`), and only if a test ever passes an
empty array (ours didn't — the old test swallowed it with `try/except: pass`).

**In Lean:** write it with the same base case and the termination checker
rejects the `def` outright — it cannot show `array[mid:]` is smaller than
`array` when `array.length = 0`. You are forced to either handle `[]` or
prove a false decreasing-measure goal. The same bug existed in
`python/misc/count_inversions.py` (`Sort_And_CountInV`).

**Exercise:** port with `if array.length == 1` as the only base case; watch
`termination_by`/structural recursion fail. Note that `partial def` makes
Lean accept it — which is why `docs/rust-lean4-conversion.md`'s `partial`
shortcut throws away exactly this protection.

### Bug 2 — Closest pair: degenerate split under duplicate x-coordinates

`python/search/search.py` `closestPair` (still present, documented as a precondition):

```python
Ly = [p for p in SortedInY if p[0] <= mid_x]
Ry = [p for p in SortedInY if p[0] >  mid_x]
```

If all points share one x-coordinate, `Ry` is empty and `Ly` is the *entire*
input — the recursion on `(Lx, Ly)` does not shrink in the y-list, and `Rx`
side crashes. Python: latent runtime bug.

**In Lean:** the recursion is on lists whose size you must prove strictly
decreases. The membership-based split gives you no such proof — the goal
`Ly.length < SortedInY.length` is simply not true without the distinct-x
hypothesis. Lean forces you to *discover the precondition* and either take it
as a hypothesis (`h : ∀ p q ∈ points, p ≠ q → p.x ≠ q.x`) or fix the split to
be index-consistent. This is the best example in the repo of the termination
checker surfacing a hidden mathematical assumption.

---

## Tier 2: caught by totality (no partial functions, `Option` instead of crashes)

### Bug 3 — RSelect/DSelect on empty input

`python/select/r_select.py` (original):

```python
def RSelect(array, ith):
    if len(array) == 1:
        return array[0]
    pivot_index = random.randint(0, len(array) - 1)   # empty: randint(0, -1) → ValueError
```

**In Lean:** `def rSelect (arr : List α) (ith : Nat) : α` is not definable —
what do you return for `[]`? Lean makes you choose the honest type up front:
`Option α`, or a hypothesis `(h : arr ≠ [])`. The crash is unrepresentable.

### Bug 4 — Sentinel values instead of absent values

Original code returned `-np.inf` (SecondLargest on 1 element), `-1`
(LinkedList errors), or `None`-sometimes (`pop` on empty Stack) — three
different conventions, all silently mixable with real data.

**In Lean:** `Option α` is the only idiom, and every caller is forced by the
type checker to pattern-match on `none`. Not a compile *error* in Python;
structurally impossible to forget in Lean.

---

## Tier 1: caught by the type checker immediately

### Bug 5 — float64 buffer corrupting integer data

`python/sort/sort.py`, `python/misc/count_inversions.py` (original):

```python
merged = np.zeros(array.shape[0])   # BUG: dtype defaults to float64
```

Sorting `[3, 1, 2]` (ints) returned `[1.0, 2.0, 3.0]` (floats). NumPy coerces
silently; tests using `assert_array_equal` compare across dtypes and pass.

**In Lean:** a generic `merge : List α → List α → List α` cannot produce a
`List Float` from `List Int` — there is no implicit numeric coercion between
container element types. The bug is untypeable.

### Bug 6 — function annotated `-> int` returning `None`

`python/minimum_cut/minimum_cut.py` (original): `min_cut(self) -> int` had no return
statement (fell off the end → `None`). Python annotations are comments;
mypy would flag it, CPython doesn't.

**In Lean:** a `def minCut : Graph → Nat` whose body doesn't produce a `Nat`
in every branch does not elaborate. Same class: `select_edge_random`'s bare
`except` left `vertex2` possibly **unbound**, and the Select CLI's dead branch
left `array` unbound (`NameError`) — Lean has no unbound names; every variable
is introduced by a binder that must be given a value.

---

## Tier 3: caught ONLY by proving a correctness theorem

These compile, terminate, and pass casual tests — in Lean too. They die only
when you state the spec.

### Bug 7 — the odd-digit recombination shift (the big one)

`python/integer_multiplication/` (original, both files):

```python
a = number1 // 10**(n1//2)
b = number1 %  10**(n1//2)          # number1 = a·10^(n1//2) + b
...
return 10**(n1)*ac + 10**(n3)*(ad+bc) + bd    # BUG: high shift must be 2*(n1//2)
```

`10^n1 = 10^(2·(n1//2))` only when `n1` is even. Every test used 1-, 2-, 4- or
8-digit numbers — all even or base-case — so 9 tests passed for years while
`123 × 456` was wrong.

**In Lean:** the definition is total and terminates; the compiler is silent.
But state the spec:

```lean
theorem recMul_correct (a b n : Nat) (h : ...) :
    recursiveIntegerMultiplication a b n n = a * b
```

and the induction dies in the odd case: after rewriting
`number1 = a * 10^(n/2) + b`, the algebra needs `10^(2*(n/2))` and you're
holding `10^n`. The stuck proof goal literally points at the wrong exponent.
This is the repo's best argument for doing proofs at all — no amount of
type-checking catches it, and the power-of-2 test suite didn't either.

### Bug 8 — DSelect pivot not an element of the array

`python/select/d_select.py` (original):

```python
C = [statistics.median(array[i:i+5]) for i in range(0, len(array), 5)]
p = DSelect(C, len(C) // 2)
index_p = array.index(p)            # BUG: p may be a mean of two elements → ValueError
```

`statistics.median` of an even-sized (tail) group averages the two middle
values — a number that may not be in the array. First crashes at n = 14;
tests only used n ≤ 6.

**In Lean:** `List.indexOf p array` is total (returns `array.length` when
absent), so no crash — but the moment you index with it, or prove
`dSelect_mem : dSelect arr i ∈ arr` or the selection spec, you face the
obligation `p ∈ array` and cannot discharge it: the median-of-means is *not*
provably a member. Choosing `sorted(group)[len // 2]` (upper median) makes
membership provable by construction. A membership proof obligation is exactly
the shape of this bug.

### Bug 9 — size invariant broken by double increment

`python/data_structures/double_linked_list.py` (original): `insert(pos=0, item)` called
`insert_at_beginning` (which does `size += 1`) and then incremented `size`
again.

**In Lean:** an intrinsic invariant — e.g. carrying `(h : size = list.length)`
in the structure, or proving `(insert l pos x).size = l.size + 1` — fails by
exactly one. Off-by-one bookkeeping bugs are what data-structure invariant
proofs are for.

### Bug 10 — inversion counting vs duplicates (REAL, found 2026-07-03)

`python/misc/count_inversions.py` merge used strict `left[i] < right[j]` (original):

```python
if left[i] < right[j]:
    merged[k] = left[i]; i += 1
else:
    merged[k] = right[j]; j += 1
    splitInv += left.shape[0] - i   # ties land here and are overcounted
```

On equal elements the strict `<` falls into the counting branch, so equal
pairs were counted as inversions: `[5,5,5]` → 3 instead of 0. The tests
dodged duplicates entirely ("handled separately due to implementation
differences") and the bug survived until the portpal parity harness compared
the divide-and-conquer count against `bruteForeCountInversion` on a duplicate
fixture. Fix: `<=` so ties take from the left without counting.

**In Lean:** provable spec pins it:
`countInv l = (l.pairs.filter (fun (i, j) => i < j ∧ l[i] > l[j])).length` —
the brute-force definition *is* the spec; proving the merge version equal to
it forces the tie-handling decision. Good candidate for your first
non-trivial equivalence proof.

---

## Suggested workflow per algorithm

1. Port the **buggy** version first (from this file / git history).
2. Record what happens: rejected at `def`? forced into `Option`? or silent?
3. If silent, write the Tier-3 theorem from `docs/porting-notes.md`'s
   invariants and watch where the proof gets stuck.
4. Port the fixed version and finish the proof.

Scorecard to fill in as you go:

| # | Bug | Expected catch | Actually caught? |
|---|-----|----------------|------------------|
| 1 | MergeSort empty recursion | termination checker | |
| 2 | closest-pair duplicate-x split | termination checker | |
| 3 | RSelect empty input | totality / `Option` | |
| 4 | sentinel returns | `Option` at call sites | |
| 5 | float buffer for ints | type checker | |
| 6 | `None` from `-> int`, unbound vars | elaborator | |
| 7 | odd-digit shift | `recMul_correct` proof | |
| 8 | DSelect pivot membership | `p ∈ arr` obligation | |
| 9 | size double increment | invariant proof | |
| 10 | inversion ties | spec-equivalence proof | |
