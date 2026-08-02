# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Count the frequency of each task
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        
        # Count how many tasks have the max frequency
        max_count = sum(1 for count in task_counts.values() if count == max_frequency)
        
        # Calculate total intervals
        # (max_frequency - 1) * (n + 1) is the length of the schedule needed for the maximum frequency task
        total_slots = (max_frequency - 1) * (n + 1) + max_count
        
        # The answer is the maximum of total_slots and the number of tasks to execute
        return max(total_slots, len(tasks))
