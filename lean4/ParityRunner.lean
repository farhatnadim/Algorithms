/- portpal parity runner (Lean 4): reads a fixture JSON, runs every case
   through the user-written `Algorithms` library, prints one JSON array of
   `{"name", "output"|"error"}` entries to stdout.

   JSON/dispatch glue only — no algorithm logic (see CLAUDE.md carve-out).

   Note: a `def` whose body is still `sorry` compiles but PANICS when
   evaluated, which is why portpal only invokes this runner for algorithms
   its progress scanner marks as implemented. -/
import Lean.Data.Json
import Algorithms

open Lean (Json ToJson FromJson toJson fromJson?)

private def getField (input : Json) (key : String) : Except String Json :=
  input.getObjVal? key

private def decodeField (α : Type) [FromJson α] (input : Json) (key : String) :
    Except String α := do
  fromJson? (← getField input key)

private def natOfDecimal (input : Json) (key : String) : Except String Nat := do
  let s : String ← decodeField String input key
  match s.toNat? with
  | some n => pure n
  | none => throw s!"input field {key} is not a decimal Nat: {s}"

def dispatch (algo : String) (input : Json) : Except String Json := do
  match algo with
  | "insertion_sort" => do
      let a : List Int ← decodeField _ input "array"
      pure (toJson (Algorithms.Sort.insertionSort a))
  | "bubble_sort" => do
      let a : List Int ← decodeField _ input "array"
      pure (toJson (Algorithms.Sort.bubbleSort a))
  | "merge_sort" => do
      let a : List Int ← decodeField _ input "array"
      pure (toJson (Algorithms.Sort.mergeSort a))
  | "quick_sort" => do
      let a : List Int ← decodeField _ input "array"
      pure (toJson (Algorithms.Sort.quickSort a))
  | "r_select" => do
      let a : List Int ← decodeField _ input "array"
      let ith : Nat ← decodeField _ input "ith"
      pure (toJson (Algorithms.Select.rSelect a ith))
  | "d_select" => do
      let a : List Int ← decodeField _ input "array"
      let ith : Nat ← decodeField _ input "ith"
      pure (toJson (Algorithms.Select.dSelect a ith))
  | "binary_search" => do
      let a : Array Int ← decodeField _ input "array"
      let target : Int ← decodeField _ input "target"
      pure (toJson (Algorithms.Search.binarySearch a target))
  | "second_largest" => do
      let a : List Int ← decodeField _ input "array"
      pure (toJson (Algorithms.Search.secondLargest a))
  | "count_inversions" => do
      let a : List Int ← decodeField _ input "array"
      pure (toJson (Algorithms.Misc.countInversions a))
  | "standard_multiply" => do
      let x ← natOfDecimal input "x"
      let y ← natOfDecimal input "y"
      pure (toJson (toString (Algorithms.IntegerMultiplication.standardMultiply x y)))
  | "karatsuba_multiply" => do
      let x ← natOfDecimal input "x"
      let y ← natOfDecimal input "y"
      pure (toJson (toString (Algorithms.IntegerMultiplication.karatsubaMultiply x y)))
  | "vec_dot" => do
      let a : List Int ← decodeField _ input "a"
      let b : List Int ← decodeField _ input "b"
      pure (toJson (Algorithms.LinearAlgebra.vecDot a b))
  | "mat_mul" => do
      let a : List (List Int) ← decodeField _ input "a"
      let b : List (List Int) ← decodeField _ input "b"
      pure (toJson (Algorithms.LinearAlgebra.matMul a b))
  | "rec_mat_mul" => do
      let a : List (List Int) ← decodeField _ input "a"
      let b : List (List Int) ← decodeField _ input "b"
      pure (toJson (Algorithms.LinearAlgebra.recMatMul a b))
  | "strassen" => do
      let a : List (List Int) ← decodeField _ input "a"
      let b : List (List Int) ← decodeField _ input "b"
      pure (toJson (Algorithms.LinearAlgebra.strassen a b))
  | "modified_gram_schmidt" => do
      let a : List (List Float) ← decodeField _ input "a"
      match Algorithms.LinearAlgebra.modifiedGramSchmidt a with
      | some (q, r) => pure (Json.mkObj [("q", toJson q), ("r", toJson r)])
      | none => pure Json.null
  | other => throw s!"unknown algorithm: {other}"

def runCase (algo : String) (case_ : Json) : Json :=
  let name := (case_.getObjVal? "name").toOption.getD (Json.str "?")
  match case_.getObjVal? "input" with
  | .error e => Json.mkObj [("name", name), ("error", Json.str e)]
  | .ok input =>
    match dispatch algo input with
    | .ok output => Json.mkObj [("name", name), ("output", output)]
    | .error e => Json.mkObj [("name", name), ("error", Json.str e)]

def main (args : List String) : IO UInt32 := do
  match args with
  | [path] =>
    let text ← IO.FS.readFile path
    match Json.parse text with
    | .error e =>
      IO.eprintln s!"invalid fixture JSON: {e}"
      pure 2
    | .ok fixture =>
      let algo := ((fixture.getObjVal? "algorithm").bind Json.getStr?).toOption.getD ""
      let cases := ((fixture.getObjVal? "cases").bind Json.getArr?).toOption.getD #[]
      IO.println (Json.arr (cases.map (runCase algo))).compress
      pure 0
  | _ =>
    IO.eprintln "usage: parity_runner <fixture.json>"
    pure 2
