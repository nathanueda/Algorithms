import unittest
from dfs_reachable_vertices import dfs_reachables_vertices

class DFSReachableVerticesTestCase(unittest.TestCase):
    """Tests for dfs_reachable_vertices.py"""

    def test_no_reachable_vertices(self):
        """
        Does the function work if the start vertex has not reachable vertices?
        """
        vertices_reachable = dfs_reachables_vertices(graph, 'D')
        self.assertEqual(vertices_reachable, {'D'})
        
    def test_start_vertex_not_in_graph(self):
        """Does the function work if the start vertex is not in the graph?"""
        vertices_reachable = dfs_reachables_vertices(graph, 'Z')
        self.assertEqual(vertices_reachable, {})
    
    def test_start_vertex_has_adj_vertices(self):
        """
        Does the function work if the start vertex has multiple vertices it can
        reach?
        """
        vertices_reachble = dfs_reachables_vertices(graph, 'A')
        self.assertEqual(vertices_reachble, {'A', 'B', 'D', 'F', 'H'})

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

if __name__ == '__main__':
    unittest.main()