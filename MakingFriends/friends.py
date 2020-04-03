import sys
from collections import deque

def parse_data():
    data = sys.stdin.read().strip().split('\n')
    data =  [line.split(' ') for line in data]
    data = list(map(lambda x : list(map(lambda t : int(t),x)), data))
    return int(data[0][0]),int(data[0][1]),data[1:] # N, M, data

N,M,data = parse_data()
