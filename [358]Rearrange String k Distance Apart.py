from collections import Counter, deque
from heapq import heapify, heappush, heappop


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        c = Counter(s)
        q = [[-c[ch], ch] for ch in c]
        heapify(q)
        mem = deque()

        res = ''
        while len(q) or len(mem):
            if len(mem) == k:
                cur = mem.popleft()
                if cur[0] < 0:
                    heappush(q, cur)
            if len(q):
                cur = heappop(q)
                res += cur[1]
                cur[0] += 1
                mem.append(cur)
            else:
                if sum([item[0] for item in mem]) == 0:
                    return res
                return ''
