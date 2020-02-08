# Graphs module
## Introduction
This is a python module that allows you to quickly create data structures for directed and undirected graphs, based on number of vertexes and specified edges.
## Functions
* create_adjacency_matrix(vec_num, edges, directed=True)  
  returns a two-dimensional list of size vec_num×vec_num
* create_incidence_matrix(vec_num, edges, directed=True)  
  returns a two-dimensional list of size vec_num×len(edges)
* create_adjacency_list(vec_num, edges, directed=True)  
  returns a two-dimensional list of length vec_num
## Arguments
* vec_num - number of vertexes (nodes)
* edges - all edges between vertexes (nodes) in form List<List<int, int>>, eg. [[0, 1], [0, 2], [1,2]]. For directed graph, a first element of each inside list is a starting vertex and the second one is the ending vertex.
* directed - if graph is directed this should be True, if undirected False
