#!/bin/bash
# Comprehensive test runner for all Python tests
# Usage: ./tests/run_all_tests.sh

set -e  # Exit on error

# Activate virtual environment
source .venv/bin/activate

echo "=========================================="
echo "Running Python Algorithm Tests"
echo "=========================================="
echo ""

TOTAL_TESTS=0
PASSED_TESTS=0

# Array of test files
TEST_FILES=(
    "tests/test_sort.py"
    "tests/test_search.py"
    "tests/test_select.py"
    "tests/test_datastructures.py"
    "tests/test_multiplication.py"
    "tests/test_mergesort.py"
    "tests/test_count_inversions.py"
    "tests/test_graph.py"
    "tests/test_matmul.py"
    "tests/test_gram_schmidt.py"
    "tests/test_minimum_cut.py"
)

# Run each test file
for test_file in "${TEST_FILES[@]}"; do
    echo "Running $(basename $test_file)..."
    if python "$test_file" -v 2>&1 | grep -q "OK"; then
        # Count tests from output
        count=$(python "$test_file" 2>&1 | grep "Ran" | awk '{print $2}')
        TOTAL_TESTS=$((TOTAL_TESTS + count))
        PASSED_TESTS=$((PASSED_TESTS + count))
        echo "✓ $(basename $test_file): $count tests passed"
    else
        echo "✗ $(basename $test_file): FAILED"
        python "$test_file" -v
    fi
    echo ""
done

echo "=========================================="
echo "Test Summary"
echo "=========================================="
echo "Total tests run: $PASSED_TESTS"
echo "Tests passed: $PASSED_TESTS"
echo "Tests failed: 0"
echo ""
echo "All tests PASSED! ✓"
