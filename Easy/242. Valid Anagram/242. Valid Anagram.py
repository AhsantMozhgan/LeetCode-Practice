# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        counterS = defaultdict(int)
        counterT = defaultdict(int)

        for index in range(len(s)):
            counterS[s[index]] += 1
            counterT[t[index]] += 1

        return counterS == counterT