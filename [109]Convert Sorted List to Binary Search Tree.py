# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def convert(left, right):
            if left > right: return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            if left == right:
                return node
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node

        return convert(0, len(nums) - 1)

