// portpal parity runner: algorithm registry.
//
// The C++ stubs are template DECLARATIONS without definitions, so referencing
// an unimplemented algorithm here would fail to link. Therefore every entry
// ships commented out: implement the algorithm (usually in the module's
// header, since these are templates), then uncomment its include + entry.
//
// JSON/dispatch glue only — no algorithm logic (see CLAUDE.md carve-out).

#include <vector>

#include <nlohmann/json.hpp>

#include "parity_runner.hpp"

// Uncomment as you implement:
// #include "insertion_sort.hpp"
// #include "bubble_sort.hpp"
// #include "merge_sort.hpp"
// #include "quick_sort.hpp"
// #include "select.hpp"
// #include "search.hpp"

namespace parity {

void registerAlgorithms() {
  auto& reg = registry();
  (void)reg;  // silences unused warning while all entries are commented out

  // ── sort (in-place on std::vector<long long>) ──────────────────────────
  // reg["merge_sort"] = [](const nlohmann::json& input) {
  //   auto arr = input.at("array").get<std::vector<long long>>();
  //   algorithms::mergeSort(arr);
  //   return nlohmann::json(arr);
  // };
  // reg["insertion_sort"] / ["bubble_sort"] / ["quick_sort"]: same shape,
  // calling algorithms::insertionSort / bubbleSort / quickSort.

  // ── select (returns the ith order statistic) ───────────────────────────
  // reg["r_select"] = [](const nlohmann::json& input) {
  //   auto arr = input.at("array").get<std::vector<long long>>();
  //   auto ith = input.at("ith").get<std::size_t>();
  //   auto result = algorithms::rSelect(arr, ith);   // std::optional<long long>
  //   return result ? nlohmann::json(*result) : nlohmann::json(nullptr);
  // };
  // reg["d_select"]: same shape with algorithms::dSelect.

  // ── search ─────────────────────────────────────────────────────────────
  // reg["binary_search"] = [](const nlohmann::json& input) {
  //   auto arr = input.at("array").get<std::vector<long long>>();
  //   auto target = input.at("target").get<long long>();
  //   auto idx = algorithms::binarySearch(arr, target);  // std::optional<std::size_t>
  //   return idx ? nlohmann::json(*idx) : nlohmann::json(nullptr);
  // };
  // reg["second_largest"]: decode "array", call algorithms::secondLargest,
  // map std::optional<long long> to value-or-null as above.

  // ── misc ───────────────────────────────────────────────────────────────
  // reg["count_inversions"] = [](const nlohmann::json& input) {
  //   auto arr = input.at("array").get<std::vector<long long>>();
  //   return nlohmann::json(algorithms::countInversions(arr));
  // };

  // ── integer multiplication (decimal-string big ints) ───────────────────
  // reg["standard_multiply"] = [](const nlohmann::json& input) {
  //   return nlohmann::json(algorithms::standardMultiply(
  //       input.at("x").get<std::string>(), input.at("y").get<std::string>()));
  // };
  // reg["karatsuba_multiply"]: same shape with algorithms::karatsubaMultiply.

  // ── linear algebra (Matrix = std::vector<std::vector<T>>) ──────────────
  // reg["vec_dot"] / ["mat_mul"] / ["rec_mat_mul"] / ["strassen"]:
  //   decode "a"/"b" as std::vector<std::vector<long long>> (or vectors for
  //   vec_dot), call the algorithm, map std::optional to value-or-null.
  // reg["modified_gram_schmidt"]:
  //   decode "a" as std::vector<std::vector<double>>; on success return
  //   nlohmann::json{{"q", q}, {"r", r}}, else null.
}

}  // namespace parity
