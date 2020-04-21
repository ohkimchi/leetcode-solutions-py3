class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.s = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.s[i][j] = matrix[i - 1][j - 1] + self.s[i - 1][j] + self.s[i][j - 1] - self.s[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.s[row2 + 1][col2 + 1] - self.s[row1][col2 + 1] - self.s[row2 + 1][col1] + self.s[row1][col1]
