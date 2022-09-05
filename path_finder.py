import random

row_num_1, col_num_1 =  random.randrange(0, 10, 1), random.randrange(0, 10, 1)
row_num_2, col_num_2 = random.randrange(0, 10, 1), random.randrange(0, 10, 1)

map = []

for row in range(10):
	map.append([])
	for col in range(10):
		if row == row_num_1 and col == col_num_1:
			map[row].append("0")
		elif row == row_num_2 and col == col_num_2:
			map[row].append("2")
		else:
			map[row].append("_")

for i in range(len(map)):
	print(map[i])
print("")
print("________________")

def find_destination_bfs(map, des):
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	queue = [(row_num_1, col_num_1)]
	visited = []
	b, d = (row_num_1, col_num_1), ()
	while len(queue) > 0:
		current_num = queue.pop(0)
		if current_num not in visited:
			if map[current_num[0]][current_num[1]] == "_":
				map[current_num[0]][current_num[1]] = "#"
			visited.append(current_num)
			for direction in directions:
				next_i, next_j = current_num[0] + direction[0], current_num[1] + direction[1]
				if 0 <= next_i < len(map) and 0 <= next_j < len(map[0]):
					if map[next_i][next_j] == des:
						return (next_i, next_j)
					if map[next_i][next_j] == "_" and (next_i, next_j) not in visited:
						queue.append((next_i, next_j))

def find_destination_dfs(map, des):
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	stack = [(row_num_1, col_num_1)]
	visited = []
	b, d = (row_num_1, col_num_1), ()
	while len(stack) > 0:
		current_num = stack.pop()
		if current_num not in visited:
			if map[current_num[0]][current_num[1]] == "_":
				map[current_num[0]][current_num[1]] = "#"
			visited.append(current_num)
			for direction in directions:
				next_i, next_j = current_num[0] + direction[0], current_num[1] + direction[1]
				if 0 <= next_i < len(map) and 0 <= next_j < len(map[0]):
					if map[next_i][next_j] == des:
						return (next_i, next_j)
					if map[next_i][next_j] == "_" and (next_i, next_j) not in visited:
						stack.append((next_i, next_j))


def shortest_path(row_s, row_d, col_s, col_d, map):
	print("the shortest distance is ", (row_s - row_d if row_s >= row_d else row_d - row_s) + (col_s - col_d if col_s >= col_d else col_d - col_s))
	if row_s >= row_d:
		cur_row = row_s - 1
		while cur_row > row_d - 1:
			map[cur_row][col_s] = "1"
			cur_row -= 1
	else:
		cur_row = row_s + 1
		while cur_row < row_d + 1:
			map[cur_row][col_s] = "1"
			cur_row += 1

	if col_s >= col_d:
		cur_col = col_s - 1
		while map[row_d][cur_col] != "2":
			map[row_d][cur_col] = "1"
			cur_col -= 1
	else:
		cur_col = col_s + 1
		while map[row_d][cur_col] != "2":
			map[row_d][cur_col] = "1"
			cur_col += 1

	return map

destination1 = find_destination_dfs(map, "2")

map_with_path =  shortest_path(row_num_1, destination1[0], col_num_1, destination1[1], map)
for i in map_with_path:
	print(i)

destination2 = find_destination_bfs(map, "2")

# map_with_path =  shortest_path(row_num_1, destination2[0], col_num_1, destination2[1], map)
# for i in map_with_path:
# 	print(i)