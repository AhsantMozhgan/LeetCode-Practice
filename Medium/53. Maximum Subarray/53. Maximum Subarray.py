# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_current = max_global = nums[0]  # Initialize with the first element

        for i in range(1, len(nums)):
            # Choose the max between current element and the sum up to the current element.
            max_current = max(nums[i], max_current + nums[i])  
            
            if max_current > max_global:
                max_global = max_current  # Update the maximum found so far

        return max_global
