AddVertex()
  Adds a new vertex to the graph
  Takes in the value of that vertex
  Returns the added vertex
AddEdge()
  Adds a new edge between two nodes in the graph
  Include the ability to have a “weight”
  Takes in the two nodes to be connected by the edge
  Both nodes should already be in the Graph
GetNodes()
  Returns all of the nodes in the graph as a collection (set, list, or similar)
GetNeighbors()
  Returns a collection of nodes connected to the given node
  Takes in a given node
  Include the weight of the connection in the returned collection


# Tests
1. Node can be successfully added to the graph
2. An edge can be successfully added to the graph
3. A collection of all nodes can be properly retrieved from the graph
4. All appropriate neighbors can be retrieved from the graph
5. Neighbors are returned with the weight between nodes included
6. The proper size is returned, representing the number of nodes in the graph
7. A graph with only one node and edge can be properly returned
8. An empty graph properly returns null