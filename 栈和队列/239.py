from collections import deque


# 单调队列
class Myqueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):  # value是要出队的值，因为每一轮都要出队一个值，所以要传入
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def getMax(self):
        return self.queue[0]


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que = Myqueue()
        res = []
        for i in range(k):
            que.push(nums[i])
        res.append(que.getMax())
        for j in range(k, len(nums)):
            que.pop(nums[j - k])
            que.push(nums[j])
            res.append(que.getMax())
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.maxSlidingWindow(nums, k))