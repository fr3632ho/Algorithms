#!/bin/python3

import sys

def parse_data():
	penalty = -4

	x = sys.stdin.read().split('\n')
	alphabet = x[0].split()
	dim = range(len(alphabet))

	# Cost matrix for aligning i with j
	cost_matrix = [[int(j) for j in i.split()] for i in x[1:len(alphabet)+1]]

	# Alignment matrix map -> matrix['A']['C'] = -3
	matrix = {}
	for i in range(len(alphabet)):
		matrix[alphabet[i]] = {}
		for j in range(len(alphabet)):
			matrix[alphabet[i]][alphabet[j]] = cost_matrix[i][j]

	# Queries to be evaluated. queries[0] = ['String1', 'String2']
	queries = [[j for j in i.split()] for i in x[len(alphabet)+2:len(x) - 1]]

	# print(f'Finished parsing data, got the following queries: {queries} & alphabet: {alphabet}')

	# Looping over queries
	for query in queries:
		s, t = query[0], query[1]

		# Size of strings inside query
		n, m = len(s), len(t)
		k = max(n,m)
		dp = [[0 for x in range(k + 1)] for y in range(k + 1)]

		for i in range(k + 1):
			dp[0][i] = penalty * i
			dp[i][0] = penalty * i

		for i in range(1,n+1):
			for j in range(1,m+1):

				# Alignment cost
				alfa = matrix[s[i - 1]][t[j - 1]]

				dp[i][j] = max(
						dp[i - 1][j - 1] + alfa,
						dp[i - 1][j] + penalty,
						dp[i][j - 1] + penalty)



		l = n + m
		i, j = n, m
		ys = [0]*(l + 1)
		xs = [0]*(l + 1)
		xpos = l
		ypos = l

		while not (i == 0 or j == 0):

			# print(f's[i - 1] = {s[i - 1]}' )
			# print(f't[j - 1] = {t[j - 1]}' )
			# print(f't = {t}' )
			# print(f's = {s}' )
			# print(f'xs = {xs}' )
			# print(f'dp[{i}][{j}] = {dp[i][j]} \n' )

			# if s[i - 1] == t[j - 1]:
			# 	xs[xpos] = s[i - 1]
			# 	ys[ypos] = t[j - 1]
			# 	xpos, ypos, i, j = dec(1, xpos, ypos, i, j)

			if (dp[i - 1][j - 1] + matrix[s[i - 1]][t[j - 1]]) == dp[i][j]:
				xs[xpos] = s[i - 1]
				ys[ypos] = t[j - 1]
				xpos, ypos, i, j = dec(1, xpos, ypos, i, j)

			elif (penalty + dp[i - 1][j]) == dp[i][j]:
				xs[xpos] = s[i - 1]
				ys[ypos] = '*'
				xpos, ypos, i = dec(1, xpos, ypos, i)

			else:# (penalty + dp[i][j - 1]) == dp[i][j]:
				xs[xpos] = '*'
				ys[ypos] = t[j - 1]
				xpos, ypos, j = dec(1, xpos, ypos, j)

		while xpos > 0:
			if i > 0:
				xs[xpos] = s[i - 1]
				i -= 1
			else:
				xs[xpos] = '*'

			xpos -= 1

		while ypos > 0:
			if j > 0:
				ys[ypos] = t[j - 1]
				j -= 1
			else:
				ys[ypos] = '*'

			ypos -= 1

		id = 1
		for i in range(l, 0, -1):
			if ys[i - 1] == '*' and xs[i - 1] == '*':
				id = i
				break

		print("".join(xs[id:]), "".join(ys[id:]))

def dec(val, *args):
	for i in args:
		yield i - val

def main():
	parse_data()


if __name__ == '__main__':
	main()
