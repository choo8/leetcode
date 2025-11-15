from collections import defaultdict


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        edge_counts = defaultdict(int)

        for u, v in edges:
            edge_counts[u] += 1
            edge_counts[v] += 1

        if edge_counts[u] == len(edges):
            return u
        elif edge_counts[v] == len(edges):
            return v


if __name__ == "__main__":
    solution = Solution()

    edges = [[1,2],[2,3],[4,2]]
    assert solution.findCenter(edges) == 2

    edges = [[1,2],[5,1],[1,3],[1,4]]
    assert solution.findCenter(edges) == 1
