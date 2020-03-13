# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped
# to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally or vertically.
# Related Topics Depth-first Search Breadth-first Search Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        r_n = len(board)
        c_n = len(board[0])
        if r_n <= 2 or c_n <= 2:
            return

        q = collections.deque([])
        for r in range(r_n):
            for c in range(c_n):
                if (r in [0, r_n - 1] or c in [0, c_n - 1]) and board[r][c] == 'O':
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            if 0 <= r < r_n and 0 <= c < c_n and board[r][c] == 'O':
                board[r][c] = 'D'
                q.append((r - 1, c))
                q.append((r + 1, c))
                q.append((r, c - 1))
                q.append((r, c + 1))

        for r in range(r_n):
            for c in range(c_n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'D':
                    board[r][c] = 'O'

# leetcode submit region end(Prohibit modification and deletion)
