# BFS taversal for a graph
from __future__ import print_function
from collections import defaultdict 

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  # function for printing the BFS of a graph

  def BFS(self, s):  # Here s is the starting vertex for traversal.
    # marking all vertices as not visited
    visited = [False] * len(self.graph)
    
    queue = []  # FIFO - first in first out
    
    queue.append(s)
    visited[s] = True

    while queue:
      # deQueue a vertex from Queue and print
      s = queue.pop(0)
      print(s, end=" ")
      
      for i in self.graph[s]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True 
     

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

print("Breadth first traversal -->")
g.BFS(2)