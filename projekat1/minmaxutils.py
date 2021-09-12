

class Node:
    def __init__(self, move, value):
        self._move = move
        self._value = value


"""
za sada heuristika se racuna tako sto se oduzima broj protivnikovih bodova, broj racunarovih bodova
"""





def heuristic(opponent_positions, my_positions):

    my_points = sum_points(my_positions, 4)
    opponent_points = sum_points(opponent_positions, 4)
    return my_points - opponent_points


"""
na osnovu pozicija vraca broj uzastopnih duzine num
"""


def sum_points(positions, num):
    points = 0
    for position in positions:

        right = 0
        left = 0
        up = 0
        down = 0
        right_up = 0
        right_down = 0
        left_up = 0
        left_down = 0
        x = position[0]
        y = position[1]

        # gore dole
        if ([x - 1, y] in positions and [x + 1, y] not in positions):
            for i in range(1, num):
                if [x - i, y] in positions:
                    up += 1
                else:
                    up = 0
                    break
            if up > 0 and [x - num, y] not in positions:
                points += 1


        elif [x - 1, y] not in positions and [x + 1, y] in positions:
            for i in range(1, num):
                if [x + i, y] in positions:
                    down += 1
                else:
                    down = 0
                    break
            if down > 0 and [x + num, y] not in positions:
                points += 1

        # lijevo desno
        if [x, y - 1] in positions and [x, y + 1] not in positions:
            for i in range(1, num):
                if [x, y - i] in positions:
                    left += 1
                else:
                    left = 0
                    break
            if left > 0 and [x, y - num] not in positions:
                points += 1
        elif [x, y - 1] not in positions and [x, y + 1] in positions:
            for i in range(1, num):
                if [x, y + i] in positions:
                    right += 1
                else:
                    right = 0
                    break
            if right > 0 and [x, y + num] not in positions:
                points += 1

        # desno gore ukoso
        if [x - 1, y + 1] in positions and [x + 1, y - 1] not in positions:
            for i in range(1, num):
                if [x - i, y + i] in positions:
                    right_up += 1
                else:
                    right_up = 0
                    break
            if right_up > 0 and [x - num, y + num] not in positions:
                points += 1
        elif [x - 1, y + 1] not in positions and [x + 1, y - 1] in positions:
            for i in range(1, num):
                if [x + i, y - i] in positions:
                    left_down += 1
                else:
                    left_down = 0
                    break
            if left_down > 0 and [x + num, y - num] not in positions:
                points += 1

        # lijevo ukoso
        if [x + 1, y + 1] in positions and [x - 1, y - 1] not in positions:
            for i in range(1, num):
                if [x + i, y + i] in positions:
                    right_down += 1
                else:
                    right_down = 0
                    break
            if right_down > 0 and [x + num, y + num] not in positions:
                points += 1
        elif [x + 1, y + 1] not in positions and [x - 1, y - 1] in positions:
            for i in range(1, num):
                if [x - i, y - i] in positions:
                    left_up += 1
                else:
                    left_up = 0
                    break
            if left_up > 0 and [x - num, y - num] not in positions:
                points += 1

    return int(points / 2)


all_moves = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],
             [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9],
             [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9],
             [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
             [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
             [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],
             [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9],
             [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9],
             [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
             [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]]


# generise sledeci potez na osnovu trenutnog stanja tabele, poslednjeg poteza i heuristike
def generate_next_move(my_positions, opponent_positions, last_opponent_move):
    node = minimax(my_positions, opponent_positions, last_opponent_move, 4, -999, 999, True)

    return node._move


def generate_possible_moves(gamestate, last_opponent_move):
    possible_moves = []
    x = last_opponent_move[0]
    y = last_opponent_move[1]
    x2 = x + 1
    y2 = y + 1
    x3 = x - 1
    y3 = y - 1
    if ([x2, y2] in all_moves and is_near([x2, y2], [x, y]) and not [x2, y2] in gamestate):
        possible_moves.append([x2, y2])

    if ([x2, y3] in all_moves and is_near([x2, y3], [x, y]) and not [x2, y3] in gamestate):
        possible_moves.append([x2, y3])

    if ([x3, y2] in all_moves and is_near([x3, y2], [x, y]) and not [x3, y2] in gamestate):
        possible_moves.append([x3, y2])

    if ([x3, y3] in all_moves and is_near([x3, y3], [x, y]) and not [x3, y3] in gamestate):
        possible_moves.append([x3, y3])

    if ([x, y2] in all_moves and is_near([x, y2], [x, y]) and not [x, y2] in gamestate):
        possible_moves.append([x, y2])

    if ([x2, y] in all_moves and is_near([x2, y], [x, y]) and not [x2, y] in gamestate):
        possible_moves.append([x2, y])

    if ([x3, y] in all_moves and is_near([x3, y], [x, y]) and not [x3, y] in gamestate):
        possible_moves.append([x3, y])

    if ([x, y3] in all_moves and is_near([x, y3], [x, y]) and not [x, y3] in gamestate):
        possible_moves.append([x, y3])

    if (possible_moves == []):
        for i in range(10):
            for j in range(10):
                if ([i, j] not in gamestate):
                    possible_moves.append([i, j])
    #print("MOGUCIII POTEZII ", possible_moves)
    return possible_moves


def is_near(first, second):
    return abs(first[0] - second[0]) <= 1 and abs(first[1] - second[1]) <= 1


def minimax(my_positions, opponent_positions, last_opponents_move, depth, alpha, beta, maximizingPlayer):
    """print("-"*15)
    if maximizingPlayer:
        print("POZICIJE RACUNARA: ", my_positions)
        print( "POZICIJE IGRACA: ",opponent_positions)
        print("IGRAC ODIGRAO POTEZ: ", last_opponents_move)

    else:
        print("POZICIJE RACUNARA: ", opponent_positions)
        print("POZICIJE IGRACA: ", my_positions)
        print("RACUNAR ODIGRAO POTEZ: ", last_opponents_move)

    print("-"*15)"""


    if depth == 0:
        return Node(last_opponents_move, heuristic(opponent_positions, my_positions))

    if maximizingPlayer:
        maxEval = Node(None, -999)
        positions = generate_possible_moves(my_positions + opponent_positions, last_opponents_move)
        for position in positions:



            eval = minimax(opponent_positions, my_positions + [position], position, depth - 1, alpha, beta, False)

            if eval._value > maxEval._value:
                maxEval._move = position
                maxEval._value = eval._value


            alpha = max(alpha, eval._value)
            if beta <= alpha:

                break
        return maxEval

    else:
        minEval = Node(None, 999)
        positions = generate_possible_moves(my_positions + opponent_positions, last_opponents_move)
        for position in positions:
            eval = minimax(opponent_positions, my_positions + [position], position, depth - 1, alpha, beta, True)


            if minEval._value > eval._value:
                minEval._value = eval._value
                minEval._move = position

            beta = min(beta, eval._value)
            if beta <= alpha:

                break
        return minEval



