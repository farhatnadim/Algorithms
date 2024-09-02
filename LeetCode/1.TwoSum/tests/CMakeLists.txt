add_executable(twosum_test
  # Add your test files here
  twosum_test.cpp
)

target_link_libraries(twosum_test
  PRIVATE
  twosum
  gtest_main
)

include(GoogleTest)
gtest_discover_tests(twosum_test)