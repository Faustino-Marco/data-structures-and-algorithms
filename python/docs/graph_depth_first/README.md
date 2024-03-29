# Depth-First Traversal of a Graph

## Challenge
Extending an Implementation: Write a depth-first method for the graph class

## Approach & Efficiency
Added code for DFS:

'''Python

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

'''

## API
<!-- Description of each method publicly available in your Graph -->
Name: Depth first
Arguments: Node (Starting point of search)
Return: A collection of nodes in their pre-order depth-first traversal order
Program output: Display the collection