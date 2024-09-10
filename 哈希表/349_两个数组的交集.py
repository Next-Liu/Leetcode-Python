class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict2 = {}
        for i in nums1:
            dict1[i] = 1
        for i in nums2:
            dict2[i] = 1
        res = []
        for i in dict1:
            if i in dict2:
                res.append(i)
        return res
