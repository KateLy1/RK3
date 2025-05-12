#Дан неориентированный граф. Необходимо написать
#функцию, которая вернет true, если граф является двудольным. 
# Вариант 1. BFS
def isBipartite(graph):
    n = len(graph)
    colors = n * [0]
    
    def bfs(start):
        queue = [start]
        colors[start] = 1
        while queue:
            node = queue.pop()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True
    
    for i in range(n):
        if colors[i] == 0:
            if not bfs(i):
                return False
    return True

import unittest

class TestIsBipartite(unittest.TestCase):
    def test1(self):
        self.assertTrue(isBipartite([]))
    
    def test2(self):
        self.assertTrue(isBipartite([[1,3], [0,2], [1,3], [0,2]]))
    
    def test3(self):
        self.assertFalse(isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
    
    def test4(self):
        self.assertTrue(isBipartite([[1], [0], [3], [2], [5], [4]]))
    
    def test5(self):
        self.assertFalse(isBipartite([[1,2], [0,2], [0,1], [4], [3]]))
    
    def test6(self):
        self.assertTrue(isBipartite([[1], [0,2], [1,3], [2,4], [3,5], [4]]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Вариант 2. DFS
def isBipartite(graph):
    n = len(graph)
    colors = [0] * n
    
    def dfs(node, c):
        colors[node] = c
        for neighbor in graph[node]:
            if colors[neighbor] == 0:
                if not dfs(neighbor, -c):
                    return False
            elif colors[neighbor] == colors[node]:
                    return False
        return True

    for i in range(n):
        if (colors[i] == 0):
            if not dfs(i, 1):
                return False
    return True

import unittest

class TestIsBipartite(unittest.TestCase):
    def test1(self):
        self.assertTrue(isBipartite([]))
    
    def test2(self):
        self.assertTrue(isBipartite([[1,3], [0,2], [1,3], [0,2]]))
    
    def test3(self):
        self.assertFalse(isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
    
    def test4(self):
        self.assertTrue(isBipartite([[1], [0], [3], [2], [5], [4]]))
    
    def test5(self):
        self.assertFalse(isBipartite([[1,2], [0,2], [0,1], [4], [3]]))
    
    def test6(self):
        self.assertTrue(isBipartite([[1], [0,2], [1,3], [2,4], [3,5], [4]]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
