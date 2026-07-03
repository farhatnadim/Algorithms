// portpal parity runner: shared registry declaration.
// JSON/dispatch glue only — no algorithm logic (see CLAUDE.md carve-out).
#ifndef ALGORITHMS_PARITY_RUNNER_HPP
#define ALGORITHMS_PARITY_RUNNER_HPP

#include <functional>
#include <map>
#include <string>

#include <nlohmann/json.hpp>

namespace parity {

using Handler = std::function<nlohmann::json(const nlohmann::json& input)>;

// algorithm name (snake_case, as in the fixture files) -> handler
std::map<std::string, Handler>& registry();

// Defined in registry.cpp. Uncomment entries there as you implement
// the corresponding algorithm.
void registerAlgorithms();

}  // namespace parity

#endif  // ALGORITHMS_PARITY_RUNNER_HPP
