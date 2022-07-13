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
7. Repeat from step 2 until the queue is empty or the target vertex is found.
"""

"""
Time Complexity: O(|V| + |E|)
"""

def bfs_shortest_path(graph: dict, start, target) -> int:
    """
    Finds the shortest path between the start and target node.
    @param graph: The graph (adjacency list) we are searching within.
    @param start: Node to start the search from.
    @param target: Node to find the shortest to.
    @return: The shortest path from the start node to the target node, or None
    if no such path exists.
    """

    queue = [(start, 0)]
    # Target distance remains None as long as no path to target is found.
    dist_from_start = {target: None}   
    visited_vertices = set()
    
    while queue:
        curr_vertex, dist = queue.pop(0)

        # Terminate computation if target vertex is reached.
        if curr_vertex == target:
            return dist
        elif curr_vertex not in visited_vertices:
            visited_vertices.add(curr_vertex)
            # Finalizing the distance for curr_vertex.
            dist_from_start[curr_vertex] = dist

            # Adding each unvisited adj_vertex to the queue.
            for adj_vertex in graph[curr_vertex]:
                if adj_vertex not in visited_vertices:
                    queue.append((adj_vertex, dist + 1))

    # If reached, no path exists.
    return dist_from_start[target]

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

bfs_shortest_path(graph, 'A', 'A')
@return: 0

bfs_shortest_path(graph, 'A', 'B')
@return: 1

bfs_shortest_path(graph, 'A', 'H')
@return: 3

bfs_shortest_path(graph, 'H', 'A')
@return: None
"""

"""
Notes:
- Implemented using a queue.
- Works on directed and undirected graphs.
- Finds the shortest path in unweighted graphs.
- This specific implementation finds the shortest path from a start vertex to
a target vertex.
"""

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