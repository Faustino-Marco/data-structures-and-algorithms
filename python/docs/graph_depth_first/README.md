# Breadth-First Traversal of a Graph

## Challenge
Extending an Implementation: Write a function called business trip

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

Arguments: graph, array of city names
Return: the cost of the trip (if it’s possible) or null (if not)