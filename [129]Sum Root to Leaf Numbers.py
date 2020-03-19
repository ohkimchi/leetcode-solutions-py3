# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        stk = [(root, 0)]
        while stk:
            cur_root, cur_sum = stk.pop()
            if cur_root:
                cur_sum = cur_root.val + 10*cur_sum
                if not cur_root.left and not cur_root.right:
                    ans += cur_sum
                else:
                    stk.append((cur_root.left, cur_sum))
                    stk.append((cur_root.right, cur_sum))
        return ans