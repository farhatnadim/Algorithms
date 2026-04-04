add_library(data_structures
    src/graph.cpp
    src/linked_list.cpp
    src/double_linked_list.cpp
    src/stack.cpp
    src/queue.cpp
    src/bfs.cpp
    src/dfs.cpp
)

target_include_directories(data_structures PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(data_structures_test tests/data_structures_test.cpp)
target_link_libraries(data_structures_test data_structures GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(data_structures_test)
