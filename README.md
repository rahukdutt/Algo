# Algo
Short programs 
This code implements a solution to find the position of the block in a grid where the minimum value among all its neighbors is the maximum. The steps involved are:

Importing the numpy library.
Define a function "find_max_min_block" that takes a grid as input and returns the position of the block in the grid.
Within the function, the code first calculates the minimum value among all 8 neighboring blocks of each cell in the grid and stores the result in a new grid called "min_grid".
The maximum value in "min_grid" is then found using np.amax and the position is found using np.where.
The position is returned by printing the row and column indices (1-indexed).
A separate function "create_grid" is defined to create the grid. It takes the grid size as input and the grid values are entered as input separated by "#".
The main function calls both functions and passes the result of "create_grid" to "find_max_min_block".

