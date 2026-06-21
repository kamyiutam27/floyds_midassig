import unittest
import recursive_floyd
from iterative_floyd import *
from sys import maxsize




class TestFloydWarshall(unittest.TestCase):

    def test_recursive_floyd(self):
        """Testing other group of number"""
        recursive_floyd.GRAPH = [
            [0, 5, NO_PATH, 10],
            [NO_PATH, 0, 3, NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

        recursive_floyd.recursive_floyd_warshall(0, 0, 0)
        result = (recursive_floyd.GRAPH)

        expected = [
            [0, 5, 8, 9],
            [NO_PATH, 0, 3, 4],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(result, expected)


    def test_recursive_floyd2(self):
        """Testing the expansion of a group of numbers."""
        recursive_floyd.GRAPH = [
            [0, 4, NO_PATH, 10, NO_PATH],
            [NO_PATH, 0, 3, NO_PATH, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2, 8],
            [NO_PATH, NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        recursive_floyd.MAX_LENGTH = len(recursive_floyd.GRAPH[0])
        recursive_floyd.recursive_floyd_warshall(0, 0, 0)
        result = (recursive_floyd.GRAPH)

        expected = [
            [0, 4, 7, 9, 10],
            [NO_PATH, 0, 3, 5, 6],
            [NO_PATH, NO_PATH, 0, 2, 3],
            [NO_PATH, NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()