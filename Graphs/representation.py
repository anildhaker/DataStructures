from __future__ import print_function

class AdjNode:
  def __init__(self, data):
    self.vertex = data
    self.next = None
    
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [None] * self.V
    
  # function to add an edge in undirected graph
  def add_edge(self, src, dest):
    node = AdjNode(dest)
    node.next = self.graph[src]
    self.graph[src] = node
    
    node = AdjNode(src)
    node.next = self.graph[dest]
    self.graph[dest] = node
  
  def print_Graph(self):
    for i in range(self.V):
      #adjaceny list of vertex i
      print("Adjacency Nodes of Vertex {}".format(i),end=" ")
      temp = self.graph[i]
      while temp:
        print("--> {}".format(temp.vertex), end=" ")
        temp = temp.next
      print()

V = 5
graph = Graph(V) 
graph.add_edge(0, 1) 
graph.add_edge(0, 4) 
graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(1, 4) 
graph.add_edge(2, 3) 
graph.add_edge(3, 4) 

graph.print_Graph()
