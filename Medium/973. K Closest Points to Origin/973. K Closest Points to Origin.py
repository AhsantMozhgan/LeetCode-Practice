# https://leetcode.com/problems/k-closest-points-to-origin/submissions/2070473227/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nearest = []
        heap = []

        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            heappush(heap, (distance, point))

        for i in range(k):
            nearest.append(heappop(heap)[1])

        return nearest


        # heap = []
        # for x, y in points:
        #     d = x ** 2 + y ** 2
        #     if len(heap) < k:
        #         heappush(heap, (-d, x, y))
        #     else:
        #         heappushpop(heap, (-d, x, y))

        # return [(x, y) for d, x, y in heap]

        # # Time: O(n log k)
        # # Space: O(k)
