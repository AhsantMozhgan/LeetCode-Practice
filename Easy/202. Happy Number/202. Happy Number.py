# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        noRepeat = set()

        while n != 1:
            noRepeat.add(n)

            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit ** 2
                n = n // 10

            if sum in noRepeat:
                return False
                
            n = sum

        return True 