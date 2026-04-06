use std::collections::HashMap;

/// Graph data structure using adjacency list
/// TODO: User implements
pub struct Graph {
    #[allow(dead_code)]
    adjacency_list: HashMap<i32, Vec<(i32, f64)>>,
}

impl Graph {
    pub fn new() -> Self {
        Graph {
            adjacency_list: HashMap::new(),
        }
    }

    pub fn add_vertex(&mut self, _vertex: i32) {
        // TODO: User implements
    }

    pub fn add_edge(&mut self, _from: i32, _to: i32, _weight: f64) {
        // TODO: User implements
    }

    pub fn neighbors(&self, _vertex: i32) -> Vec<i32> {
        Vec::new() // TODO: User implements
    }
}

impl Default for Graph {
    fn default() -> Self {
        Self::new()
    }
}

/// Singly linked list
/// TODO: User implements
pub struct LinkedList<T> {
    _marker: std::marker::PhantomData<T>,
}

impl<T> LinkedList<T> {
    pub fn new() -> Self {
        LinkedList {
            _marker: std::marker::PhantomData,
        }
    }

    pub fn push_front(&mut self, _value: T) {
        // TODO: User implements
    }

    pub fn push_back(&mut self, _value: T) {
        // TODO: User implements
    }

    pub fn pop_front(&mut self) -> Option<T> {
        None // TODO: User implements
    }

    pub fn pop_back(&mut self) -> Option<T> {
        None // TODO: User implements
    }

    pub fn len(&self) -> usize {
        0 // TODO: User implements
    }

    pub fn is_empty(&self) -> bool {
        true // TODO: User implements
    }
}

impl<T> Default for LinkedList<T> {
    fn default() -> Self {
        Self::new()
    }
}

/// Doubly linked list
/// TODO: User implements
pub struct DoubleLinkedList<T> {
    _marker: std::marker::PhantomData<T>,
}

impl<T> DoubleLinkedList<T> {
    pub fn new() -> Self {
        DoubleLinkedList {
            _marker: std::marker::PhantomData,
        }
    }

    pub fn push_front(&mut self, _value: T) {
        // TODO: User implements
    }

    pub fn push_back(&mut self, _value: T) {
        // TODO: User implements
    }

    pub fn pop_front(&mut self) -> Option<T> {
        None // TODO: User implements
    }

    pub fn pop_back(&mut self) -> Option<T> {
        None // TODO: User implements
    }

    pub fn len(&self) -> usize {
        0 // TODO: User implements
    }

    pub fn is_empty(&self) -> bool {
        true // TODO: User implements
    }
}

impl<T> Default for DoubleLinkedList<T> {
    fn default() -> Self {
        Self::new()
    }
}

/// Stack data structure
/// TODO: User implements
pub struct Stack<T> {
    _marker: std::marker::PhantomData<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Self {
        Stack {
            _marker: std::marker::PhantomData,
        }
    }

    pub fn push(&mut self, _value: T) {
        // TODO: User implements
    }

    pub fn pop(&mut self) -> Option<T> {
        None // TODO: User implements
    }

    pub fn peek(&self) -> Option<&T> {
        None // TODO: User implements
    }

    pub fn len(&self) -> usize {
        0 // TODO: User implements
    }

    pub fn is_empty(&self) -> bool {
        true // TODO: User implements
    }
}

impl<T> Default for Stack<T> {
    fn default() -> Self {
        Self::new()
    }
}

/// Queue data structure
/// TODO: User implements
pub struct Queue<T> {
    _marker: std::marker::PhantomData<T>,
}

impl<T> Queue<T> {
    pub fn new() -> Self {
        Queue {
            _marker: std::marker::PhantomData,
        }
    }

    pub fn enqueue(&mut self, _value: T) {
        // TODO: User implements
    }

    pub fn dequeue(&mut self) -> Option<T> {
        None // TODO: User implements
    }

    pub fn front(&self) -> Option<&T> {
        None // TODO: User implements
    }

    pub fn len(&self) -> usize {
        0 // TODO: User implements
    }

    pub fn is_empty(&self) -> bool {
        true // TODO: User implements
    }
}

impl<T> Default for Queue<T> {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn graph_placeholder() {
        let _g = Graph::new();
        assert!(true);
    }

    #[test]
    fn linked_list_placeholder() {
        let _ll: LinkedList<i32> = LinkedList::new();
        assert!(true);
    }

    #[test]
    fn double_linked_list_placeholder() {
        let _dll: DoubleLinkedList<i32> = DoubleLinkedList::new();
        assert!(true);
    }

    #[test]
    fn stack_placeholder() {
        let _s: Stack<i32> = Stack::new();
        assert!(true);
    }

    #[test]
    fn queue_placeholder() {
        let _q: Queue<i32> = Queue::new();
        assert!(true);
    }
}
