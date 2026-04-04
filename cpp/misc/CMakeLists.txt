add_library(misc
    src/count_inversions.cpp
)

target_include_directories(misc PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(misc_test tests/misc_test.cpp)
target_link_libraries(misc_test misc GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(misc_test)
