#include "twosum.h"


 std::vector<int> twoSum(std::vector<int>& nums, int target)
{
    std::vector<int> result; 
    for (auto it_out = nums.begin(); it_out < nums.end(); it_out++)
    {
        for (auto it_in = it_out + 1; it_in < nums.end(); it_in++)
        {
            if (*it_out + *it_in == target)
            {
                result.push_back(std::distance(nums.begin(),it_out));
                result.push_back(std::distance(nums.begin(),it_in));
                return result;
            }
        }
    }
    return result;  
}    
