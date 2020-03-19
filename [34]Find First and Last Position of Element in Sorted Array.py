class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs_left(left, right):
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def bs_right(left, right):
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        n = len(nums) - 1
        left, right = bs_left(0, n), bs_right(0, n)
        return [left, right] if left <= right else [-1, -1]
