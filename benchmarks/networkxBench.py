import programIO
import networkx as nx

if __name__ == "__main__":
	infile      = programIO.parseCommandLineArgs()
	init_graph  = programIO.readGraph(infile)
	
	G = nx.Graph()
	for node in init_graph:
		for neighbor in node.neighborList:
			G.add_edge(node.nodeID, neighbor)
	
	print('networkx can do it in ' + str(len(nx.dominating_set(G))))
	

