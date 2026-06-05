class Graph:
    def __init__(self,bidirection=True):
        num_nodes, num_edges = map(int,input().split())
        self.graph = [[] for _ in range(num_nodes+1)]
        for _ in range(num_edges):
            u,v = map(int,input().split())
            self.graph[u].append(v)
            if bidirection:
                self.graph[v].append(u)
        self.visited = []
    def dfs(self, node):
        print(node, end=' ')
        self.visited.append[node]
        for adj_node in self.graph(node):
            if adj_node not in self.visited:
                self.dfs(adj_node)
if __name__ == '__main__':
    g = Graph(bidirection=False)
    start = int(input())
    g.dfs()