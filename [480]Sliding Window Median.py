class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        wind = sorted(nums[:k])
        res = []
        for a, b in zip(nums, nums[k:] + [0]):
            res.append((wind[k // 2] + wind[~(k // 2)]) / 2.)
            wind.remove(a)
            bisect.insort(wind, b)
        return res
