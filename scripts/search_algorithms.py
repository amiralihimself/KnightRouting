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