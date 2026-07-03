add_library(select
    src/select.cpp
)

target_include_directories(select PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(select_test tests/select_test.cpp)
target_link_libraries(select_test select GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(select_test)
