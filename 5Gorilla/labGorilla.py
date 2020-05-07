#!/bin/python3

import sys

def parse_data():
	x = sys.stdin.read().split('\n')
	alphabet = x[0].split()
	dim = range(len(alphabet))


	cost_matrix = [[int(j) for j in i.split()] for i in x[1:len(alphabet)+1]]

	matrix = {}
	for i in range(len(alphabet)):
		matrix[alphabet[i]] = {}
		for j in range(len(alphabet)):
			matrix[alphabet[i]][alphabet[j]] = cost_matrix[i][j]

	print(matrix)

	queries = [[j for j in i.split()] for i in x[len(alphabet)+2:len(x) - 1]]

	print(f'Finished parsing data, got the following queries: {queries} & alphabet: {alphabet}')

	for query in queries:
		parent(query[0], query[1], cost_matrix)

def parent(s, t, c):
	opt(len(s), len(t), s, t)

def opt(i, j, s, t):
	if j == 0:
		return i * -4
	if i == 0:
		return j * -4



def main():
	parse_data()


if __name__ == '__main__':
	main()