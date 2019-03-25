# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
  
import sys

class Graph():
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
  
  # function to calculate minDistance of vertex from the set which are not yet included
  # in shortest path tree set (sptSet):

  def minDistance(self, dist, sptSet):
    
    min = sys.maxsize

    for v in range(self.V):
      if dist[v] < min and sptSet[v] == False:
        min = dist[v]
        min_index = v
    return min_index


  def dijkstra(self, src):
    dist = [sys.maxsize] * self.V
    dist = src[0]
    sptSet = [False] * self.V
    
    for cout in range(self.V):

      u = self.minDistance(dist, sptSet)
      
      sptSet[u] = True

      for v in range(self.V): 
          if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                dist[v] = dist[u] + self.graph[u][v]