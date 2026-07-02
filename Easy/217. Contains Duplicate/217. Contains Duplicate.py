# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = set()

        for num in nums:

            if num in table:
                return True

            table.add(num)
            
        return False