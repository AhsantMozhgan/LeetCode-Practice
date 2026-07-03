# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counterR = Counter(ransomNote)
        counterM = Counter(magazine)

        for key, val in counterR.items():
            if key not in counterM or val > counterM[key]:
                return False
        
        return True