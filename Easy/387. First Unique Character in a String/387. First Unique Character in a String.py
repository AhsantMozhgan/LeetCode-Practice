# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict()

        for ch in s:
            if ch in counter:
                counter[ch] = counter[ch] + 1
            else:
                counter[ch] = 1
        
        for index, ch in enumerate(s):
            if counter[ch] == 1:
                return index

        return -1 