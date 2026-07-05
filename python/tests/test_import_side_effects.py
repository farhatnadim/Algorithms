"""Importing every algorithm module must be side-effect free (no printing,
no file I/O, no plotting) so the modules are safe to use as a reference
during the Lean 4 / C++26 port."""
import contextlib
import io
import os
import sys
import unittest

# This test lives at python/tests/, so the repo root is three levels up.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestImportSideEffects(unittest.TestCase):
    def test_top_level_modules_import_silently(self):
        sys.path.insert(0, REPO_ROOT)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            import python.sort.sort
            import python.sort.merge_sort
            import python.misc.count_inversions
            import python.search.search
            import python.select.r_select
            import python.select.d_select
            import python.minimum_cut.minimum_cut
            import python.linear_algebra.mat_mul
            import python.linear_algebra.modified_gram_schmidt
            import python.integer_multiplication.recursive_integer_multiplication
            import python.integer_multiplication.karatsuba_integer_multiplication
        self.assertEqual(buf.getvalue(), "")

    def test_datastructures_modules_import_silently(self):
        # DataStructures modules import each other via absolute python.* paths,
        # so only the repo root needs to be on sys.path.
        sys.path.insert(0, REPO_ROOT)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            import python.data_structures.node
            import python.data_structures.linked_list
            import python.data_structures.double_linked_list
            import python.data_structures.stack
            import python.data_structures.queue
            import python.data_structures.graph
            import python.data_structures.bfs
            import python.data_structures.dfs
        self.assertEqual(buf.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
