class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)
        for row in range(9):
            for col in range(9):
                entry = board[row][col]
                if entry != ".":
                    entry = int(entry)
                    box_key = (row//3, col//3)
                    if (entry in row_map[row]) or (entry in col_map[col]) or (entry in box_map[box_key]):
                        return False
                    row_map[row].add(entry)
                    col_map[col].add(entry)
                    box_map[box_key].add(entry)
        return True