# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, return False
        window_size = len(s1)
        if window_size > len(s2):
            return False

        # Create frequency counts for s1 and the initial window in s2
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:window_size])

        # Check if the first window matches
        if s1_counter == window_counter:
            return True
        
        # Start sliding the window
        for i in range(window_size, len(s2)):
            # Add new character to the window
            window_counter[s2[i]] += 1
            
            # Remove the leftmost character of the window
            left_char = s2[i - window_size]
            window_counter[left_char] -= 1
            
            # If the count goes to zero, remove it from the dictionary
            if window_counter[left_char] == 0:
                del window_counter[left_char]
            
            # Compare the current window count with s1's count
            if s1_counter == window_counter:
                return True

        return False  # No permutation of s1 is a substring of s2


# class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:

    #     if len(s1) > len(s2):
    #         return False

    #     count_s1 = Counter(s1)
    #     window_size = len(s1)

    #     count_window = defaultdict(int)
    #     for i in range(window_size):
    #         count_window[s2[i]] += 1

    #     if count_s1 == count_window:
    #         return True

    #     left = 0
    #     for right in range(window_size, len(s2)):
    #         left_char = s2[left]

    #         if count_window[left_char] == 1:
    #             del count_window[left_char]
    #         else:
    #             count_window[left_char] -= 1

    #         count_window[s2[right]] += 1
    #         left += 1

    #         if count_s1 == count_window:
    #             return True

    #     return False
    