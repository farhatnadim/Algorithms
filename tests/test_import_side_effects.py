"""Importing every algorithm module must be side-effect free (no printing,
no file I/O, no plotting) so the modules are safe to use as a reference
during the Lean 4 / C++26 port."""
import contextlib
import io
import os
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestImportSideEffects(unittest.TestCase):
    def test_top_level_modules_import_silently(self):
        sys.path.insert(0, REPO_ROOT)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            import Sort.Sort
            import Sort.MergeSort
            import Misc.CountInversions
            import Search.Search
            import Select.Python.RSelect
            import Select.Python.DSelect
            import MinimumCut.MinimumCut
            import LinearAlgebra.Python.MatMul
            import LinearAlgebra.Python.ModfiedGramShmidt
            import RecursiveIntegerMultiplication.Recursive_IntegerMultiplication
            import RecursiveIntegerMultiplication.Karatsuba_Integer_Multiplication
        self.assertEqual(buf.getvalue(), "")

    def test_datastructures_modules_import_silently(self):
        # DataStructures/ modules import each other without a package prefix
        # (e.g. `from Node import Vertex`), so the directory itself must be
        # on sys.path for this flat-import style to resolve.
        sys.path.insert(0, os.path.join(REPO_ROOT, 'DataStructures'))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            import Node
            import LinkedList
            import DoubleLinkedList
            import Stack
            import Queue
            import Graph
            import bfs
            import dfs
        self.assertEqual(buf.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
