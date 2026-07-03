// portpal parity runner (C++): reads a fixture JSON, runs every case through
// the registered user-written algorithms, prints one JSON array of
// {"name", "output"|"error"} entries to stdout.
//
// JSON/dispatch glue only — no algorithm logic (see CLAUDE.md carve-out).

#include <fstream>
#include <iostream>
#include <string>

#include <nlohmann/json.hpp>

#include "parity_runner.hpp"

namespace parity {

std::map<std::string, Handler>& registry() {
  static std::map<std::string, Handler> instance;
  return instance;
}

}  // namespace parity

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "usage: parity_runner <fixture.json>\n";
    return 2;
  }
  std::ifstream file(argv[1]);
  if (!file) {
    std::cerr << "cannot read " << argv[1] << "\n";
    return 2;
  }

  nlohmann::json fixture;
  try {
    file >> fixture;
  } catch (const nlohmann::json::exception& e) {
    std::cerr << "invalid fixture JSON: " << e.what() << "\n";
    return 2;
  }

  parity::registerAlgorithms();
  const std::string algorithm = fixture.value("algorithm", "");
  const auto& reg = parity::registry();
  const auto handler = reg.find(algorithm);

  nlohmann::json results = nlohmann::json::array();
  for (const auto& kase : fixture.value("cases", nlohmann::json::array())) {
    nlohmann::json entry;
    entry["name"] = kase.value("name", "?");
    if (handler == reg.end()) {
      entry["error"] = "unregistered: " + algorithm +
                       " (implement it, then uncomment its entry in cpp/parity/registry.cpp)";
    } else {
      try {
        entry["output"] = handler->second(kase.at("input"));
      } catch (const std::exception& e) {
        entry["error"] = std::string(e.what());
      }
    }
    results.push_back(entry);
  }
  std::cout << results.dump() << "\n";
  return 0;
}
