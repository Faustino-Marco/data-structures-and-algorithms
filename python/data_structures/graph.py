class Graph:
    """
    Put docstring here
    """


    def __init__(self):
        # initialization here
        self.adjacency_list = {}


    def add_node(self, value):
        # method body here
        return Vertex(value)
    

    def what(self, vertex):
        # get the vertex/mode in the graph
        self.adjacency_list[vertex] = []
        return vertex


    def size(self):
        return len(self.adjacency_list)


    def get_nodes(self):
        return self.adjacency_list.keys()
    

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)


    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value
    
class Edge:
    def __init__(self, vertex, weight):
        pass
