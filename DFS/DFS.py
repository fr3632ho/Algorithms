from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def print_relations(self):
        for x in self.graph:
            print(str(x) + " " + str(self.graph[x]))

    def dfsHelper(self,v,visited):
        visited[v] = True
        print(v, end = ' ')
        for x in self.graph[v]:
            if not visited[x]:
                self.dfsHelper(x,visited)

    #handels a disconnected graph
    def DFSdisc(self):
        V = len(self.graph)
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                self.dfsHelper(i,visited)

    def DFS(self,v):
        visited = [False] * (len(self.graph))
        self.dfsHelper(v,visited)




graph = Graph()

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(3,3)
graph.add_edge(4,4)
graph.print_relations()

print("Starting position is node 1 ")
graph.DFS(2)
print()
graph.DFSdisc()
