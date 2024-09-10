# 一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。

# 在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽
# 底边宽度 − 1变短：
# 若向内移动短板 ，水槽的短板 min(h[i],h[j])可能变大或者变小，水槽面积可能变大或者变小
# 若向内移动长板 ，水槽的短板 min(h[i],h[j])不变或变小，因此水槽的面积不变或者变小 。
# 因此，初始化双指针分列水槽左右两端，循环每轮将短板向内移动一格，并更新面积最大值，直到两指针相遇时跳出；即可获得最大面积。
class Solution:
    def maxArea(self, height: list):
        i = 0
        j = len(height) - 1
        max_scale = (j - i) * min(height[i], height[j])
        while i != j:
            if height[i] < height[j]:
                i += 1
                max_scale = max(max_scale, (j - i) * min(height[i], height[j]))
            else:
                j -= 1
                max_scale = max(max_scale, (j - i) * min(height[i], height[j]))
        return max_scale


if __name__ == '__main__':
    l = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_scale = Solution().maxArea(l)
    print(max_scale)
