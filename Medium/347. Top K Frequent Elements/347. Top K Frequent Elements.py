# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                counter = dict()
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter[num] = 1

        heap = []
        for key, value in counter.items():
            if len(heap) >= k:
                heappushpop(heap, (value, key))
            else:
                heappush(heap, (value, key))

        # result = []
        # for _ in range(k):
        #     result.append(heappop(heap)[1])
        # return result

        return [heappop(heap)[1] for _ in range(k)]

        # Second method
        # counter = dict()
        # for num in nums:
        #     if num in counter:
        #         counter[num] = counter[num] + 1
        #     else:
        #         counter[num] = 1

        # heap = []
        # for key, value in counter.items():
        #     heappush(heap, (-value, key))

        # result = []
        # for _ in range(k):
        #     result.append(heappop(heap)[1])

        # return result

