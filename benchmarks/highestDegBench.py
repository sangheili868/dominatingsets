from getDomSet import *
from prune import *
import programIO
import networkx as nx

infile = programIO.parseCommandLineArgs()
graph  = programIO.readGraph(infile)
sortList(graph)
dom_set = set()
G = nx.Graph()
for node in graph:
	for neighbor in node.neighborList:
		G.add_edge(node.nodeID, neighbor)



while len(graph) != 0:
	removal_node = highestDegNode(graph)
	dom_set.add(removal_node.nodeID)
	removed_list = [removal_node]
	for neigh in removal_node.neighborList:
		removed_list.append(findNode(graph, neigh))
	for node in removed_list:
		del graph[findNodeIndex(graph, node.nodeID)]
		propogateNodeRemoval(node, graph)	
	
print('Found dominating set of size ' + str(len(dom_set)))
