class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(r, c):
            return not (cols[c] + hills[r + c] + dales[r - c])

        def place(r, c):
            cols[c] = 1
            hills[r + c] = 1
            dales[r - c] = 1
            queens.add((r, c))

        def add_ans():
            sln = []
            for _, c in sorted(queens):
                sln.append('.' * c + 'Q' + '.' * (n - c - 1))
            ans.append(sln)

        def remove_queen(r, c):
            cols[c] = 0
            hills[r + c] = 0
            dales[r - c] = 0
            queens.remove((r, c))

        def backtrack(r=0):
            for c in range(n):
                if can_place(r, c):
                    place(r, c)
                    if r == n - 1:
                        add_ans()
                    else:
                        backtrack(r + 1)
                    remove_queen(r, c)

        cols = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)
        queens = set()
        ans = []
        backtrack()
        return ans
