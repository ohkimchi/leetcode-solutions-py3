from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans, hp = matrix[0][0], []
        heappush(hp, (ans, 0, 0))
        n, m = len(matrix), len(matrix[0])
        while k:
            ans, r, c = heappop(hp)
            if r == 0 and c + 1 < m:
                heappush(hp, (matrix[r][c + 1], r, c + 1))
            if r + 1 < n:
                heappush(hp, (matrix[r + 1][c], r + 1, c))
            k -= 1
        return ans

