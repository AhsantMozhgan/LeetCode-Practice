# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case: 0 and 1 are their own square roots
        if x < 2:
            return x
        
        # Start with an initial guess.
        # Using 'x' itself works, but we can start with x // 2 for slight optimization.
        guess = x
        
        # Newton's formula: guess = (guess + x / guess) / 2
        # We keep refining until guess^2 <= x (the floor sqrt).
        while guess * guess > x:
            # Integer division is used here to keep the result as an integer
            # and automatically floor the value at each step.
            guess = (guess + x // guess) // 2
            
        return guess


        # if x < 2:
        #     return x
        
        # low, high = 0, x
        
        # while low <= high:
        #     mid = (low + high) // 2
        #     square = mid * mid
            
        #     if square == x:
        #         return mid
        #     elif square < x:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
                
        # return high



