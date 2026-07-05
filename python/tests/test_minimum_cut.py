import unittest
import random
import os

from python.minimum_cut.minimum_cut import Graph, load_graph

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'minimum_cut', 'data')


def make_square_graph():
    """4-cycle: 1-2, 2-3, 3-4, 4-1 (min cut = 2)"""
    g = Graph()
    g['1'] = ['2', '4']
    g['2'] = ['1', '3']
    g['3'] = ['2', '4']
    g['4'] = ['3', '1']
    return g


class TestGraphOperations(unittest.TestCase):
    def test_count_edges(self):
        g = make_square_graph()
        self.assertEqual(g.countEdges(), 4)

    def test_select_edge_random_returns_incident_edge(self):
        random.seed(42)
        g = make_square_graph()
        for _ in range(20):
            v1, v2 = g.select_edge_random()
            self.assertIn(v1, g)
            self.assertIn(v2, g[v1])

    def test_merge_vertex(self):
        g = make_square_graph()
        g.merge_vertex('1', '2')
        self.assertNotIn('2', g)
        # '1' inherits '2's edges
        self.assertEqual(sorted(g['1']), ['1', '2', '3', '4'])

    def test_replace_vertex(self):
        g = make_square_graph()
        g.merge_vertex('1', '2')
        g.replace_vertex('1', '2')
        for vertex in g:
            self.assertNotIn('2', g[vertex])

    def test_remove_self_loops(self):
        g = make_square_graph()
        g.merge_vertex('1', '2')
        g.replace_vertex('1', '2')
        g.remove_self_loops('1')
        self.assertNotIn('1', g['1'])

    def test_min_cut_returns_edge_count(self):
        random.seed(0)
        g = make_square_graph()
        cut = g.min_cut()
        self.assertIsInstance(cut, int)
        self.assertEqual(len(g), 2)
        self.assertGreaterEqual(cut, 2)  # min cut of the 4-cycle is 2


class TestKargerEndToEnd(unittest.TestCase):
    def test_square_graph_min_cut(self):
        """Repeated trials on the 4-cycle must find the min cut of 2"""
        random.seed(42)
        results = []
        for _ in range(30):
            results.append(make_square_graph().min_cut())
        self.assertEqual(min(results), 2)

    def test_fixture_graph_min_cut(self):
        """Karger on a 6-vertex fixture must find the known min cut"""
        random.seed(42)
        input_file = os.path.join(DATA_DIR, 'input_random_1_6.txt')
        output_file = os.path.join(DATA_DIR, 'output_random_1_6.txt')
        with open(output_file) as f:
            expected = int(f.read().strip())

        results = []
        for _ in range(30):
            g = load_graph(input_file)
            results.append(g.min_cut())
        self.assertEqual(min(results), expected)


if __name__ == '__main__':
    unittest.main()
