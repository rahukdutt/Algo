def main():

	import numpy as np

	def find_max_min_block(grid):
		n = len(grid)
		sep="#"
		max_min = -1
		max_min_positions = []
		min_grid=np.zeros((n, n))
		for i in range(n):
			for j in range(n):
				# Consider 8 neighboring blocks
				neighbors = [(i,j),(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
							 (i + 1, j + 1)]
				min_neighbor_val = float('inf')
				for neighbor in neighbors:
					if (neighbor[0] >= 0 and neighbor[0] < n) and (neighbor[1] >= 0 and neighbor[1] < n):
						#print("## i:",i,"j:",j,grid[neighbor[0]][neighbor[1]])
						min_neighbor_val = min(min_neighbor_val, grid[neighbor[0]][neighbor[1]])
						#print("## i:", i, "j:", j,"neighbor:",neighbor)
						#print(min_neighbor_val)
				min_grid[i][j]=min_neighbor_val
		#print("#######",min_grid)
		max_value = np.amax(min_grid)
		#print(max_value)
		max_index = np.where(min_grid == max_value)
		for i in range(len(max_index[0])):
			print("{}{}{}".format(1+max_index[0][i], "#", 1+max_index[1][i]))
		return min_grid


	def create_grid():
		n = int(input())
		grid = []
		#print("Enter the grid values:")
		for i in range(n):
			grid.append(list(map(int, input().split("#"))))
		return grid


	grid = create_grid()
	#print(grid)
	find_max_min_block(grid)

main()
