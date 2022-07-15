"""
Algorithm:
1. Add the starting vertex with a distance of 0 to a queue.
2. Start a loop that runs while the queue is not empty.
3. Pop the first element from the queue and label it as "curr_vertex."
4. Mark curr_vertex as visited.
5. Finalize the distance of curr_vertex from the starting vertex with the
distance it was popped from the queue with. Label this distance as "dist."
6. Iterate over all the adjacent vertices of the current vertex. Add all 
adjacent vertices that have not yet been visited to the queue with a distance of
dist+1.
7. Repeat from step 2 until the queue is empty or we have visted each vertex 
once.
"""

"""
Time Complexity: O(|V| + |E|)
"""

def bfs_reachables_vertices(graph: dict, start) -> dict:
    """
    Finds all reachable nodes from the start vertex as well as their respective
    shortest path from the start vertex.
    @param graph: The graph (adjacency list) we are searching within.
    @param start: Node to start the search from.
    @return: All nodes reachable from the start vertex as well as their 
    respective shortest path from the start vertex. Return an empty dict if
    the start vertex is not in graph.
    """

    if start not in graph:
        return {}
        
    queue = [(start, 0)]
    # Target distance remains None as long as no path to target is found.
    dist_from_start = {}   
    visited_vertices = set()
    
    while queue:
        curr_vertex, dist = queue.pop(0)

        if curr_vertex not in visited_vertices:
            visited_vertices.add(curr_vertex)
            # Finalizing the distance for curr_vertex.
            dist_from_start[curr_vertex] = dist

            # If we've visited each vertex we are done.
            if len(visited_vertices) == len(graph):
                break

            # Adding each unvisited adj_vertex to the queue.
            for adj_vertex in graph[curr_vertex]:
                if adj_vertex not in visited_vertices:
                    queue.append((adj_vertex, dist + 1))

    return dist_from_start

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

bfs_reachables_vertices(graph, 'D')
{'D': 0}

bfs_reachables_vertices(graph, 'Z')
{}

bfs_reachables_vertices(graph, 'A')
{'A': 0, 'B': 1, 'D': 2, 'F': 2, 'H': 3}
"""

"""
Notes:
- Implemented using a queue.
- Works on directed and undirected graphs.
- Finds the shortest path in unweighted graphs.
- This specific implementation finds all nodes reachable from a starting vertex
as well as the shortest paths to all the reachables vertices from the starting
vertex.
"""