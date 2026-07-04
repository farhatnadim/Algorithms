# Python → C++26 Type & Idiom Mapping

Companion to `python-rust-type-mapping.md`, for porting the Python reference
code to the `cpp/` tree. Feeds portpal's C++ hints. Idiom mapping only — the
algorithm bodies are yours to write.

## Element types and generics

Python's duck typing / NumPy dtypes become function templates constrained by
concepts. The stubs already chose the shape:

```cpp
template <typename T>
void mergeSort(std::vector<T>& arr);   // add a concept: std::totally_ordered<T>
```

- `np.int64` → `std::int64_t` (the parity fixtures use 64-bit ints).
- NumPy's `np.result_type(a, b)` promotion → `std::common_type_t<A, B>`.
- mypy `--strict` ↔ concepts: an unconstrained template fails deep inside the
  instantiation; a concept moves the error to the call site with a readable
  message. Prefer `std::totally_ordered` for comparisons-based algorithms.
- Templates are implemented **in the header** (the stub `.cpp` files stay
  nearly empty or hold explicit instantiations).

## Arrays, slices, views — know which Python slice you are porting

- **NumPy slices are VIEWS** (`array[mid:]` shares the buffer). The C++
  analogue is `std::span<T>` / `span.subspan(offset, count)` — no copy.
- **List slices COPY** (`array[:j]` in RSelect). The C++ analogue is
  constructing a new `std::vector<T>(first, last)` — or better, switch to the
  windowed variant (`Search.Rselect` style) and pass a subspan, per
  `porting-notes.md`.
- Half-open `[left, right)` windows (QuickSort, partition) map directly to
  iterator pairs or `subspan(left, right - left)`. Keep the half-open
  convention explicit; closed-interval conversions breed off-by-ones.

## Absent values and errors

- `raise ValueError(...)` on violated preconditions → this repo's convention
  is `std::optional<T>` returns (see the stubs), or `std::expected<T, E>`
  when the caller needs the reason. Match the stub's signature.
- `return None` (e.g. pop on empty) → `std::nullopt`.
- Sentinels are banned in ports: `-np.inf` (SecondLargest) and `-1`
  (BinarySearch absent) both become `std::optional` — the fixtures encode
  absent as JSON `null`.

## Integers: Python's are arbitrary precision, C++'s are not

- **Signed overflow is UB in C++**, not a wrong answer you can test for.
  Karatsuba/standard multiplication intermediates overflow 64 bits fast; the
  stubs (and fixtures) therefore pass **decimal strings** — implement
  digit-string arithmetic, or constrain inputs so products fit `__int128`
  and document the limit.
- `10**n` has no C++ analogue; think in digit shifts on the string
  representation rather than powers.
- `len(str(abs(n)))` (digit count) and `int.bit_length()` need explicit
  loops; watch `std::size_t` unsigned arithmetic.

## Mutation vs. return style

- `InsertionSort` mutates in place *and* returns the array; in C++ pick one:
  the stubs chose in-place `void f(std::vector<T>&)`. Follow them.
- Tuple returns (`BubbleSort` → `(array, count)`,
  `modified_gramshmidt` → `(Q, R)`) → `std::pair` / `std::tuple` / a small
  struct — check what the stub promises before inventing a shape.

## Randomness

- The reference's injectable `np.random.Generator` parameter →
  `std::mt19937_64&` (a URBG reference parameter), seeded by the caller.
  Never `rand()`, never a hidden global — cross-language tests depend on it.
- `rng.integers(lo, hi)` (half-open) →
  `std::uniform_int_distribution<std::int64_t>{lo, hi - 1}` — note the
  distribution's **closed** range; this is a classic porting off-by-one.

## Floats

- Same IEEE 754 semantics, but different summation order changes last bits:
  parity uses `float_tol` for Gram-Schmidt, and the `1e-10` dependence
  tolerance should be a defaulted parameter, not a burned-in constant.
- `np.isclose` → write the comparison explicitly (`std::abs(a-b) <= atol +
  rtol*std::abs(b)`), or use ULP-based helpers in tests.

## Indexing pitfalls (the classics)

- No negative indexing. `array[-1]` → `arr.back()` (after an emptiness
  check).
- `arr.size() - 1` on an empty vector wraps to a huge unsigned value —
  check `empty()` first or use `std::ssize(arr)`.
- Backward loops with unsigned counters (BubbleSort's backward pass,
  `range(end-1, start-1, -1)`) are underflow traps; loop with signed
  indices or restructure.

## Matrices and broadcasting

- 2-D `NDArray` → `std::vector<std::vector<T>>` (the stubs' `Matrix<T>`
  shape). No NumPy broadcasting exists: `RecMatMult`'s 1×1 base case returns
  a *scalar* that broadcasting absorbs — the C++ port must return a 1×1
  matrix explicitly (see `porting-notes.md`, Linear Algebra).
- `np.zeros((m, n), dtype=...)` → construct with sizes and `T{}`; dtype
  discipline is automatic once the element type is a template parameter.

## Testing

- pytest ↔ GoogleTest: `TEST(SortTest, SortsDuplicates)`, `EXPECT_EQ`,
  registered via `gtest_discover_tests` and run with `ctest`. Mirror the
  existing `cpp/<module>/tests/*_test.cpp` layout.
- Precondition tests: with `optional` returns, assert `std::nullopt` — no
  exception-based `assertRaises` analogue needed.

## Build & workflow

- Bump `CMAKE_CXX_STANDARD` from 17 to **26** in `cpp/CMakeLists.txt` when
  you start implementing (tracked in `porting-notes.md`).
- After implementing an algorithm, **uncomment its entry in
  `cpp/parity/registry.cpp`** so `portpal parity` can exercise it.
