class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        n, m = len(grid), len(grid[0])

        def explore(r, c, di=0):
            if 0 <= r < n and 0 <= c < m and grid[r][c] and (r, c) not in seen:
                seen.add((r, c))
                shape.append(di)
                explore(r + 1, c, 1)
                explore(r - 1, c, 2)
                explore(r, c + 1, 3)
                explore(r, c - 1, 4)
                shape.append(0)

        shapes = set()
        for i in range(n):
            for j in range(m):
                shape = []
                explore(i, j)
                if shape:
                    shapes.add(tuple(shape))
        return len(shapes)
