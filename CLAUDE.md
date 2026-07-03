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
# Recommended: Use pytest to run all tests
source .venv/bin/activate
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest tests/test_sort.py       # Run specific test file
pytest -k "test_merge"          # Run tests matching pattern

# Alternative: unittest discover
python -m unittest discover -s tests -p "test_*.py"
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

## Claude's Role

**DO NOT write implementation code in C++, Lean4, or Rust.** Claude should:
- Guide and review user-written code
- Fix bugs in existing Python code
- Set up test infrastructure and CI/CD
- Provide code review feedback on correctness, style, and complexity
- Help with documentation

The user writes the actual algorithm implementations; Claude assists with the review workflow.

**Sole exception (agreed 2026-07-03):** the portpal parity-harness *runner glue* —
JSON decode/encode and dispatch code in `rust/parity-runner/`, `cpp/parity/`, and
`lean4/ParityRunner.lean` — may be Claude-written. It contains no algorithm logic;
algorithm bodies remain user-written everywhere.

## Code Quality Requirements

**No bugs should exist in the Python code.** All Python implementations must:
- Pass all unit tests before committing
- Use proper exception types (e.g., `NotImplementedError` not `NotImplemented`)
- Avoid mutable default arguments (e.g., use `edges=None` not `edges=[]`)
- Wrap script-level code in `if __name__ == '__main__':` guards
- Use `is None` / `is not None` instead of `== None` / `!= None`
- Be compatible with NumPy 2.0+ (e.g., use `-np.inf` not `np.NINF`)

Run all tests before committing:
```bash
source .venv/bin/activate
pytest  # Runs all tests
```

## Common Issues

- **Graph Class**: Assumes vertices are sorted in descending order with no missing vertices in sequence.
- **Closest Pair (Search/Search.py)**: The divide-and-conquer closest pair requires points with distinct x-coordinates (see docs/porting-notes.md).

## Documentation

- **docs/python-rust-type-mapping.md**: Guide showing Python type hints mapping to Rust concepts
- **docs/rust-lean4-conversion.md**: Rust to Lean 4 conversion patterns
- **docs/porting-notes.md**: Per-algorithm preconditions, invariants, and termination arguments for the Lean 4 / C++26 ports
- **docs/lean4-catchable-bugs.md**: Catalog of real bugs fixed in the Python (kept verbatim) classified by which Lean 4 mechanism catches them — used as porting exercises
