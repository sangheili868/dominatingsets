import programIO
import prune
import getDomSet

if __name__ == "__main__":
	infile      = programIO.parseCommandLineArgs()
	init_graph  = programIO.readGraph(infile)
	curr_graph  = init_graph[:]
	tot_dom_set = set()
	TMP_FILE    = 'tmp_graph_file.in'
	iterations = 0	

	while len(curr_graph) != 0:
		iterations += 1
		print('Begining iteration ' + str(iterations))
		
		saveToFile(curr_graph, TMP_FILE)
		GDV = programIO.calcGDVs(TMP_FILE)
		dom_set_additions = getDomSet.getDomSetNodes(curr_graph, GDV)
		tot_dom_set = tot_dom_set.union(dom_set_additions)
		curr_graph = prune.pruneGraph(init_graph, curr_graph, tot_dom_set)

		'''
		Is this removeDuplicates written? It would be much better if we didn't have to read and write from a file
		'''
		removeDuplicates(numNodes,numEdges,'temp.el','iteration.el')
