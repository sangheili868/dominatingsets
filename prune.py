def sortNodeList(node_list):
	'''
	Description: Merge sorts in place a list of integers
	Input: list of integers
	Ouput: None
	'''
	if len(alist) > 1:
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]
		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i = i+1
			else:
				alist[k] = righthalf[j]
				j = j+1
			k = k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	

def nodeInList(node_list, node_num):
	'''
	Description: Checks if a node object with id is in the node_list of node id integers in ascending order

	Input: node_list - integer list of node for entire graph sorted with lowest node id at index 0
	       node_num - the id of the node to look for in the node_list

	Output: True if the node_num is found in node_list, false otherwise
	'''
	first = 0
	last = len(node_list) - 1

	while first <= last:
		midpoint = (first + last) // 2
		if node_list[midpoint] == node_num:
			return True
		else:
			if item < node_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1	
	return False

def neigborsDominated(node_list, dom_set_list, node):
	'''
	Description: Determines whether all neighbors of given node are connected to a node in the
	             dominating set

	Input: node_list - list of node objects currently in graph
	       dom_set_list - integer list of node id's currently in dominating set
	       node - node object to check the neihbors of

	Output: returns true if all the neigbors of node_id are connected to the dominating set,
		false otherwise
	'''
	for neighbor_node in node.neighborList:
		if not nodeInList(dom_set_list, neighbor_node):
			return False
	return True

def oneUndominatedNeighbor(node_list, dom_set_list, node):
	'''
	Description: Determines whether all neighbors but one of given node are conected to a node
		     in the dominating set

	Input: node_list - list of node objects currently in graph
	       dom_set_list - integer list of node id's currently in dominating set
	       node - node object to check the neihbors of

	Output: returns true if all the neigbors but one of node_id are connected to the dominating set,
		false otherwise
	'''
	oneConnected = 0
	for neighbor_node in node.neighborList:
		if node_list[neighbor_node].isDominated:
			oneConnected += 1
			if oneConnected > 1:
				return False
	if oneConnected == 1:
		return True
	else:
		return False


def pruneGraph(node_list, dom_set_list):
	'''
	Description: Removes node from node_list if:
			node is in dom_set_list
				OR
		     	node is connected to a node in dom_set_list AND
			all its neighbors are connected to a node in dom_set_list
				OR
			node is connected to a node in dom_set_list AND 
			exactly one neihbor is not connected to a node in dom_set_list

	Input: node_list - list of all node objects currently in graph
	       dom_set_list - list of all node objects in the dominating set

	Ouput: node_list pruned according to the algorithm rules
	'''
	sortNodeList(node_list)
	pruned_graph = []
	for node in node_list:
		if not nodeInList(dom_set_list, node.id):
			continue
		elif not neighborsDominated(node_list, dom_set_list, node):
			continue
		elif not oneUndominatedNeighbor(node_list, dom_set_list, node):
			continue
		else:
			pruned_graph.append(node)
	return pruned_graph
		
