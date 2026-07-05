# Test Coverage Report

Generated: 2026-07-02

## Summary

Total test files: 11
All Python algorithm modules have test coverage.

## Test Files and Coverage

| Test file | Tests | Covers |
|---|---|---|
| test_sort.py | 13 | python/sort/sort.py (Quick/Bubble/Insertion/Merge) + empty-array, dtype-preservation, seeded-QuickSort determinism |
| test_mergesort.py | 7 | python/sort/merge_sort.py (typed reference version) |
| test_search.py | 8 | python/search/search.py: binary search, SecondLargest (incl. non-mutation), 1D/2D closest pair (incl. coincident points, D&C vs brute force), ThreeSum, Rselect |
| test_select.py | 5 | python/select/r_select.py + d_select.py, incl. even-sized tail groups (14/23 elements) and ValueError inputs |
| test_datastructures.py | 51 | Node, Stack, Queue, LinkedList, DoubleLinkedList, LinkedNumber + regression guards (empty-list search, insert(0) size, tail clearing, silent is_empty) |
| test_graph.py | 14 | python/data_structures/graph.py: BFS, DFS, connected components, topological sort, reversal, Kosaraju (returns SCC count) |
| test_multiplication.py | 12 | python/integer_multiplication/: both algorithms, helpers, odd digit counts, 20-digit big integers, negative digit counting |
| test_count_inversions.py | 8 | python/misc/count_inversions.py: brute force + merge-sort counting, empty array, dtype |
| test_matmul.py | 9 | python/linear_algebra/mat_mul.py: VecDot, MatMul, RecMatMult, Strassen vs NumPy; shape-mismatch errors |
| test_gram_schmidt.py | 3 | python/linear_algebra/modified_gram_schmidt.py: orthonormality, QR reconstruction, dependent-column error |
| test_minimum_cut.py | 8 | python/minimum_cut/minimum_cut.py: graph ops, seeded Karger trials vs fixture expected outputs |

Total: 138 test functions.

## Running

```bash
source .venv/bin/activate
pytest              # all tests via pytest.ini (testpaths = python/tests)
./python/tests/run_all_tests.sh   # unittest-style per-file runner
```

## Notes

- Randomized algorithms (QuickSort, Karger) are tested with seeded RNGs for
  determinism.
- The divide-and-conquer closest pair is only tested with distinct
  x-coordinates — that is a documented precondition (see docs/porting-notes.md).
- LinearAlgebra recursive multiplications are only tested on square
  power-of-2 matrices — documented precondition.
