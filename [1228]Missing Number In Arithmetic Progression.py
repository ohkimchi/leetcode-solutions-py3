# In some array arr, the values were in arithmetic progression: the values arr[i+1] -
# arr[i] are all equal for every 0 <= i < arr.length - 1.
#
# Then, a value from arr was removed that was not the first or last value in the array. 
#
# Return the removed value. 
#
# 
# Example 1: 
#
# 
# Input: arr = [5,7,11,13]
# Output: 9
# Explanation: The previous array was [5,7,9,11,13].
# 
#
# Example 2: 
#
# 
# Input: arr = [15,13,12]
# Output: 14
# Explanation: The previous array was [15,14,13,12].
#
# 
# Constraints: 
#
# 
# 3 <= arr.length <= 1000 
# 0 <= arr[i] <= 10^5 
# 
# Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)

# leetcode submit region end(Prohibit modification and deletion)
