# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        table = dict()

        for index, num in enumerate(nums):

            if num in table:
                if index - table[num] <= k:
                    return True

            table[num] = index

        return False