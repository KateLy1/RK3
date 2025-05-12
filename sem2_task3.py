#Является ли граф деревом
def isTree(graph, start):
    visited = []
    queue = [start]
    parent = {start: None}
    
    while queue:
        vertex = queue.pop()
        visited.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent[vertex] != neighbor:
                    return False
    
    return len(visited) == len(graph)


import unittest

class TestIsTree(unittest.TestCase):

    def test1(self):
        self.assertTrue(isTree({'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}, 'A'))

    def test2(self):
        self.assertFalse(isTree({'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}, 'A'))

    def test3(self):
        self.assertFalse(isTree({'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C']}, 'A'))

    def test4(self):
        self.assertTrue(isTree({'A': []}, 'A'))
        
    def test5(self):
        self.assertFalse(isTree({}, None))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
