add_library(sort
    src/insertion_sort.cpp
    src/bubble_sort.cpp
    src/merge_sort.cpp
    src/quick_sort.cpp
)

target_include_directories(sort PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Tests
add_executable(sort_test tests/sort_test.cpp)
target_link_libraries(sort_test sort GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(sort_test)
