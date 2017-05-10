import programIO
import getDomSet
import prune

if __name__ == "__main__":
	infile      = programIO.parseCommandLineArgs()
	init_graph  = programIO.readGraph(infile)
	curr_graph  = init_graph[:]
	tot_dom_set = set()
	TMP_FILE    = 'tmp_graph_file.el'
	iterations = 0	
	last_num_nodes = 0

	while len(curr_graph) != 0:
		iterations += 1
		print('Begining iteration ' + str(iterations))
		
		programIO.writeGraph(curr_graph, TMP_FILE)
		GDV = programIO.calcGDVs(TMP_FILE)
		dom_set_additions, init_graph = getDomSet.getDomSetNodes(curr_graph, init_graph, GDV)
		tot_dom_set = tot_dom_set.union(dom_set_additions)
		curr_graph, last_num_nodes, tot_dom_set = prune.pruneGraph(init_graph, curr_graph, tot_dom_set, last_num_nodes)
	
        print('Size of domset is ' + str(len(tot_dom_set)))

