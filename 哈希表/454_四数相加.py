class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # 字典的key是数组元素之和 value是这个和出现的次数
        dict1 = {}
        for i in nums1:
            for j in nums2:
                if dict1.get(i + j):
                    dict1[i + j] += 1
                else:
                    dict1[i + j] = 1
        res = 0
        for i in nums3:
            for j in nums4:
                if dict1.get(-i - j):
                    res += dict1[-i - j]
        return res
