# DFS taversal for a graph
from __future__ import print_function
from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def DFShelper(self, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    #recurring for adjacent vertices 
    for i in self.graph[v]:
      if visited[i] == False:
        self.DFShelper(i, visited)
        
  def DFS(self, v): # v is the starting vertex here 
    visited = [False] * len(self.graph)
    
    self.DFShelper(v,visited)

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.DFS(2)