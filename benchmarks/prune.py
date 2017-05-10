from Node import Node
from getDomSet import *

def sortList(node_list):
	'''
	Description: Merge sorts a list of integers or node objects
	Input: list of integers or Node objects
	Ouput: None
	'''
	if node_list == []:
		return []

	isNode = None
	if type(node_list[0]) == Node:
		isNode = True
	elif type(node_list[0]) == int:
		isNode = False
	else:
		print("Not a supported type to sort")

	if len(node_list) > 1:
		mid = len(node_list) // 2
		lefthalf = node_list[:mid]
		righthalf = node_list[mid:]
		sortList(lefthalf)
		sortList(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			#Get left and right half based on datatype being sorted
			leftHalf = None
			rightHalf = None		
			if isNode:
				leftHalf = lefthalf[i].nodeID
				rightHalf = righthalf[j].nodeID
			else:
				leftHalf = lefthalf[i]
				rightHalf = righthalf[j]

			if leftHalf < rightHalf:
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

def nodeInList(node_list, node_num):
	'''
	Description: Checks if integer node_num is in the array of integers node_list

	Input: node_list - integer list of node for entire graph sorted with lowest node id at index 0
	       node_num - the id of the node to look for in the node_list

	Output: True if the node_num is found in node_list, false otherwise. Followed by the index in node_list
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
		if not findNode(initial_node_list, neighbor_node).isDominated:
			return False
	return True

def oneUndominatedNeighbor(node_list, node):
	'''
	Description: Determines whether all neighbors but one of given node are conected to a node
		     in the dominating set

	Input: node_list - list of node objects currently in graph
	       node - node object to check the neihbors of

	Output: returns true if all the neigbors but one of node_id are connected to the dominating set,
		false otherwise
	'''

	undominatedNeighbors = 0
	for neighbor_node in node.neighborList:	
		if not findNode(node_list, neighbor_node).isDominated:
			undominatedNeighbors += 1
			if undominatedNeighbors > 1:
				return False

	if undominatedNeighbors == 1:
		return True
	elif undominatedNeighbors == 0:
		return False
	else:
		raise RuntimeError('Impossible number of undominated neighbors in undominatedNeighbors function')


def propogateNodeRemoval(node_to_remove, current_graph):
	'''
	Description: Removes the node from any neighbor lists in the pruned graph
	
	Input: node_to_remove - a node object that is not present in the pruned graph
	       pruned_graph - a list of node objects that represents the current graph

	Output: list of node objects which is the pruned graph
	'''
	propogated_graph = []
	for node in current_graph:
		try:
			node.neighborList.remove(node_to_remove.nodeID)
		except:
			pass
		propogated_graph.append(node)
	return propogated_graph

				
			

def pruneGraph(initial_node_list, current_node_list, dom_set, last_num_nodes):
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
	       last_num_nodes - number of nodes in last iteration of the graph. If it doesn't change,
				we do a tie-break.

	Ouput: node_list pruned according to the algorithm rules
	'''
	
	dom_set_list = list(dom_set)
	sortList(dom_set_list)
	sortList(current_node_list)
	pruned_graph = []
	removed_graph = []
	for node in current_node_list:
		if nodeInList(dom_set_list, node.nodeID):
			removed_graph.append(node)
		elif node.isDominated and neighborsDominated(current_node_list, node):
			removed_graph.append(node)
		elif node.isDominated and oneUndominatedNeighbor(initial_node_list, node):
			removed_graph.append(node)
		else:
			pruned_graph.append(node)
	
	if len(pruned_graph) == last_num_nodes:
		node_to_remove = highestDegNode(pruned_graph)
		removed_graph.append(node_to_remove)
		dom_set.add(node_to_remove.nodeID)
		remove_indx = findNodeIndex(pruned_graph, node_to_remove.nodeID)
		del pruned_graph[remove_indx]
		
		#Remove neighbors and the node itself from pruned graph
		for neigh_id in node_to_remove.neighborList:
			indx = findNodeIndex(pruned_graph, neigh_id)
			neigh_node = findNode(pruned_graph, neigh_id)
			removed_graph.append(neigh_node)
			del pruned_graph[indx]
		
	for node in removed_graph:
		propogateNodeRemoval(node, pruned_graph)
		
	last_num_nodes = len(pruned_graph)		
	return pruned_graph, last_num_nodes, dom_set


