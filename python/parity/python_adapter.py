#!/usr/bin/env python3
"""portpal parity adapter: runs fixture cases through the Python REFERENCE code.

Usage:
    python python/parity/python_adapter.py <fixture.json>              # run, print results JSON
    python python/parity/python_adapter.py --generate <fixture.json>…  # fill "expected" in place

This file is the source of truth for expected outputs — it only *calls* the
reference implementations and normalizes their results to JSON; it contains no
algorithm logic of its own.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

import numpy as np  # noqa: E402

from python.sort.merge_sort import MergeSort  # noqa: E402
from python.sort.sort import BubbleSort, InsertionSort, QuickSort  # noqa: E402
from python.select.r_select import RSelect  # noqa: E402
from python.select.d_select import DSelect  # noqa: E402
from python.search.search import BinarySearchIterative, SecondLargest  # noqa: E402
from python.misc.count_inversions import Sort_And_CountInV  # noqa: E402
from python.integer_multiplication.karatsuba_integer_multiplication import (  # noqa: E402
    getNumDigits,
    karatsubaMultiplication,
    recursiveIntegerMultiplication,
)
from python.linear_algebra.mat_mul import (  # noqa: E402
    MatMul,
    RecMatMult,
    VecDot,
    strassenRecMat,
)
from python.linear_algebra.modified_gram_schmidt import modified_gramshmidt  # noqa: E402


def _int_array(values) -> np.ndarray:
    return np.array(values, dtype=np.int64)


def _quick_sort(inp):
    arr = _int_array(inp["array"])
    QuickSort(arr, 0, arr.shape[0], rng=np.random.default_rng(42))
    return arr.tolist()


def _binary_search(inp):
    idx = int(BinarySearchIterative(_int_array(inp["array"]), inp["target"]))
    return None if idx == -1 else idx


def _second_largest(inp):
    result = SecondLargest(np.array(inp["array"], dtype=np.float64))
    second = result[1]
    return None if np.isneginf(second) else int(second)


def _multiply(fn, inp):
    x, y = int(inp["x"]), int(inp["y"])
    return str(fn(x, y, getNumDigits(x), getNumDigits(y)))


def _matrix_to_list(m) -> list:
    # RecMatMult/strassenRecMat return a bare scalar for 1x1 inputs
    if np.isscalar(m) or getattr(m, "ndim", 2) == 0:
        return [[int(m)]]
    return np.asarray(m).tolist()


def _gram_schmidt(inp):
    q, r = modified_gramshmidt(np.array(inp["a"], dtype=np.float64))
    return {"q": q.tolist(), "r": r.tolist()}


HANDLERS = {
    "insertion_sort": lambda inp: InsertionSort(_int_array(inp["array"])).tolist(),
    "bubble_sort": lambda inp: BubbleSort(_int_array(inp["array"]))[0].tolist(),
    "merge_sort": lambda inp: MergeSort(_int_array(inp["array"])).tolist(),
    "quick_sort": _quick_sort,
    "r_select": lambda inp: RSelect(list(inp["array"]), inp["ith"]),
    "d_select": lambda inp: DSelect(list(inp["array"]), inp["ith"]),
    "binary_search": _binary_search,
    "second_largest": _second_largest,
    "count_inversions": lambda inp: int(Sort_And_CountInV(_int_array(inp["array"]))[1]),
    "standard_multiply": lambda inp: _multiply(recursiveIntegerMultiplication, inp),
    "karatsuba_multiply": lambda inp: _multiply(karatsubaMultiplication, inp),
    "vec_dot": lambda inp: int(VecDot(_int_array(inp["a"]), _int_array(inp["b"]))),
    "mat_mul": lambda inp: MatMul(_int_array(inp["a"]), _int_array(inp["b"])).tolist(),
    "rec_mat_mul": lambda inp: _matrix_to_list(RecMatMult(_int_array(inp["a"]), _int_array(inp["b"]))),
    "strassen": lambda inp: _matrix_to_list(strassenRecMat(_int_array(inp["a"]), _int_array(inp["b"]))),
    "modified_gram_schmidt": _gram_schmidt,
}


def run_fixture(path: Path) -> list[dict]:
    fixture = json.loads(path.read_text())
    handler = HANDLERS.get(fixture["algorithm"])
    results = []
    for case in fixture["cases"]:
        if handler is None:
            results.append({"name": case["name"], "error": f"no handler for {fixture['algorithm']}"})
            continue
        try:
            results.append({"name": case["name"], "output": handler(case["input"])})
        except Exception as e:  # surfaced per-case, runner keeps going
            results.append({"name": case["name"], "error": f"{type(e).__name__}: {e}"})
    return results


def generate(path: Path) -> None:
    fixture = json.loads(path.read_text())
    results = {r["name"]: r for r in run_fixture(path)}
    for case in fixture["cases"]:
        r = results[case["name"]]
        if "error" in r:
            raise SystemExit(f"{path}: case {case['name']!r} failed: {r['error']}")
        case["expected"] = r["output"]
    path.write_text(json.dumps(fixture, indent=1) + "\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    if args[0] == "--generate":
        for p in args[1:]:
            generate(Path(p))
            print(f"generated: {p}", file=sys.stderr)
    else:
        print(json.dumps(run_fixture(Path(args[0]))))


if __name__ == "__main__":
    main()
