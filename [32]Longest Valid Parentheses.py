class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                res = max(res, i - stack[-1][0])
            else:
                stack += (i, paren),
        return res
