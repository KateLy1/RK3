#Дан граф в виде списка вершин. Необходимо понять, есть ли
#в этом графе цикл

def dfs(graph, vertex, parent, visited):
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, vertex, visited):
                return True
    return False

def has_cycle(graph):
    visited = []
    for vertex in graph:
        if vertex not in visited:
            if dfs(graph, vertex, None, visited):
                return True
    return False

import unittest

class TestHas_cycle(unittest.TestCase):

    def test1(self):
        self.assertFalse(has_cycle({0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}))

    def test2(self):
        self.assertTrue(has_cycle({0: [1, 2], 1: [0, 2], 2: [0, 1]}))

    def test3(self):
        self.assertFalse(has_cycle({}))

    def test4(self):
        self.assertTrue(has_cycle({0: [1], 1: [0, 2], 2: [1, 0], 3: [4], 4: [3]}))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
