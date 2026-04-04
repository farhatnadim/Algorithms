add_library(integer_multiplication
    src/standard_multiplication.cpp
    src/karatsuba.cpp
)

target_include_directories(integer_multiplication PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(integer_multiplication_test tests/integer_multiplication_test.cpp)
target_link_libraries(integer_multiplication_test integer_multiplication GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(integer_multiplication_test)
