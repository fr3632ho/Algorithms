import sys
import heapq
from collections import defaultdict

'''
Parses the data form standard in.
Returns: Undirected graph with the use of a defaultdict
'''
def parse_data():
    data = sys.stdin.read().strip().split('\n')
    data = [[int(x) for x in line.split(' ')] for line in data]
    graph = defaultdict(list)
    heap = []
    for frm,to,cost in data[1:]:
        graph[frm].append((to,cost))
        graph[to].append((frm,cost))

    return graph # N, M, data

'''
Implementation of prims algorithm from the lecture.
Data Structures: Heap for ordering the vertices, defaultdict for the graph and
                 set for the explored and unexplored vertices.
Returns: A total weight of all edges for the MST.
'''
def prim(G,root):
    #Q := Unexplored vertices, V:= Explored vertices
    total_weight = 0
    Q = [(0,root)]
    V = set()

    while Q:
        weight,u = heapq.heappop(Q)
        # If vertex u is already explored then continue
        if u not in V:
            # Add u to V, indicating that it is explored and sum up the weight
            V.add(u)
            total_weight += weight
            #C Check all the neighbours of u and push them on the heap if unexplored
            for n,cost in G[u]:
                if n not in V:
                    heapq.heappush(Q,(cost,n))

    return total_weight

def run():
    G = parse_data()
    print(prim(G,1))

run()








#END
