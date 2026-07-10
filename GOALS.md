# Goals — Algorithms

A multi-language learning repo of algorithms and data structures from "Algorithms
Illuminated" (Roughgarden), CLRS, and Sedgewick. Python is the complete reference
implementation; C++, Rust, and Lean 4 ports are user-written and mostly stubs, mentored
by the `portpal` hints-only assistant with a parity harness verifying them against Python.

## Goals

- [x] Merge sort, quick sort, insertion sort, bubble sort in Python (`python/sort/`)
- [x] Binary search, closest pair, ThreeSum, second largest in Python (`python/search/search.py`)
- [x] Randomized and deterministic Select in Python (`python/select/`)
- [x] Karatsuba and recursive integer multiplication in Python (`python/integer_multiplication/`)
- [x] Strassen matrix multiply and modified Gram-Schmidt (QR) in Python (`python/linear_algebra/`)
- [x] Karger's minimum cut in Python (`python/minimum_cut/minimum_cut.py`)
- [x] BFS and DFS plus linked list / stack / queue / graph structures in Python (`python/data_structures/`)
- [x] Count inversions in Python, with pytest coverage across all modules (`python/tests/`)
- [x] Legacy standalone C++ implementations: randomized Select and Karger's minimum cut (`legacy/`)
- [x] Legacy standalone Rust implementation: modified Gram-Schmidt (`legacy/linear_algebra/rust/`)
- [x] portpal parity harness with Python adapter and fixtures (`parity/`, `python/parity/`)
- [ ] Implement the sort algorithms (merge/quick/insertion/bubble) in Rust (`rust/algorithms-sort/`)
- [ ] Implement merge sort in C++ (`cpp/sort/src/merge_sort.cpp`, currently a TODO stub)
- [ ] Implement the sort algorithms in Lean 4, replacing the `sorry` stubs (`lean4/Algorithms/Sort/Basic.lean`)
- [ ] Implement Select (rSelect/dSelect) in the unified C++, Rust, and Lean 4 trees
- [ ] Implement linear algebra (matMul, Strassen, QR) in the C++, Rust, and Lean 4 trees
- [ ] Port Karatsuba integer multiplication to C++, Rust, and Lean 4
- [ ] Port BFS/DFS graph algorithms to C++, Rust, and Lean 4
