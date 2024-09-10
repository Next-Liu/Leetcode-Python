# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 2：abc 3：def 4：ghi 5：jkl 6：mno 7：pqrs 8：tuv 9：wxyz
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 回溯法 “23”
#  a       b       c
# d e f   d e f   d e f
class Solution:
    def letterCombinations(self, digits: str):
        digit_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []

        def traceback(index):
            if index == len(digits):
                ans.append("".join(letters))
            else:
                digit = digits[index]
                for letter in digit_dict[digit]:
                    letters.append(letter)
                    traceback(index + 1)
                    letters.pop()

        letters = []
        ans = []
        traceback(0)
        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
