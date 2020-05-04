class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        todo, bit = num, 1
        while todo:
            num ^= bit
            todo >>= 1
            bit <<= 1
        return num
