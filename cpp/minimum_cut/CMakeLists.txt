add_library(minimum_cut
    src/kargers_algorithm.cpp
)

target_include_directories(minimum_cut PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(minimum_cut_test tests/minimum_cut_test.cpp)
target_link_libraries(minimum_cut_test minimum_cut GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(minimum_cut_test)
