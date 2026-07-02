# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = dict()

        for index, num in enumerate(nums):          

            if num in value_to_index:
                return [value_to_index[num], index]
            
            value_to_index[target - num] =  index