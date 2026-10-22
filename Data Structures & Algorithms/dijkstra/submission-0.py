from typing import List, Dict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(n)}
        dist[src] = 0
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist