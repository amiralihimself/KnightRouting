"""
This module contains an implementation of knight routing algorithms on an n X m chessboard.The input is an nXn representing a chessboard.
The squares of the input chessboard can either have obstacles placed on them, or be one of the start or end positions
Let s_ij be the square located on the i-th row and the j-th column of the chessboard, and let A be the nXn array representing the array. Then, we have;
+-----------+-----------------------------------+
| A[i][j]=1 | If there is an obstacle on s_ij   |
+-----------+-----------------------------------+
| A[i][j]=2 | If s_ij is the starting square    |
+-----------+-----------------------------------+
| A[i][j]=3 | If s_ij is the destination square |
+-----------+-----------------------------------+
| A[i][j]=0 | Otherwise                         |
+-----------+-----------------------------------+

I assume the following:
1) The starting square cannot have any obstacles in it
2) The destination square cannot have any obstacles in it
3) The source and destination squares are necessarily different
"""
import inf
def knightMoves()
def recursivebranchAndBound(row, col, limit, fitnessValue, visitedAlongTheWay):
    visitedAlongTheWay.append((row, col))
    path2.append((row, col))
    if test_goal(row, col):
        return (row, col), 0
    children = knight_moves(f_n, row, col)
    if len(children) is 0:
        return None, inf
    while True:
        children.sort(key=lambda x: x[0])
        # min_f_n = children[0][0] + manhattan(children[0][1], children[0][2], goal_row,goal_col)
        min_f_n = children[0][0]
        if min_f_n > limit:
            return "flimit", min_f_n
        if len(children) > 1:
            ## alternative=children[1][0]+manhattan(children[1][1],children[1][2],goal_row,goal_col)
            alternative = children[1][0]
        else:
            alternative = infinity
        result, min_f_n = RBFS(children[0][1], children[0][2], min(alternative, flimit), children[0][0])
        if result is not None and result is not "flimit":
            return result, min_f_n
        elif result is "flimit":
            path2.pop(len(path2) - 1)
            temp_tup = (min_f_n, children[0][1], children[0][2])
            children.pop(0)
            children.insert(0, temp_tup)
