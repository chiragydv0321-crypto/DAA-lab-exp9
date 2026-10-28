"""
Experiment 9: Graphs and Dynamic Programming
Program 1: Prim's Minimum Spanning Tree
Aim: Find the total weight of a minimum spanning tree using Prim's algorithm.
"""

def prim_mst(graph, start=0):
    n = len(graph)
    selected = [False] * n
    selected[start] = True
    total, edges = 0, []
    for _ in range(n - 1):
        best = None
        for u in range(n):
            if selected[u]:
                for v in range(n):
                    w = graph[u][v]
                    if not selected[v] and w > 0 and (best is None or w < best[0]):
                        best = (w, u, v)
        if best is None:
            return None, edges
        w, u, v = best
        selected[v] = True
        total += w
        edges.append((u, v, w))
    return total, edges

g = [[0, 2, 0, 6], [2, 0, 3, 8], [0, 3, 0, 0], [6, 8, 0, 0]]
print(prim_mst(g))
