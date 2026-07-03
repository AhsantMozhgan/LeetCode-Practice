# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        halfLen = floor(len(nums) / 2)

        count = Counter(nums)
        
        for key, val in count.items():
            if val > halfLen:
                return key