# https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        lightest_person = 0
        heaviest_person = len(people) - 1

        boat_count = 0

        while lightest_person <= heaviest_person:

            # Can the lightest and heaviest share one boat?
            if people[lightest_person] + people[heaviest_person] <= limit:
                lightest_person += 1

            # The heaviest person always gets on the current boat
            heaviest_person -= 1

            boat_count += 1

        return boat_count