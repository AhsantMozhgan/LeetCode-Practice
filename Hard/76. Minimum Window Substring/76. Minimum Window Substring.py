# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if either string is empty
        if not s and not t:
            return ""

        # Create a counter for the characters in t
        need = Counter(t)

        # Initialize a dictionary to count characters in the current window
        window = dict()

        # Counters for unique characters that are currently in the window
        have = 0
        
        required = len(need)    # Total unique characters required

        left = 0    # Left pointer for the sliding window

        result = ""     # To store the result substring

        result_length = float('inf')    # Initialize result length to infinity

        # Iterate over the string with the right pointer
        for right in range(len(s)):
            char = s[right]
            # Add the current character to the window count
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1   # Increment have when the current char meets the need

            # When we have all required characters
            while have == required:
                current_length = right - left + 1   # Calculate the current window length

                # Update result if the current window is smaller than the previous best
                if current_length < result_length:
                    result_length = current_length
                    result = s[left:right + 1]  # Update the result substring

                # Remove the leftmost character from the window
                left_char = s[left]
                window[left_char] -= 1  # Decrease the count of the left character

                # If removing left_char causes a deficit, decrease have
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1  # Move the left pointer to shrink the window

        return result  # Return the minimum window substring
        
        
        
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not t or not s:
#             return ""

#         # Dictionary to keep track of character counts in t
#         dict_t = Counter(t)

#         # Unique characters in t that need to be present in the window
#         required_char_types = len(dict_t)  

#         # Pointers and variables for the sliding window
#         left, right = 0, 0

#         # To keep track of how many unique characters in t are currently in the window
#         satisfied_char_types = 0 

#         window_counts = defaultdict(int)  # Current window character counts

#         # Result tuple (length, left, right)
#         smallest_window = float("inf"), None, None

#         while right < len(s):
#             current_char = s[right]
#             window_counts[current_char] += 1

#             # Only count the characters that are needed (in t)
#             if current_char in dict_t and window_counts[current_char] == dict_t[current_char]:
#                 satisfied_char_types += 1

#             # Try to shrink the window until it ceases to be 'desirable'
#             while left <= right and satisfied_char_types == required_char_types:
#                 current_char = s[left]

#                 # Update the result if this window is smaller than the previous minimum
#                 if right - left + 1 < smallest_window[0]:
#                     smallest_window = (right - left + 1, left, right)

#                 # Remove the leftmost character from the window
#                 window_counts[current_char] -= 1
#                 if current_char in dict_t and window_counts[current_char] < dict_t[current_char]:
#                     satisfied_char_types -= 1
                
#                 left += 1  # Move left pointer forward to reduce the size of the window
            
#             right += 1  # Expand the window by moving right pointer

#         # Return the minimum window substring or empty string if no window was found
#         return "" if smallest_window[0] == float("inf") else s[smallest_window[1]: smallest_window[2] + 1]
