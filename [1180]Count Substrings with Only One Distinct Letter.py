# Given a string S, return the number of substrings that have only one distinct letter.
#
# 
# Example 1: 
#
# 
# Input: S = "aaaba"
# Output: 8
# Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
# "aaa" occurs 1 time.
# "aa" occurs 2 times.
# "a" occurs 4 times.
# "b" occurs 1 time.
# So the answer is 1 + 2 + 4 + 1 = 8.
# 
#
# Example 2: 
#
# 
# Input: S = "aaaaaaaaaa"
# Output: 55
# 
#
# 
# Constraints: 
#
# 
# 1 <= S.length <= 1000 
# S[i] consists of only lowercase English letters. 
# 
# Related Topics Math String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countLetters(self, S: str) -> int:
        res = 0
        for i, j in itertools.groupby(S):
            test = list(j)
            for k in range(1, len(test) + 1):
                res += len(test) - k + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
