import unittest
from python.data_structures.node import Node, DoubleNode, Vertex
from python.data_structures.linked_list import SimpleLinkedList, LinkedNumber
from python.data_structures.double_linked_list import DoubleLinkedList, LinkedNumber as DLinkedNumber
from python.data_structures.stack import Stack
from python.data_structures.queue import Queue


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

    def test_insert_at_position(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(3)
        ll.insert(1, 2)  # Insert 2 at position 1
        # List should be 1 -> 2 -> 3
        self.assertEqual(ll.get_head().get_item(), 1)
        self.assertEqual(ll.get_head().get_next().get_item(), 2)

    def test_insert_at_position_zero(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(2)
        ll.insert(0, 1)  # Insert at beginning
        self.assertEqual(ll.get_head().get_item(), 1)

    def test_delete_at_position(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        ll.insertAtEnd(3)
        ll.delete(1)  # Delete position 1 (value 2)
        # List should be 1 -> 3
        self.assertEqual(ll.get_head().get_item(), 1)
        self.assertEqual(ll.get_head().get_next().get_item(), 3)

    def test_delete_at_position_zero(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        ll.insertAtEnd(2)
        ll.delete(0)  # Delete first element
        self.assertEqual(ll.get_head().get_item(), 2)

    def test_delete_from_empty_list(self):
        ll = SimpleLinkedList()
        result = ll.deleteFromBeginning()
        self.assertIsNone(result)

    def test_traverse_list(self):
        ll = SimpleLinkedList()
        ll.insertAtBeginning(1)
        ll.insertAtBeginning(2)
        ll.insertAtBeginning(3)
        ll.traverseList()
        # After traversal, tail should be set correctly
        self.assertEqual(ll.get_tail().get_item(), 1)

    def test_insert_at_end_empty_list(self):
        ll = SimpleLinkedList()
        ll.insertAtEnd(1)
        self.assertEqual(ll.get_head().get_item(), 1)
        self.assertEqual(ll.get_tail().get_item(), 1)


class TestLinkedNumber(unittest.TestCase):
    def test_minimum(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        ll.insertAtEnd(2)
        ll.insertAtEnd(8)
        ll.insertAtEnd(1)
        ll.minimum()
        self.assertEqual(ll.getMin().get_item(), 1)

    def test_maximum(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        ll.insertAtEnd(2)
        ll.insertAtEnd(8)
        ll.insertAtEnd(1)
        ll.maximum()
        self.assertEqual(ll.getMax().get_item(), 8)

    def test_successor(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        ll.insertAtEnd(2)
        ll.insertAtEnd(8)
        ll.insertAtEnd(1)
        successor = ll.successor()
        # Maximum is 8, successor (second largest) should be 5
        self.assertIsNotNone(successor)
        self.assertEqual(successor.get_item(), 5)

    def test_predecessor(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        ll.insertAtEnd(2)
        ll.insertAtEnd(8)
        ll.insertAtEnd(1)
        predecessor = ll.predecessor()
        # Minimum is 1, predecessor (second smallest) should be 2
        self.assertIsNotNone(predecessor)
        self.assertEqual(predecessor.get_item(), 2)

    def test_minimum_single_element(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        result = ll.minimum()
        # For single element, minimum() returns the node directly
        if result is not None:
            self.assertEqual(result.get_item(), 5)

    def test_maximum_single_element(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        result = ll.maximum()
        # For single element, maximum() returns the node directly
        if result is not None:
            self.assertEqual(result.get_item(), 5)

    def test_successor_single_element(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        result = ll.successor()
        self.assertIsNone(result)

    def test_predecessor_single_element(self):
        ll = LinkedNumber()
        ll.insertAtEnd(5)
        result = ll.predecessor()
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


class TestRegressionFixes(unittest.TestCase):
    """Guards for bugs fixed while preparing the code for Lean 4 / C++ ports."""

    def test_double_linked_list_search_on_empty_list(self):
        """search on an empty list must return None, not crash"""
        dll = DoubleLinkedList()
        self.assertIsNone(dll.search(42))

    def test_double_linked_list_insert_at_zero_size(self):
        """insert(pos=0, ...) must increment size exactly once"""
        dll = DoubleLinkedList()
        dll.add_at_end(1)
        dll.add_at_end(2)
        dll.insert(0, 99)
        self.assertEqual(dll.get_size(), 3)
        self.assertEqual(dll.to_array(), [99, 1, 2])

    def test_simple_linked_list_delete_from_end_clears_tail(self):
        """emptying the list via deleteFromEnd must also clear the tail"""
        sll = SimpleLinkedList()
        sll.insertAtBeginning(1)
        sll.deleteFromEnd()
        self.assertIsNone(sll.get_head())
        self.assertIsNone(sll.get_tail())

    def test_stack_is_empty_has_no_side_effects(self):
        """is_empty must not print anything"""
        import io
        import contextlib
        s = Stack()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertTrue(s.is_empty())
            s.push(1)
            self.assertFalse(s.is_empty())
        self.assertEqual(buf.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
