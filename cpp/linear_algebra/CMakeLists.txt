add_library(linear_algebra
    src/linear_algebra.cpp
)

target_include_directories(linear_algebra PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(linear_algebra_test tests/linear_algebra_test.cpp)
target_link_libraries(linear_algebra_test linear_algebra GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(linear_algebra_test)
