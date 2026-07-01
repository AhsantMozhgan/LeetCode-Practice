class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Initialize a hash map
        value_to_index = {}

        # Step 2: Iterate through the array
        for index, value in enumerate(nums):
            complement = target - value

            # Step 3: Check if the complement is in the hash map
            if complement in value_to_index:
                # Step 4: Return the indices of the two numbers
                return [index , value_to_index[complement]]

            else:
                # Step 5: Store the current number and its index
                value_to_index[value] =  index

        # If no solution is found, returning an empty list (based on problem constraints, theoretically this should not happen)
        return []