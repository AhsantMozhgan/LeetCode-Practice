# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        noRepeat = set()
        pattern = dict()

        for index, ch in enumerate(s):
            if ch in pattern:
                if t[index] != pattern[ch]:
                    return False
                
            else:
                if t[index] in noRepeat:
                    return False
                pattern[ch] = t[index]
                noRepeat.add(t[index])
        return True