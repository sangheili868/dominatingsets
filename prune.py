def sortList(node_list):
	'''
	Description: Merge sorts a list of integers
	Input: list of integers
	Ouput: None
	'''
	if len(node_list) > 1:
		mid = len(node_list) // 2
		lefthalf = node_list[:mid]
		righthalf = node_list[mid:]
		sortNodeList(lefthalf)
		sortNodeList(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				node_list[k] = lefthalf[i]
				i = i+1
			else:
				node_list[k] = righthalf[j]
				j = j+1
			k = k+1

		while i < len(lefthalf):
			node_list[k] = lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			node_list[k] = righthalf[j]
			j=j+1
			k=k+1

def sortNodes(node_list):
	'''
	Description: Merge sorts a list of Node objects
	Input: list of Nodes
	Ouput: None
	'''
	if len(node_list) > 1:
		mid = len(node_list) // 2
		lefthalf = node_list[:mid]
		righthalf = node_list[mid:]
		sortNodeList(lefthalf)
		sortNodeList(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i].nodeID < righthalf[j].nodeID:
				node_list[k].nodeID = lefthalf[i].nodeID
				i = i+1
			else:
				node_list[k].nodeID = righthalf[j].nodeID
				j = j+1
			k = k+1

		while i < len(lefthalf):
			node_list[k].nodeID = lefthalf[i].nodeID
			i=i+1
			k=k+1

		while j < len(righthalf):
			node_list[k].nodeID = righthalf[j].nodeID
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
			if node_num < node_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1	
	return False

def neighborsDominated(initial_node_list, node):
	'''
	Description: Determines whether all neighbors of given node are connected to a node in the
	             dominating set or are dominating nodes themselves

	Input: initial_node_list - list of node objects in the orignal network
	       node - node object to check the neighbors of

	Output: returns true if all the neigbors of node_id are connected to the dominating set,
		false otherwise
	'''
	for neighbor_node in node.neighborList:
		if not initial_node_list[neighbor_node].isDominated:
			return False
	return True

def oneUndominatedNeighbor(initial_node_list, node):
	'''
	Description: Determines whether all neighbors but one of given node are conected to a node
		     in the dominating set

	Input: node_list - list of node objects currently in graph
	       dom_set_list - integer list of node id's currently in dominating set
	       node - node object to check the neihbors of

	Output: returns true if all the neigbors but one of node_id are connected to the dominating set,
		false otherwise
	'''
	connectedNeighbors = 0
	for neighbor_node in node.neighborList:
		if initial_node_list[neighbor_node].isDominated:
			connectedNeighbors += 1
			if connectedNeighbors > 1:
				return False
	if connectedNeighbors == 1:
		return True
	else:
		return False


def pruneGraph(initial_node_list, current_node_list, dom_set):
	'''
	Description: Removes node from node_list if:
			node is in dom_set_list
				OR
		     	node is connected to a node in dom_set_list AND
			all its neighbors are connected to a node in dom_set_list
				OR
			node is connected to a node in dom_set_list AND 
			exactly one neighbor is not connected to a node in dom_set_list

	Input: initial_node_list - list of node objects initially/globally in the graph
	       current_node_list - list of all node objects currently in graph for this pruning round
	       dom_set - set of all node objects in the dominating set

	Ouput: node_list pruned according to the algorithm rules
	'''
	dom_set_list = list(dom_set)
	sortList(dom_set_list)
	sortNodes(current_node_list)
	pruned_graph = []
	for node in current_node_list:
		if nodeInList(dom_set_list, node.nodeID):
			continue
		elif node.isDominated and neighborsDominated(initial_node_list, node):
			continue
		elif node.isDominated and oneUndominatedNeighbor(initial_node_list, node):
			continue
		else:
			pruned_graph.append(node)
	return pruned_graph


