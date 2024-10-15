# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 说明：
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp[i]=true 代表字符串长度为i时 可以被拆分，若dp[j]=true 且s[j:i]在wordDict中，则dp[i]=true
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):  # 遍历背包
            for j in range(i):  # 遍历单词
                if dp[j] and s[j:i] in wordDict:  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    # s[0:j]由dp[j]的值确定，s[j:i]在wordDict中，所以直接为True
                    dp[i] = True
                    break
        return dp[-1]
