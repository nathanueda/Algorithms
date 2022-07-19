"""
Algorithm:
1. Loop through each vertex setting the distance to infinity.
2. Add the starting vertex with a distance of 0 to a priority queue (pq). 
3. Start a loop that runs while the pq is not empty.
4. Pop the first element from the pq and label it as "curr_vertex."
5. Mark curr_vertex as visited.
6. Finalize the distance of curr_vertex from the starting vertex with the
distance it was popped from the pq with. Label this distance as "dist."
7. Iterate over all the adjacent vertices of the current vertex, labeled 
"adj_vertex" and label the distance between curr_vertex and adj_vertex as 
"edge_weight."
8. If dist + edge_weight < the current distance in adj_vertex (adj_dist)
    - update adj_dist = dist + edge_weight
    - adj_prev = curr_vertex
    - add (adj_dist, adj_vertex) to the pq.
9. Repeat from step 3 until the pq is empty or we have visited each vertex 
once.
"""

"""
Time Complexity: O(|V| + |E|log|E|)
"""

import heapq
import math

def dijkstras_shortest_path(graph: dict, start) -> dict:
    """
    Finds the shortest path between the start and all reachable vertices within
    the graph.
    @param graph: The weighted graph (adjacency list) we are searching within.
    @param start: Node to start the search from.
    @return: All nodes reachable from the start vertex as well as their 
    respective shortest path from the start vertex. Return an empty dict if
    the start vertex is not in graph.
    """

    if start not in graph:
        return {}

    visited = set()
    prev = {}
    dist_from_start = {}
    final_dist = {start: 0}
    
    for vertex in graph:
        if vertex == start:
            dist_from_start[vertex] = 0
        else:
            dist_from_start[vertex] = math.inf
    
    pq = [(0, start)]

    while pq:
        # Min-heap prioritized by first item in tuple by default.
        dist, curr_vertex = heapq.heappop(pq)

        if curr_vertex not in visited:
            visited.add(curr_vertex)

            # If we've visited each vertex we are done.
            if len(visited) == len(graph):
                break

            for adj_vertex, edge_weight in graph[curr_vertex]:
                if dist + edge_weight < dist_from_start[adj_vertex]:
                    dist_from_start[adj_vertex] = dist + edge_weight
                    final_dist[adj_vertex] = dist + edge_weight
                    prev[adj_vertex] = curr_vertex
                    heapq.heappush(pq, 
                    (dist_from_start[adj_vertex], adj_vertex))
    
    return final_dist

"""
Examples:
graph = {
    'A': [('D', 3), ('C', 6), ('B', 1)],
    'B': [('C', 4)],
    'C': [],
    'D': [('C', 1)]
}

dijkstras_shortest_path(graph, 'A')
{'A': 0, 'B': 1, 'C': 4, 'D': 3}

dijkstras_shortest_path(graph, 'F')
{}

dijkstras_shortest_path(graph, 'C')
{'C': 0}

dijkstras_shortest_path(graph, 'B')
{'B': 0, 'C': 4}
"""

"""
Notes:
- Implemented using a priority queue.
- The element with the highest priority is the one with the lowest distance.
- Works on directed and undirected graphs.
- Finds the shortest path in a weighted graph where all the weights are non-
negative.
- Can have multiple instances of the same vertex in the priority queue at once.
"""