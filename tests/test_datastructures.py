import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'DataStructures'))

from Node import Node, DoubleNode, Vertex
from LinkedList import SimpleLinkedList, LinkedNumber
from DoubleLinkedList import DoubleLinkedList, LinkedNumber as DLinkedNumber
from Stack import Stack
from Queue import Queue


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node(5)
        self.assertEqual(node.get_item(), 5)
        self.assertIsNone(node.get_next())

    def test_node_with_next(self):
        node2 = Node(10)
        node1 = Node(5, node2)
        self.assertEqual(node1.get_next(), node2)

    def test_double_node(self):
        node = DoubleNode(5)
        self.assertEqual(node.get_item(), 5)
        self.assertIsNone(node.get_next())
        self.assertIsNone(node.get_previous())


class TestVertexEdgesIsolation(unittest.TestCase):
    """Tests to verify the mutable default argument bug is fixed."""

    def test_vertex_edges_isolation(self):
        """Two Vertex instances should NOT share the same edges list."""
        v1 = Vertex()
        v2 = Vertex()

        v1.add_edge(1)

        # If the bug exists, v2.edges would also contain 1
        self.assertEqual(v1.get_edges(), [1])
        self.assertEqual(v2.get_edges(), [])
        self.assertIsNot(v1.edges, v2.edges)

    def test_vertex_with_explicit_edges(self):
        """Verify vertex works correctly with explicit edges."""
        edges = [1, 2, 3]
        v = Vertex(edges=edges)
        self.assertEqual(v.get_edges(), [1, 2, 3])

    def test_multiple_vertices_independent(self):
        """Multiple vertices created should have independent edge lists."""
        vertices = [Vertex() for _ in range(5)]
        for i, v in enumerate(vertices):
            v.add_edge(i)

        for i, v in enumerate(vertices):
            self.assertEqual(v.get_edges(), [i])


class TestStack(unittest.TestCase):
    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_empty_pop(self):
        s = Stack()
        result = s.pop()
        self.assertIsNone(result)

    def test_insert_at_beginning_raises_notimplementederror(self):
        """Verify NotImplementedError is raised (not NotImplemented)."""
        s = Stack()
        with self.assertRaises(NotImplementedError):
            s.insert_at_beginning(1)

    def test_insert_raises_notimplementederror(self):
        s = Stack()
        with self.assertRaises(NotImplementedError):
            s.insert(0, 1)

    def test_delete_raises_notimplementederror(self):
        s = Stack()
        with self.assertRaises(NotImplementedError):
            s.delete(0)


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

    def test_empty_dequeue(self):
        q = Queue()
        result = q.dequeue()
        self.assertIsNone(result)

    def test_insert_at_beginning_raises_notimplementederror(self):
        """Verify NotImplementedError is raised (not NotImplemented)."""
        q = Queue()
        with self.assertRaises(NotImplementedError):
            q.insert_at_beginning(1)

    def test_insert_raises_notimplementederror(self):
        q = Queue()
        with self.assertRaises(NotImplementedError):
            q.insert(0, 1)

    def test_delete_raises_notimplementederror(self):
        q = Queue()
        with self.assertRaises(NotImplementedError):
            q.delete(0)

    def test_delete_from_end_raises_notimplementederror(self):
        q = Queue()
        with self.assertRaises(NotImplementedError):
            q.delete_from_end()


class TestSimpleLinkedList(unittest.TestCase):
    def test_insert_at_beginning(self):
        ll = SimpleLinkedList()
        ll.insertAtBeginning(1)
        ll.insertAtBeginning(2)
        ll.insertAtBeginning(3)
        self.assertEqual(ll.get_head().get_item(), 3)

    def test_insert_at_end(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        ll.insertAtEnd(3)
        self.assertEqual(ll.get_head().get_item(), 1)
        self.assertEqual(ll.get_tail().get_item(), 3)

    def test_delete_from_beginning(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        ll.deleteFromBeginning()
        self.assertEqual(ll.get_head().get_item(), 2)

    def test_delete_from_end(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        ll.deleteFromEnd()
        self.assertEqual(ll.get_tail().get_item(), 1)

    def test_search(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        ll.insertAtEnd(3)
        result = ll.search(2)
        self.assertIsNotNone(result)
        self.assertEqual(result.get_item(), 2)

    def test_search_not_found(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        result = ll.search(5)
        self.assertIsNone(result)


class TestDoubleLinkedList(unittest.TestCase):
    def test_insert_at_beginning(self):
        dll = DoubleLinkedList()
        dll.insert_at_beginning(1)
        dll.insert_at_beginning(2)
        dll.insert_at_beginning(3)
        self.assertEqual(dll.get_head().get_item(), 3)
        self.assertEqual(dll.get_tail().get_item(), 1)

    def test_add_at_end(self):
        dll = DoubleLinkedList()
        dll.add_at_end(1)
        dll.add_at_end(2)
        dll.add_at_end(3)
        self.assertEqual(dll.get_head().get_item(), 1)
        self.assertEqual(dll.get_tail().get_item(), 3)

    def test_to_array(self):
        dll = DoubleLinkedList()
        dll.add_at_end(1)
        dll.add_at_end(2)
        dll.add_at_end(3)
        arr = dll.to_array()
        self.assertEqual(arr, [1, 2, 3])

    def test_delete_from_beginning(self):
        dll = DoubleLinkedList()
        dll.add_at_end(1)
        dll.add_at_end(2)
        dll.add_at_end(3)
        item = dll.delete_from_beginning()
        self.assertEqual(item, 1)
        self.assertEqual(dll.get_head().get_item(), 2)

    def test_delete_from_end(self):
        dll = DoubleLinkedList()
        dll.add_at_end(1)
        dll.add_at_end(2)
        dll.add_at_end(3)
        item = dll.delete_from_end()
        self.assertEqual(item, 3)
        self.assertEqual(dll.get_tail().get_item(), 2)

    def test_search(self):
        dll = DoubleLinkedList()
        dll.add_at_end(1)
        dll.add_at_end(2)
        dll.add_at_end(3)
        result = dll.search(2)
        self.assertIsNotNone(result)
        self.assertEqual(result.get_item(), 2)


class TestLinkedNumberSort(unittest.TestCase):
    def test_insertion_sort(self):
        dll = DLinkedNumber()
        dll.add_at_end(5)
        dll.add_at_end(2)
        dll.add_at_end(8)
        dll.add_at_end(1)
        dll.add_at_end(9)
        dll.insertionSort()
        arr = dll.to_array()
        self.assertEqual(arr, [1, 2, 5, 8, 9])

    def test_minimum(self):
        dll = DLinkedNumber()
        dll.add_at_end(5)
        dll.add_at_end(2)
        dll.add_at_end(8)
        dll.add_at_end(1)
        dll.minimum()
        self.assertEqual(dll.getMin().get_item(), 1)

    def test_maximum(self):
        dll = DLinkedNumber()
        dll.add_at_end(5)
        dll.add_at_end(2)
        dll.add_at_end(8)
        dll.add_at_end(1)
        dll.maximum()
        self.assertEqual(dll.getMax().get_item(), 8)


if __name__ == '__main__':
    unittest.main()
