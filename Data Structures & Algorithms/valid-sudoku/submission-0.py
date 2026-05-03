class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            checkSet = set()
            for value in row:
                if value != '.' and value in checkSet:
                    return False
                checkSet.add(value)

        for x in range(0, 9):
            checkSet = set()
            for y in range(0, 9):
                value = board[y][x]
                if value != '.' and value in checkSet:
                    return False
                checkSet.add(value)
                
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                checkSet = set()
                for y in range(i, i+3):
                    for x in range(j, j+3):
                        value = board[y][x]
                        if value != '.' and value in checkSet:
                            return False
                        checkSet.add(value)
                # print(checkSet)
                
        return True