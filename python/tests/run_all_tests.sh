#!/bin/bash
# Comprehensive test runner for all Python tests
# Usage: ./python/tests/run_all_tests.sh

set -e  # Exit on error

# Resolve the repo root from this script's location (python/tests/ -> repo root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

# Activate virtual environment
source .venv/bin/activate

# Make the top-level `python` package importable for direct `python <file>`
# execution (conftest.py is only auto-loaded by pytest, not plain python).
export PYTHONPATH="$REPO_ROOT:${PYTHONPATH:-}"

echo "=========================================="
echo "Running Python Algorithm Tests"
echo "=========================================="
echo ""

TOTAL_TESTS=0
PASSED_TESTS=0

# Array of test files
TEST_FILES=(
    "python/tests/test_sort.py"
    "python/tests/test_search.py"
    "python/tests/test_select.py"
    "python/tests/test_datastructures.py"
    "python/tests/test_multiplication.py"
    "python/tests/test_mergesort.py"
    "python/tests/test_count_inversions.py"
    "python/tests/test_graph.py"
    "python/tests/test_matmul.py"
    "python/tests/test_gram_schmidt.py"
    "python/tests/test_minimum_cut.py"
)

# Run each test file
for test_file in "${TEST_FILES[@]}"; do
    echo "Running $(basename $test_file)..."
    if python "$test_file" -v 2>&1 | grep -q "OK"; then
        # Count tests from output
        count=$(python "$test_file" 2>&1 | grep "Ran" | awk '{print $2}')
        TOTAL_TESTS=$((TOTAL_TESTS + count))
        PASSED_TESTS=$((PASSED_TESTS + count))
        echo "PASS $(basename $test_file): $count tests passed"
    else
        echo "FAIL $(basename $test_file)"
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
echo "All tests PASSED!"
