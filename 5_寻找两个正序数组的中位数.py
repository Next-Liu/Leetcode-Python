# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2

class Solution:
    def findMedianSortedArrays(nums1: list, nums2: list):
        if nums1 == []:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            else:
                return nums2[len(nums2) // 2]
        elif nums2 == []:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
            else:
                return nums1[len(nums1) // 2]
        len1 = len(nums1)
        len2 = len(nums2)
        len3 = len1 + len2
        i = j = k = 0
        if len3 % 2 == 0:
            len3 = len3 // 2
            while k < len3 - 1:
                if i < len1 and j < len2:
                    if nums1[i] < nums2[j]:
                        i += 1
                    else:
                        j += 1
                elif i < len1:
                    i += 1
                else:
                    j += 1
                k += 1
            if i < len1 and j < len2:
                return (nums1[i] + nums2[j]) / 2
            elif i < len1:
                return (nums1[i] + nums1[i + 1]) / 2
            else:
                return (nums2[j] + nums2[j + 1]) / 2
        else:
            len3 = len3 // 2
            while k < len3 - 1:
                if i < len1 and j < len2:
                    if nums1[i] < nums2[j]:
                        i += 1
                    else:
                        j += 1
                elif i < len1:
                    i += 1
                else:
                    j += 1
                k += 1
            if i < len1 and j < len2:
                return nums1[i] if nums1[i] > nums2[j] else nums2[j]
            elif i < len1:
                return nums1[i + 1]
            else:
                return nums2[j + 1]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3]
    print(Solution.findMedianSortedArrays(nums1, nums2))
