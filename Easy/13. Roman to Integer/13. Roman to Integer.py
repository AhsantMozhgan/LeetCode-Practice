# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        pattern = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50, 
            "C" : 100, 
            "D" : 500, 
            "M" : 1000
            }

        result = 0
        prev = 0

        for ch in s[::-1]:
            curr = pattern[ch]
            
            if curr >= prev:
                result += curr
            else:
                result -= curr

            prev = curr

        return result