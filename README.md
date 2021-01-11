# directed weighted graph 

![Graph](https://user-images.githubusercontent.com/41864040/104228878-20404100-5454-11eb-9904-0e4572065ce9.png)

### about the project 
In this project i made a data structure of a directed weighted graph in python.
I also made some methods that you can run on this project, like the shortest path between two nodes,
 connected components of a given node and more.

## Classes

##### DiGraph

This class implements the GraphInterface interface. 
This class have the following methods:

**get_all_v** return a collection of all the nodes in the graph.

**all_in_edges_of_node** return a collection of all the nodes that are pointing to this node.

**all_out_edges_of_node** return a collection of all the nodes that this node pointing to.

**add_node** adds a node to the graph, if the node already exist doesn't add it. returns true if successfully added the 
node else false.
 
**add_edge** add an edge from node1 to node2 with a given weight. if an edge already exist between this two nodes nothing happened.
 if an edge is made returns true else false.

**remove_node** removes the node with the associated key from the graph. returns true if successfully removed else false.
 also removes all the edges associates with this node.
  
 
**remove_edge** removes the edge between the two given keys. returns true if successfully removed else false.

**v_size** return the number of the nodes in this graph.

**e_size** return the number of edges in this graph.

**get_mc** return the number of changes made in this graph.

In this class we have another inner class **Node**.
 This class represent the nodes that our graph is made from.
  
#### GraphAlgo

This class implements the GraphAlgoInterface interface. in this class we have the algorithms we can run on our graph,
also in this class we have methods to save and load the graph in json fashion. contains the following methods:

**get_graph** returns the DiGraph which the algorithm works on.

**load_from_json** loads the graph from a file, if successfully loaded returns true else false.

**save_to_json** saves the graph to a file,if successfully saved returns true else false.

**shortest_path** return a tuple of the weight and list of nodes for the shortest path between two nodes, if a path doesnt exist (float('inf'),[]).

**connected_component** return a list of the strongly connected component (SCC) that the node is a part of.

**connected_components** return all the strongly connected component in the graph .

**plot_graph** plots the graph.
