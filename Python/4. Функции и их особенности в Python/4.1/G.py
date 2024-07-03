def can_eat(knight_pos, other_pos):
    x1, y1 = knight_pos
    x2, y2 = other_pos

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
