# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
#
# Example 1: 
#
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
#
# 
#
# Example 2: 
#
# 
# Input: 3
# Output: False
# 
#
# 
# Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c))
        i, j = 0, n
        while i <= j:
            res = i * i + j * j
            if res == c:
                return True
            elif res < c:
                i += 1
            else:
                j -= 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
