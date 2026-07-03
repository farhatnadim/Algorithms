-- Selection algorithms (ith order statistic)
namespace Algorithms.Select

/-- Randomized selection (quickselect): the ith order statistic (0-indexed).
    Reference: Select/Python/RSelect.py -/
def rSelect (arr : List α) (ith : Nat) [Ord α] : Option α :=
  sorry -- TODO: User implements

/-- Deterministic selection (median-of-medians): the ith order statistic
    (0-indexed). Uses the upper median for even-sized groups.
    Reference: Select/Python/DSelect.py -/
def dSelect (arr : List α) (ith : Nat) [Ord α] : Option α :=
  sorry -- TODO: User implements

end Algorithms.Select
