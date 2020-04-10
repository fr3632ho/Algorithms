import sys
from math import inf
import heapq
from collections import deque,defaultdict

import random

def parse_data():
    data = sys.stdin.read().strip().split('\n')
    data = [[int(x) for x in line.split(' ')] for line in data]
    graph = defaultdict(list)
    heap = []
    for frm,to,cost in data[1:]:
        graph[frm].append((to,cost))
        graph[to].append((frm,cost))
        heapq.heappush(heap,(cost,frm,to))
        heapq.heappush(heap,(cost,to,frm))

    return int(data[0][0]),int(data[0][1]),graph,heap # N, M, data


'''
Minimal value in keys that has yet not been visited!
'''
def prim(G,root):
    #Q := Unexplored vertices, V:= Explored vertices
    total_weight = 0
    Q = [(0,root)]
    V = set()

    while Q:

        weight,u = heapq.heappop(Q)

        if u not in V:
            V.add(u)
            total_weight += weight
            for n,cost in G[u]:
                if n not in V:
                    heapq.heappush(Q,(cost,n))

    return total_weight

N,M,G,heap = parse_data()
#print(N,M)
#print(f'N: {N},M: {M},\nDATA: {G}\nHeap: {heap}')
print(prim(G,1))








#END
