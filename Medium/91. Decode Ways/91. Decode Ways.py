# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:

        # A string starting with 0 cannot be decoded
        if not s or s[0] == "0":
            return 0

        string_length = len(s)

        # decode_count[i] = number of ways to decode
        # the first i characters of s
        decode_count = [0] * (string_length + 1)

        # Empty string has one valid decoding
        decode_count[0] = 1

        for current_position in range(1, string_length + 1):

            # Decode the current digit by itself
            if s[current_position - 1] != "0":
                decode_count[current_position] += decode_count[current_position - 1]

            # Decode the last two digits together
            if (
                current_position > 1
                and "10" <= s[current_position - 2:current_position] <= "26"
            ):
                decode_count[current_position] += decode_count[current_position - 2]

        return decode_count[string_length]
        