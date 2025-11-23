from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue

                corner_r, corner_c = r // 3, c // 3
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sub_boxes[(corner_r, corner_c)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_boxes[(corner_r, corner_c)].add(board[r][c])
                
        return True


if __name__ == "__main__":
    solution = Solution()

    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    assert solution.isValidSudoku(board)

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    assert not solution.isValidSudoku(board)
