# Python to Rust Type Mapping Guide

This document captures the type hinting concepts implemented in the MergeSort algorithm to help understand Rust type system concepts from Python.

## Overview

We enhanced the Python MergeSort implementation with comprehensive type hints that mirror Rust's type system concepts. This provides a bridge for understanding Rust's ownership, generics, and type safety from a Python perspective.

## Core Type Concepts

### Generic Type Variables

**Python:**
```python
from typing import TypeVar, Any
import numpy as np

# Type variable for numeric types - similar to Rust's generic T with trait bounds
NumericType = TypeVar('NumericType', bound=np.floating[Any])
```

**Rust:**
```rust
// Generic function with trait bounds
fn merge_sort<T>(array: &[T]) -> Vec<T>
where
    T: Clone + PartialOrd + Debug,
```

**Key Learning:** Python's `TypeVar` with `bound` parameter is equivalent to Rust's trait bounds (`T: Clone + PartialOrd`).

### Function Signatures

**Python:**
```python
def Merge(left: NDArray[NumericType], right: NDArray[NumericType], merged: NDArray[NumericType]) -> NDArray[NumericType]:
    # Function body
    
def MergeSort(array: NDArray[NumericType]) -> NDArray[NumericType]:
    # Function body
```

**Rust:**
```rust
fn merge<T>(left: &[T], right: &[T]) -> Vec<T> 
where T: Clone + PartialOrd + Debug
{
    // Function body
}

pub fn merge_sort<T>(array: &[T]) -> Vec<T>
where T: Clone + PartialOrd + Debug
{
    // Function body
}
```

**Key Learning:** 
- Python's `NDArray[NumericType]` parameters ≈ Rust's `&[T]` (borrowed slice)
- Python's `-> NDArray[NumericType]` return ≈ Rust's `-> Vec<T>` (owned vector)

### Variable Declarations

**Python:**
```python
i: int = 0  # left array index - equivalent to Rust's let mut i = 0
j: int = 0  # right array index - equivalent to Rust's let mut j = 0 
k: int = 0  # merged array index
mid: int = array.shape[0] // 2  # equivalent to Rust's let mid = array.len() / 2
merged: NDArray[NumericType] = np.zeros(array.shape[0], dtype=array.dtype)
```

**Rust:**
```rust
let mut i = 0; // left array index
let mut j = 0; // right array index
let mut k = 0; // merged array index
let mid = array.len() / 2;
let mut merged = Vec::with_capacity(left.len() + right.len());
```

**Key Learning:** Python type annotations help visualize Rust's explicit mutability (`mut`) and type inference.

## Array/Collection Types

### Ownership Concepts

**Python (Conceptual Mapping):**
```python
# Input parameter (borrowed reference concept)
array: NDArray[NumericType]  # Maps to Rust's &[T]

# Return value (owned data concept)  
-> NDArray[NumericType]      # Maps to Rust's Vec<T>

# Array slicing (borrowing concept)
left = MergeSort(array[mid:])     # Maps to &array[mid..]
right = MergeSort(array[0:mid])   # Maps to &array[0..mid]
```

**Rust (Actual Implementation):**
```rust
// Input parameter (borrowed slice)
array: &[T]

// Return value (owned vector)
-> Vec<T>

// Array slicing (borrowing)
let left_sorted = merge_sort(&array[mid..]);
let right_sorted = merge_sort(&array[0..mid]);
```

## Test File Type Annotations

### Test Setup

**Python:**
```python
from typing import List, Any
from numpy.typing import NDArray

class TestMergeSort(unittest.TestCase):
    def setUp(self) -> None:
        # Type hint for test arrays - similar to Rust's Vec<Vec<T>> concept  
        self.test_arrays: List[NDArray[np.float64]] = [
            np.array([5, 2, 8, 1, 9, 3]),
            np.array([1, 1, 1, 1]),
            # ... more test cases
        ]
```

**Rust Equivalent:**
```rust
struct TestMergeSort {
    test_arrays: Vec<Vec<i32>>,  // Vec of Vecs
}

impl TestMergeSort {
    fn new() -> Self {
        Self {
            test_arrays: vec![
                vec![5, 2, 8, 1, 9, 3],
                vec![1, 1, 1, 1],
                // ... more test cases
            ],
        }
    }
}
```

### Test Method Signatures

**Python:**
```python
def test_mergesort_basic(self) -> None:
    for arr in self.test_arrays:
        expected: NDArray[np.float64] = np.sort(arr.copy())
        result: NDArray[np.float64] = MergeSort(arr.copy())
```

**Rust:**
```rust
#[test]
fn test_merge_sort_basic() {
    let test_cases = vec![
        (vec![5, 2, 8, 1, 9, 3], vec![1, 2, 3, 5, 8, 9]),
        // ... more cases
    ];
    
    for (input, expected) in test_cases {
        let result: Vec<i32> = merge_sort(&input);
        assert_eq!(result, expected);
    }
}
```

## Benefits for Rust Learning

1. **Type Safety:** Python type hints demonstrate how explicit types catch errors at development time
2. **Generic Programming:** `TypeVar` concepts map directly to Rust's generic `<T>` parameters
3. **Ownership Patterns:** Type annotations help visualize data flow and ownership transfer
4. **Memory Safety:** Understanding when data is borrowed vs owned through type signatures
5. **Trait Bounds:** `bound=` parameter in Python TypeVar mirrors Rust's `where` clauses

## Running Type Checks

### Python (mypy)
```bash
pip install mypy
python -m mypy python/sort/merge_sort.py --strict
```

### Rust (built-in)
```bash
cargo check  # Type checking
cargo build  # Compile with type validation
```

## Files Modified

- `python/sort/merge_sort.py` - Added comprehensive type hints
- `python/tests/test_mergesort.py` - Added type annotations to all test methods
- Both files now demonstrate Python-to-Rust type mapping concepts

This type-annotated Python code serves as a bridge to understanding Rust's type system, ownership model, and memory safety guarantees.