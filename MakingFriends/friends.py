import sys
import heapq
from collections import deque,defaultdict

import random

def parse_data():
    data = sys.stdin.read().strip().split('\n')
    data =  [line.split(' ') for line in data]
    data = [[int(x) for x in line] for line in data]
    graph = defaultdict(list)
    queue = []
    for pair in data[1:]:
        graph[pair[0]].append((pair[1],pair[2]))
        graph[pair[1]].append((pair[0],pair[2]))
        queue.append(pair)

    return int(data[0][0]),int(data[0][1]),graph # N, M, data,Q


'''
Minimal value in keys that has yet not been visited!
'''
def minimumValue(keys,visited):
    min = 10**12
    min_index =-1

    #This is slow!
    for i in range(N):
        if keys[i] < min and visited[i] == False:
            min = keys[i]
            min_index = i
    return min_index

def prim(G,root):
    # visited vertices, starting min value, parents
    visited = [False]*N
    keys = [10**12]*N
    keys[0] = root-1
    #parents = [0]*N
    #parents[0] = -1
    for v in range(N):

        #Finds the index of the minimal value in keys!
        u = minimumValue(keys,visited)
        #Sets u as a visited node!
        visited[u] = True

        neighbours = G[u+1]

        #print(f'u: {u+1}\nneighbours: {neighbours}\nIndex : {u}\n')
        for n in neighbours:

            v,w = n[0],n[1]

            if w < keys[v-1] and not visited[v-1]:

                keys[v-1] = w

    print(sum(keys[1:]))

N,M,G = parse_data()
print(N,M)
#print(f'N: {N},M: {M},\nDATA: {G}')
#print({1,2}.issubset({1,2,3,4}),{2,1}.issubset({1,2,3,4}))
prim(G,1)







#END
