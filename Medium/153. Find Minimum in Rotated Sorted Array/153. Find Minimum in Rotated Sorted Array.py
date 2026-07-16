# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:          # use <, not <=
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost,
            # the minimum is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half (including mid).
                right = mid
                
        return nums[left]   # or nums[right] – both are the minimum