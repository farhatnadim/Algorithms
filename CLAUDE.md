# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an algorithms and data structures learning repository implementing fundamental algorithms from "Algorithms Illuminated" (Roughgarden, Stanford), "Introduction to Algorithms" (Cormen et al., MIT), and "Algorithms" (Sedgewick, Princeton). The codebase is primarily written in Python with some C++ and Rust implementations.

## Code Architecture

### Language Structure
- **Python**: Primary implementation language using NumPy arrays for data structures
- **C++**: Performance-focused implementations with CMake build system and Google Test framework
- **Rust**: Systems programming implementations (LinearAlgebra)

### Directory Organization
- **Sort/**: Sorting algorithms (Bubble, Insertion, Merge, Quick Sort) in `Sort.py`, plus standalone `MergeSort.py` with type hints
- **Search/**: Search algorithms (Binary Search, Second Largest, Closest Pair, ThreeSum)
- **Select/**: Selection algorithms with both Python and C++ implementations
- **DataStructures/**: Graph, LinkedList, DoubleLinkedList, Stack, Queue, BFS, DFS
- **LinearAlgebra/**: Matrix operations including Strassen's multiplication (Python and Rust implementations)
- **RecursiveIntegerMultiplication/**: Standard and Karatsuba integer multiplication
- **MinimumCut/**: Graph minimum cut algorithms (Python and C++)
- **LeetCode/**: Problem-specific C++ implementations with CMake build system
- **Misc/**: Count inversions and other algorithms
- **tests/**: Unit tests for Python implementations

### Key Design Patterns
- All Python implementations use NumPy arrays
- CamelCase naming convention for functions
- Test files use `sys.path.append()` to import from parent directories

## Development Commands

### Python Testing
```bash
# Run individual test files (recommended - pytest has import conflicts with argparse)
python tests/test_sort.py
python tests/test_search.py
python tests/test_select.py
python tests/test_multiplication.py
python tests/test_mergesort.py
```

### Type Checking
```bash
python -m mypy Sort/MergeSort.py --strict
python -m mypy tests/test_mergesort.py --strict
```

### C++ Building and Testing
```bash
# LeetCode problems
cd LeetCode/1.TwoSum && mkdir build && cd build && cmake .. && make && ctest

# MinimumCut
cd MinimumCut/cpp && mkdir build && cd build && cmake .. && make

# Select algorithms
cd Select/Cpp && mkdir build && cd build && cmake .. && make
```

### Rust Building
```bash
cd LinearAlgebra/Rust/modified_gram_shmidt
cargo build
cargo run
```

### Dependencies
```bash
pip install -r requirements.txt  # numpy>=1.19.0
pip install mypy  # Optional, for type checking
```

## Common Issues

- **Import Conflicts**: Some modules use argparse at module level, causing pytest collection failures. Run test files individually.
- **Algorithm Bugs**: Some sorting implementations (BubbleSort, InsertionSort) have known bugs - this is a learning repository.
- **Graph Class**: Assumes vertices are sorted in descending order with no missing vertices in sequence.

## Documentation

- **docs/python-rust-type-mapping.md**: Guide showing Python type hints mapping to Rust concepts
- **docs/rust-lean4-conversion.md**: Rust to Lean 4 conversion patterns
