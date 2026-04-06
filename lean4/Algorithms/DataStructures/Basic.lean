-- Data structures
namespace Algorithms.DataStructures

/-- Graph using adjacency list representation -/
structure Graph where
  adjacencyList : List (Nat × List Nat)
deriving Repr

namespace Graph
  /-- Create an empty graph -/
  def empty : Graph :=
    { adjacencyList := [] }

  /-- Add a vertex to the graph -/
  def addVertex (g : Graph) (v : Nat) : Graph :=
    sorry -- TODO: User implements

  /-- Add an edge to the graph -/
  def addEdge (g : Graph) (from_ to : Nat) : Graph :=
    sorry -- TODO: User implements

  /-- Get neighbors of a vertex -/
  def neighbors (g : Graph) (v : Nat) : List Nat :=
    sorry -- TODO: User implements
end Graph

/-- Singly linked list -/
inductive LinkedList (α : Type)
  | nil : LinkedList α
  | cons : α → LinkedList α → LinkedList α
deriving Repr

namespace LinkedList
  def pushFront (l : LinkedList α) (x : α) : LinkedList α :=
    sorry -- TODO: User implements

  def popFront (l : LinkedList α) : Option (α × LinkedList α) :=
    sorry -- TODO: User implements
end LinkedList

/-- Stack data structure -/
structure Stack (α : Type) where
  data : List α
deriving Repr

namespace Stack
  def empty : Stack α :=
    { data := [] }

  def push (s : Stack α) (x : α) : Stack α :=
    sorry -- TODO: User implements

  def pop (s : Stack α) : Option (α × Stack α) :=
    sorry -- TODO: User implements

  def peek (s : Stack α) : Option α :=
    sorry -- TODO: User implements
end Stack

/-- Queue data structure -/
structure Queue (α : Type) where
  data : List α
deriving Repr

namespace Queue
  def empty : Queue α :=
    { data := [] }

  def enqueue (q : Queue α) (x : α) : Queue α :=
    sorry -- TODO: User implements

  def dequeue (q : Queue α) : Option (α × Queue α) :=
    sorry -- TODO: User implements

  def front (q : Queue α) : Option α :=
    sorry -- TODO: User implements
end Queue

end Algorithms.DataStructures
