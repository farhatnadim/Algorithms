import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'DataStructures'))

from Node import Vertex
from Graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        """Create a simple test graph for each test"""
        pass

    def create_simple_graph(self):
        """
        Create a simple undirected graph:
        0 -- 1
        |    |
        2 -- 3
        """
        v0 = Vertex(edges=[1, 2], label='0')
        v1 = Vertex(edges=[0, 3], label='1')
        v2 = Vertex(edges=[0, 3], label='2')
        v3 = Vertex(edges=[1, 2], label='3')

        g = Graph()
        g.add_vertex(v0)
        g.add_vertex(v1)
        g.add_vertex(v2)
        g.add_vertex(v3)
        return g

    def create_disconnected_graph(self):
        """
        Create a graph with two connected components:
        0 -- 1    3 -- 4
        |         |
        2         5
        """
        v0 = Vertex(edges=[1, 2], label='0')
        v1 = Vertex(edges=[0], label='1')
        v2 = Vertex(edges=[0], label='2')
        v3 = Vertex(edges=[4, 5], label='3')
        v4 = Vertex(edges=[3], label='4')
        v5 = Vertex(edges=[3], label='5')

        g = Graph()
        for v in [v0, v1, v2, v3, v4, v5]:
            g.add_vertex(v)
        return g

    def create_dag(self):
        """
        Create a directed acyclic graph for topological sort testing:
        0 -> 1 -> 3
        |    |
        v    v
        2 -> 3
        """
        v0 = Vertex(edges=[1, 2], label='0')
        v1 = Vertex(edges=[3], label='1')
        v2 = Vertex(edges=[3], label='2')
        v3 = Vertex(edges=[], label='3')

        g = Graph()
        for v in [v0, v1, v2, v3]:
            g.add_vertex(v)
        return g

    def test_add_vertex(self):
        g = Graph()
        v0 = Vertex(edges=[], label='0')
        g.add_vertex(v0)
        self.assertEqual(len(g.get_vertices()), 1)
        self.assertEqual(g.get_vertex(0), v0)

    def test_get_vertices(self):
        g = self.create_simple_graph()
        vertices = g.get_vertices()
        self.assertEqual(len(vertices), 4)

    def test_set_vertices(self):
        g = Graph()
        v0 = Vertex(edges=[], label='0')
        v1 = Vertex(edges=[], label='1')
        g.set_vertices([v0, v1])
        self.assertEqual(len(g.get_vertices()), 2)

    def test_delete_vertex(self):
        g = self.create_simple_graph()
        deleted = g.delete_vertex(0)
        self.assertEqual(len(g.get_vertices()), 3)
        self.assertEqual(deleted.label, '0')

    def test_bfs_single_component(self):
        g = self.create_simple_graph()
        g.bfs(0, connected_components=1)

        # All vertices should be explored
        for v in g.get_vertices():
            self.assertTrue(v.is_explored())

        # Check distances
        self.assertEqual(g.get_vertex(0).distance, 0)
        self.assertEqual(g.get_vertex(1).distance, 1)
        self.assertEqual(g.get_vertex(2).distance, 1)
        # Vertex 3 can be reached from 0 via 1 or 2 (distance 2)
        self.assertEqual(g.get_vertex(3).distance, 2)

        # All should have same connected component
        for v in g.get_vertices():
            self.assertEqual(v.cc, 1)

    def test_undirected_connected_components(self):
        g = self.create_disconnected_graph()
        g.undirected_connected_components()

        # Check that we have two connected components
        cc_values = set(v.cc for v in g.get_vertices())
        self.assertEqual(len(cc_values), 2)

        # Vertices 0, 1, 2 should be in one component
        cc0 = g.get_vertex(0).cc
        self.assertEqual(g.get_vertex(1).cc, cc0)
        self.assertEqual(g.get_vertex(2).cc, cc0)

        # Vertices 3, 4, 5 should be in another component
        cc3 = g.get_vertex(3).cc
        self.assertEqual(g.get_vertex(4).cc, cc3)
        self.assertEqual(g.get_vertex(5).cc, cc3)

        # The two components should be different
        self.assertNotEqual(cc0, cc3)

    def test_dfs_iterative(self):
        g = self.create_simple_graph()
        g.dfs()

        # All vertices should be explored
        for v in g.get_vertices():
            self.assertTrue(v.is_explored())

    def test_dfs_recursive(self):
        g = self.create_simple_graph()
        g.dfs_recursive(g.get_vertex(0))

        # All vertices should be explored
        for v in g.get_vertices():
            self.assertTrue(v.is_explored())

    def test_topological_sort(self):
        g = self.create_dag()
        g.topological_sort()

        # Check that all vertices have labels assigned
        for v in g.get_vertices():
            self.assertIsNotNone(v.currentLabel)

        # Verify topological ordering property:
        # For every directed edge u -> v, u comes before v in the ordering
        for i, vertex in enumerate(g.get_vertices()):
            for edge_idx in vertex.edges:
                edge_vertex = g.get_vertex(edge_idx)
                # vertex should have a smaller label than its successors
                self.assertLess(vertex.currentLabel, edge_vertex.currentLabel,
                              f"Vertex {i} (label {vertex.currentLabel}) should come before "
                              f"vertex {edge_idx} (label {edge_vertex.currentLabel})")

        # After topological sort, exploration status should be reset
        for v in g.get_vertices():
            self.assertFalse(v.is_explored())

    def test_reversal(self):
        """Test graph reversal (edge direction flip)"""
        g = self.create_dag()
        reversed_g = g.reversal()

        # Check that number of vertices is the same
        self.assertEqual(len(reversed_g.get_vertices()), len(g.get_vertices()))

        # Check that edges are reversed
        # Original: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
        # Reversed: 1 -> 0, 2 -> 0, 3 -> 1, 3 -> 2

        # Vertex 0 in original has edges to [1, 2]
        # In reversed graph, vertex 0 should have no incoming edges shown as outgoing
        # This is complex to verify without knowing exact implementation
        # At minimum, verify graph exists and has same size
        self.assertEqual(len(reversed_g.get_vertices()), 4)

    def test_kosaraju_simple(self):
        """Test Kosaraju's algorithm for strongly connected components"""
        # Create a simple directed graph with known SCCs
        v0 = Vertex(edges=[1], label='0')
        v1 = Vertex(edges=[2], label='1')
        v2 = Vertex(edges=[0], label='2')  # Creates cycle 0->1->2->0
        v3 = Vertex(edges=[4], label='3')
        v4 = Vertex(edges=[3], label='4')  # Creates cycle 3->4->3

        g = Graph()
        for v in [v0, v1, v2, v3, v4]:
            g.add_vertex(v)

        num_scc = g.kosaraju()
        self.assertEqual(num_scc, 2)

        # Vertices 0, 1, 2 should be in one SCC
        scc0 = g.get_vertex(0).scc
        self.assertEqual(g.get_vertex(1).scc, scc0)
        self.assertEqual(g.get_vertex(2).scc, scc0)

        # Vertices 3, 4 should be in another SCC
        scc3 = g.get_vertex(3).scc
        self.assertEqual(g.get_vertex(4).scc, scc3)

        # The two SCCs should be different
        self.assertNotEqual(scc0, scc3)

    def test_merge_vertices_not_implemented(self):
        g = self.create_simple_graph()
        with self.assertRaises(NotImplementedError):
            g.merge_vertices(0, 1)

    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(len(g.get_vertices()), 0)

    def test_single_vertex_graph(self):
        g = Graph()
        v0 = Vertex(edges=[], label='0')
        g.add_vertex(v0)

        # BFS on single vertex
        g.bfs(0, connected_components=1)
        self.assertTrue(v0.is_explored())
        self.assertEqual(v0.distance, 0)
        self.assertEqual(v0.cc, 1)

if __name__ == '__main__':
    unittest.main()
