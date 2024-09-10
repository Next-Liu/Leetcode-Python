import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
        heap = []
        for key, value in map.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))  # 这里是小顶堆，所以要把value放在前面
            else:
                if value > heap[0][0]:
                    heapq.heappop(heap)  # 弹出堆顶元素
                    heapq.heappush(heap, (value, key))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])  # 弹出堆顶元素
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k))
