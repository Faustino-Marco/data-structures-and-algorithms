from data_structures.queue import Queue


class Graph:
    """
    add node
    Arguments: value
    Returns: The added node
    Add a node to the graph

    add edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph
    If specified, assign a weight to the edge
    Both nodes should already be in the Graph

    get nodes
    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)
    Empty collection returned if there are no nodes

    get neighbors
    Arguments: node
    Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection
    Empty collection returned if there are no nodes
    
    size
    Arguments: none
    Returns the total number of nodes in the graph
    0 if there are none
    """
    def __init__(self):
        pass
        # initialization here
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        return len(self._adjacency_list)

    def get_nodes(self):
        return list(self._adjacency_list.keys())

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()
        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def breadth_first(self, vertex):
        all_vertices = []
        breadth = Queue()
        visited_vertices = []
        breadth.enqueue(vertex)
        visited_vertices.append(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            all_vertices.append(front.value)
            print(all_vertices)

            for edge in self.get_neighbors(front):
                
                if edge.vertex not in visited_vertices:
                    visited_vertices.append(edge.vertex)
                    breadth.enqueue(edge.vertex)
        return all_vertices

    def depth_first_search(self, start):
        def pre_order(vertex, collection=[], visited=set()):
            if not vertex or vertex not in self._adjacency_list or vertex in visited:
                return collection
            collection.append(vertex.value)
            visited.add(vertex)
            edge_list = self._adjacency_list[vertex]
            for edge in edge_list:
                pre_order(edge.vertex, collection, visited)
            return collection

        return pre_order(start)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight