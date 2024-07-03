def make_board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((i + j) % 2)
        board.append(row)
    return board
