#include <gtest/gtest.h>
#include "twosum.h"

/* I need to test the twoSum function */

TEST(TwoSumTest, BasicTest) {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> expected = {0, 1};
    EXPECT_EQ(twoSum(nums, target), expected);
}
/* more edge cases */
TEST(TwoSumTest, EdgeCases) {
    std::vector<int> nums = {3, 2, 4};
    int target = 6;
    std::vector<int> expected = {1, 2};
    EXPECT_EQ(twoSum(nums, target), expected);
}
