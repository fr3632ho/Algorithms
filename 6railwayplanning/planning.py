import sys
from collections import defaultdict,deque

'''
Finds the path from the sink to the parent of the parents
'''
def findPath(node, parents):
    path = deque([node])
    root = node
    while parents[root] != -1:
        root = parents[root]
        path.appendleft(root)
    return path

'''
Shortest path BFS for now, this will be needed for the lab
'''
def BFS(G,source,sink,N):
    if source == sink:
        return []
    discovered,queue = {source}, deque([source])

    paths = []
    parents = [-1]*N

    while queue:

        node = queue.pop();

        if node == sink:
            paths.append(findPath(node,parents))
            continue

        discovered.add(node)
        for neighbour in G[node]:
            if neighbour[1] not in discovered:
                # Set parent
                parents[neighbour[1]] = node
                queue.appendleft(neighbour[1])

    return paths

if __name__ == "__main__":
    # Parsing of data
    data = [[int(i) for i in line.strip('\n').split()] for line in sys.stdin]
    N,M,C,P = data[0]
    source = sink = 0
    G = defaultdict(list)
    for j,i in enumerate(data[1:M+1]):
        if j == 0:
            source = i[0]
        if j == M-1:
            sink = i[0]
        G[i[0]].append((i[2],i[1]))
        G[i[1]].append((i[2],i[0]))
    paths = [i[0] for i in data[M+1:]]

    found_paths = BFS(G,source,sink,N)

    print('Found paths, with condition that stepping back to a discovered node is prohibited')
    for path in found_paths:
        print(list(path))

    print('\nNodes: {}\nEdges: {}\nStudents: {}\nPaths to remove: {}\nSource: {}\nSink: {}\n'.format(N,M,C,paths,source,sink))
    print("Graph containig:")
    [print(f'Node {i} => {G[i]}') for i in G]
