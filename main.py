# variables


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def solve(c_board):
    find = find_empty(c_board)
    if not find:
        return True
    else:
        row,col=find
        for i in range(1,10):
            if isvalid(c_board,find,i):
                c_board[row][col]=i
                if solve(c_board):
                    return True
                c_board[row][col]=0

def print_board(c_board):
    # should print with seperators
    for i in range(len(c_board)):
        for j in range(len(c_board[0])):
            print(c_board[i][j], end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print("")
        if (i + 1) % 3 == 0:
            print("---------------------")


def find_empty(c_board):
    for i in range(9):
        for j in range(9):
            if c_board[i][j] == 0:
                return (i, j)
    return None


def isvalid(c_board, pos, num):
    # check in rows for reluctant data
    for i in range(9):
        if c_board[pos[0]][i] == num and i != pos[1]:
            return False
    # check in columns for reductant data
    for i in range(9):
        if c_board[i][pos[1]] == num and i != pos[0]:
            return False
    # check in grid
    gridx, gridy, = pos[0] // 3, pos[1] // 3
    for i in range(3):
        for j in range(3):
            if c_board[gridx * 3 + i][gridy * 3 + j] == num and (gridx * 3 + i, gridy * 3 + j) != pos:
                return False
    return True
solve(board)
print_board(board)