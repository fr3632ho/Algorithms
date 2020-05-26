import sys, copy, time
from collections import defaultdict, deque

nbr_nodes, nbr_edges, min_tot_flow, nbr_routes, routes_to_remove, source, sink, capacities, graph, mid, max_flow, last_valid = [0]*12


class Graph:  # A residual graph

    def __init__(self):
        self.nodes = defaultdict(dict)
        self.index_of_index = {}
        self.edges_by_index = defaultdict(list)
        self.edge_count = 0
        self.opposite_edges = {}

    def add_edge(self, start, stop, capacity):
        edge1 = self.Edge(start, stop, capacity)
        edge2 = self.Edge(stop, start, capacity)
        self.nodes[start].update({self.edge_count : edge1})
        self.nodes[stop].update({self.edge_count : edge2})
        self.edges_by_index[self.edge_count] = (edge1, edge2)

        self.opposite_edges[edge1] = edge2
        self.opposite_edges[edge2] = edge1
        self.edge_count += 1

    def get_opposite_edge(self, edge):
        return self.opposite_edges[edge]

    def remove_edge(self, index): # För hög komplexitet, byta listorna av edge1 o edge2 så vi kan indexera och ta bort
        edges = self.edges_by_index[index]
        del self.nodes[edges[0].start][index]
        del self.nodes[edges[1].start][index]
        self.edge_count -= 1

    def remove_up_to(self, nbr_edges):
        for i, route_index in enumerate(routes_to_remove):
            if i == nbr_edges:
                break
            self.remove_edge(route_index)

    def reset_graph(self):  # För hög komplexitet tror jag
        for edges in graph.nodes.values().values():
            for edge in edges:
                edge.flow = 0

    def get_max_flow(self):
        max_flow = 0
        while path := bfs(self, source, sink):
            self.update_flow(path)
            max_flow = self.calculate_max_flow()

        return max_flow

    def calculate_max_flow(self):
        return sum([edge.flow for edge in self.nodes[source].values()]) + sum(
            [self.get_opposite_edge(edge).flow for edge in self.nodes[source].values()])

    def update_flow(self, path):
        min_capacity = sys.maxsize

        for edge in path:
            if (edge.capacity - edge.flow) < min_capacity:  # Här va felet, stod edge.capacity, och inte capacity - flow
                min_capacity = edge.capacity - edge.flow  # Samma här

        for edge in path:
            edge.flow += min_capacity
            self.get_opposite_edge(edge).capacity -= min_capacity

    def connected_edges(self, current_edge):
        return self.nodes[current_edge.stop].values()

    class Edge:

        def __init__(self, start, stop, capacity):
            self.start = start
            self.stop = stop
            self.capacity = capacity
            self.predecessor = None
            self.flow = 0




def parse_data(data):
    global nbr_nodes, nbr_edges, min_tot_flow, nbr_routes, routes_to_remove, source, sink, graph

    data_list = data.strip().replace('\n', ' ').split()
    data_list = [int(i) for i in data_list]
    nbr_nodes, nbr_edges, min_tot_flow, nbr_routes = data_list[:4]

    graph = Graph()
    routes_to_remove = []

    for i in range(4, len(data_list) - nbr_routes, 3):
        graph.add_edge(data_list[i], data_list[i + 1], data_list[i + 2])

    routes_to_remove = data_list[len(data_list) - nbr_routes:]
    source = 0
    sink = nbr_nodes - 1


def backtrack_route(current_edge):
    path = [current_edge]
    while current_edge.predecessor:
        path.append(current_edge.predecessor)
        current_edge = current_edge.predecessor
    return path


def is_full(edge):
    return edge.capacity <= edge.flow


def bfs(graph, start, end):
    if source == sink or graph.edge_count == 0:
        return
    edges_visited = {}
    for node in graph.nodes:
        for edge in graph.nodes[node].values():
            edges_visited[edge] = False  # O(n)

    # edges_visited[graph.nodes[source]] = True
    edges_to_visit = deque([edge for edge in graph.nodes[source].values() if not is_full(edge)])
    for edge in graph.nodes[source].values():
        edges_visited[edge] = True

    while edges_to_visit:
        current_edge = edges_to_visit.pop()
        if current_edge.stop == sink:
            return backtrack_route(current_edge)
        for neighboring_edge in graph.connected_edges(current_edge):  # O(n)
            if not edges_visited[neighboring_edge] and not is_full(neighboring_edge):
                edges_to_visit.appendleft(neighboring_edge)
                neighboring_edge.predecessor = current_edge  # setting predecessor for backtracking
                edges_visited[neighboring_edge] = True
                edges_visited[graph.get_opposite_edge(neighboring_edge)] = True
                if neighboring_edge.stop == sink:
                    return backtrack_route(neighboring_edge)


def get_sample_data():
    file = open("./data/secret/2med.in")
    return file.read()


def get_data():
    file = sys.stdin
    return file.read()

def binary_search_flow(initial_graph, left, right):
    global mid, max_flow, last_valid
    if right >= left:
        mid = left + (right - left) // 2
        copied_graph = copy.deepcopy(initial_graph)
        copied_graph.remove_up_to(mid)
        max_flow = copied_graph.get_max_flow()
        if max_flow >= min_tot_flow:
            last_valid = (mid, max_flow)
            return binary_search_flow(initial_graph, mid + 1, right)
        else:
            return binary_search_flow(initial_graph, left, mid - 1)
    else:
        return last_valid

def main():
    data = get_sample_data()
    parse_data(data)
    routes_removed, max_flow = binary_search_flow(graph, 0, len(routes_to_remove))

    print(routes_removed, max_flow)

if __name__ == '__main__':
    main()
