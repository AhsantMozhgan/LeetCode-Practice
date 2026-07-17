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
