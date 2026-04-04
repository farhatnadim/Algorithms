-- Minimum cut algorithms
namespace Algorithms.MinimumCut

/-- Edge representation -/
structure Edge where
  from_ : Nat
  to : Nat
deriving Repr

/-- Karger's randomized minimum cut algorithm -/
def kargersMinCut (edges : List Edge) (numVertices : Nat) : Nat :=
  sorry -- TODO: User implements

end Algorithms.MinimumCut
