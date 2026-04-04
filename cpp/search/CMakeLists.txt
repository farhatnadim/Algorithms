add_library(search
    src/binary_search.cpp
    src/second_largest.cpp
    src/closest_pair.cpp
    src/three_sum.cpp
)

target_include_directories(search PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(search_test tests/search_test.cpp)
target_link_libraries(search_test search GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(search_test)
