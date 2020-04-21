class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = dict()
        s = 0
        d[s] = -1
        for i in range(len(nums)):
            s += nums[i]
            if k != 0:
                s %= k
            if s in d:
                if i - d[s] > 1:
                    return True
            else:
                d[s] = i
        return False
