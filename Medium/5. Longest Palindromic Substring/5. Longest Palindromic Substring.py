# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        longest_palindrome = ""

        def expand_from_center(left: int, right: int) -> str:

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return s[left + 1:right]

        for center in range(len(s)):

            # Odd length palindrome
            odd_palindrome = expand_from_center(center, center)

            # Even length palindrome
            even_palindrome = expand_from_center(center, center + 1)

            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome

            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome
