import programIO
import prune
import getDomSet
import makeConnected
import networkx as nx
import networkx.algorithms.approximation as nxaa
from dominatingsets import *

if __name__ == "__main__":
	infile      = programIO.parseCommandLineArgs()
	init_graph  = programIO.readGraph(infile)

		
	#Double check it's a dominating set with networkx
	G = nx.Graph()
	for node in init_graph:
		for neighbor in node.neighborList:
			G.add_edge(node.nodeID, neighbor)
	
	d = DominatingSets()	
	print('networkx can do it in ' + str(len(nxaa.min_weighted_dominating_set(G))))
	#print('this paper can do it in ' + str(len(DominatingSets.min_connected_dominating_sets_non_distributed(G))))
	

