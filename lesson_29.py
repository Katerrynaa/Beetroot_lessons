# Імплементуйте зважений направлений граф (directed weighted graph) з пошуком найкоротшого шляху між двома заданими вертексами (нодами). 

class MyGraph:
    def __init__(self, edges, n):
        self.adjList = [None] * n

        for s in range(n):
            self.adjList[s] = []
 
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
 
def printGraph(graph):
    for src in range(len(graph.adjList)):
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()
 
 
if __name__ == '__main__':
    edges = [(0, 3, 6), (1, 2, 4), (3, 2, 7), (5, 2, 8), (3, 6, 9),
            (4, 3, 0), (5, 2, 1)]
 
    n = 7
    graph = MyGraph(edges, n)
    printGraph(graph)