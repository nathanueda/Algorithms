"""
Algorithm:
1. Add the starting vertex to a stack.
2. Start a loop that runs while the stack is not empty.
3. Pop the first element from the stack and label it as "curr_vertex."
4. Mark curr_vertex as visited.
5. Iterate over all the adjacent vertices of the current vertex. Add all 
adjacent vertices that have not yet been visited to the stack.
6. Repeat from step 2 until the stack is empty or we have visted each vertex 
once.
"""

"""
Time Complexity: O(|V| + |E|)
"""

def dfs_reachables_vertices(graph: dict, start) -> dict:
    """
    Finds all reachable vertices from a given start vertex.
    @param graph: The graph (adjacency list) we are searching within.
    @param start: Node to start the search from.
    @return: All nodes reachable from the start vertex. Return an empty dict if
    the start vertex is not in graph.
    """

    if start not in graph:
        return {}

    stack = [start]
    # Any vertex visited is reachable.
    visited_vertices = set()

    while stack:
        curr_vertex = stack.pop()
        if curr_vertex not in visited_vertices:
            visited_vertices.add(curr_vertex)

            # If we've visited each vertex we are done. 
            if len(visited_vertices) == len(graph):
                break
            
            # Adding each unvisited adj_vertex to the stack.
            for adj_vertex in graph[curr_vertex]:
                if adj_vertex not in visited_vertices:
                    stack.append(adj_vertex)
            
    return visited_vertices

"""
Examples:
graph = {
    'A': ['B'],
    'B': ['D', 'F'],
    'C': ['A', 'B', 'G'],
    'D': [],
    'E': ['G', 'H'],
    'F': ['D', 'H'],
    'G': ['C', 'H'],
    'H': ['F']
    }

dfs_reachables_vertices(graph, 'D')
{'D'}

dfs_reachables_vertices(graph, 'Z')
{}

dfs_reachables_vertices(graph, 'A')
{'A', 'B', 'D', 'F', 'H'}
"""

"""
Notes:
- Implemented using a stack.
- Works on directed and undirected graphs.
- Finds a path between two vertices but one that is not necessarily the shortest 
path.
"""