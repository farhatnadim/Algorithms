# portpal parity runner (JSON/dispatch glue only — see CLAUDE.md carve-out)

FetchContent_Declare(
  nlohmann_json
  URL https://github.com/nlohmann/json/releases/download/v3.11.3/json.tar.xz
)
FetchContent_MakeAvailable(nlohmann_json)

add_executable(parity_runner parity_runner.cpp registry.cpp)
target_link_libraries(parity_runner PRIVATE nlohmann_json::nlohmann_json)

# All module include dirs, so registry entries compile as soon as they are
# uncommented after the user implements an algorithm.
target_include_directories(parity_runner PRIVATE
  ${CMAKE_SOURCE_DIR}/sort/include
  ${CMAKE_SOURCE_DIR}/search/include
  ${CMAKE_SOURCE_DIR}/select/include
  ${CMAKE_SOURCE_DIR}/data_structures/include
  ${CMAKE_SOURCE_DIR}/linear_algebra/include
  ${CMAKE_SOURCE_DIR}/integer_multiplication/include
  ${CMAKE_SOURCE_DIR}/minimum_cut/include
  ${CMAKE_SOURCE_DIR}/misc/include
)
