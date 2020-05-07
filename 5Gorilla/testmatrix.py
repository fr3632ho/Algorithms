cost_matrix = [[2, 0, -1], [0, 3, 1], [-1, 1, 3]]
matrix = {}
alpha = ['A', 'B', 'C']

for i in range(len(alpha)):
	matrix[alpha[i]] = {}
	for j in range(len(alpha)):
		matrix[alpha[i]][alpha[j]] = cost_matrix[i][j]

print(matrix)