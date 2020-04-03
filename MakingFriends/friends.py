import sys
from collections import deque

def parse_data():
    data = sys.stdin.read().strip().split('\n')
    data =  [line.split(' ') for line in data]
    data = [[int(x) for x in line] for line in data]
    return int(data[0][0]),int(data[0][1]),data[1:] # N, M, data

N,M,data = parse_data()
print(data)
