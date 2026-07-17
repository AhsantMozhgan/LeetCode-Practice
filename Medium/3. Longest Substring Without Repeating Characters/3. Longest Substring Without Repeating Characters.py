# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        length = 0

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            seen.add(s[j])

            length = max(length, j - i + 1)
            
        return length