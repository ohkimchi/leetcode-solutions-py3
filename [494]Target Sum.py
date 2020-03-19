from collections import defaultdict 

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            step = defaultdict(int)
            for y in cnt:
                step[y+x] += cnt[y]
                step[y-x] += cnt[y]
            cnt = step
        return cnt[S]