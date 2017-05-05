from getDomSet import *
from prune import *
import programIO
import networkx as nx

infile      = programIO.parseCommandLineArgs()
graph  = programIO.readGraph(infile)
sortList(graph)
dom_set = set()
G = nx.Graph()
for node in graph:
	for neighbor in node.neighborList:
		G.add_edge(node.nodeID, neighbor)

while not nx.is_dominating_set(G, list(dom_set)):
	removal_node = highestDegNode(graph)
	dom_set.add(removal_node.nodeID)
	indx = findNodeIndex(graph, removal_node.nodeID)
	removed_list = [removal_node]
	for neigh in removal_node.neighborList:
		dom_set.add(neigh)
		indx = findNodeIndex(graph, neigh)
		removed_list.append(findNode(graph, neigh))

	for node in removed_list:
		del graph[findNodeIndex(graph, node.nodeID)]
		propogateNodeRemoval(node, graph)	
	
print('Found dominating set of size ' + str(len(dom_set)))
