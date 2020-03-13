from numpy.core.tests.test_mem_overlap import xrange


class NumArray:
    def __init__(self, nums):
        leng = len(nums)
        self.sums = [0] * (leng + 1)
        for i in xrange(leng):
            self.sums[i+1] =self.sums[i] +nums[i]

    def sumRange(self, i, j):
        return self.sums[j+1] - self.sums[i]
