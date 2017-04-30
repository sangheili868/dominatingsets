import random
from Node import Node

def findNode(node_list, node_num):
	'''
	Description: Returns a node object with nodeID node_num if found in node_list
	Input: node_list - list of node objects for entire graph sorted with lowest node id at index 0
	       node_num - the id of the node to look for in the node_list
	Output: Returns a node object matching the node_num or None if not present in list
	'''
	first = 0
	last = len(node_list) - 1

	while first <= last:
		midpoint = (first + last) // 2
		if node_list[midpoint].nodeID == node_num:
			return node_list[midpoint]
		else:
			if node_num < node_list[midpoint].nodeID:
				last = midpoint - 1
			else:
				first = midpoint + 1	
	raise LookupError('findNode unable to find a node with id node_num in node_list')


def findNodeIndex(node_list, node_num):
	'''
	Description: Returns the index of node object with node_num in node_list
	Input: node_list - list of node objects for entire graph sorted with lowest node id at index 0
	       node_num - the id of the node to look for in the node_list
	Output: Returns an integer index
	'''
	first = 0
	last = len(node_list) - 1

	while first <= last:
		midpoint = (first + last) // 2
		if node_list[midpoint].nodeID == node_num:
			return midpoint
		else:
			if node_num < node_list[midpoint].nodeID:
				last = midpoint - 1
			else:
				first = midpoint + 1	
	raise LookupError('findNode unable to find a node with id node_num in node_list')

def hasDomSetNeighbor(node, dom_set):
	'''
	Description: takes a node object and returns true if it has a neighbor in the 
		     dominating set, false otherwise
	Input: node - a node object
	       dom_set - a python set with nodeID's of the dominating set nodes
	Output: Boolean value
	'''
	for neighbor in node.neighborList:
		if neighbor in dom_set:
			return True
	return False

def pickRandom(node_list):
	'''
	Description: Returns a random node from the given list
	Input: node_list - a list of node objects to pick from
	Output: a node object picked from the list
	'''
	if node_list == []:
		raise ValueError('Cannot pick from an empty list')
		
	for n in node_list:
		if n.isDominating==True:
			return n

	indx = random.randint(0, len(node_list) - 1)
	return node_list[indx]

def degreeOf(node):
	'''
	Description: returns the degree of a given node object
	Input: a node object
	Ouput: integer value for degree of the node
	'''
	return len(node.neighborList)

def orbitCount(node_indx, GDV, orbit):
	'''
	Description: Wrapper function for accessing a GDV vector for readabilty
	
	Input: node_indx - integer which is the index of a given node object in nodes
	       GDV - 2-d array of graphlet degree vectors
	       orbit - integer which is the orbit to acess. By default returns entire GDV
	Output: an integer if Orbit is given, an array of integers if not
	'''
	return GDV[node_indx][orbit]

def getNeighborNodes(node, sorted_nodes):
	'''
	Description: returns an array of node objects that are neighbors to the given node
	
	Input: node - the node object to find a neighbor of
	       sorted_nodes - the sorted graph the node argument is in
	Ouput: an array of node objects that neighbor the given node
	'''
	neighbor_nodes = []
	for neigh_id in node.neighborList:
		found_node = findNode(sorted_nodes, neigh_id)
		neighbor_nodes.append(found_node)
	return neighbor_nodes

def highestDegNode(node_list):
	'''
	Description: takes a list of node objects and returns the one with the highest degree
 		     Picks a random node if there is a tie for highest degree
	Input: a list of node objects
	
	Output: a node object
	'''
	#Get array of highest degree nodes
	highest_deg = -1
	highest_deg_nodes = []
	for node in node_list:
		if degreeOf(node) > highest_deg:
			highest_deg = degreeOf(node)
			highest_deg_nodes = [node]
		elif degreeOf(node) == highest_deg:
			highest_deg_nodes.append(node)
		else:
			continue

	#Either return highest deg nodes or pick randomly
	if len(highest_deg_nodes) == 0:
		return highest_deg_nodes[0]
	else:
		return pickRandom(highest_deg_nodes)


def processOrbit(curr_graph, dom_set, GDV, desired_degree, desired_orbit):
	'''
	Description: For every node in curr_graph, if the node has exactly desiredDegree and is in
		     desiredOrbit exactly once, the node is added to dom_set.
	
	Input: curr_graph - a list of node objects representing current graph
	       dom_set - a python set of nodeID's in the dominating set
	       desiredDegree - an integer specifying the degree a node should have to be 
                               added to dom_set
	       desiredOrbit - the orbit a node should be in exactly once to be added to
			      the dom_set
	Output: None
	'''
	for node_indx, node in enumerate(curr_graph):
		if orbitCount(node_indx, GDV, desired_orbit) == 1 and degreeOf(node) == desired_degree:
			if not hasDomSetNeighbor(node, dom_set):
				neighbor_nodes = getNeighborNodes(node, curr_graph)
				node_to_add = highestDegNode(neighbor_nodes)
				dom_set.add(node_to_add.nodeID)


def getDomSetNodes(curr_graph, init_graph, GDV):
	'''
	Description: takes a graph and the GDV for each node in the graph
		     and generates some nodes in the dominating set for the graph
	Input: curr_graph - an array of nodes that represent the current graph
	       init_graph - an array of nodes represented the non-pruned graph
	       GDV - a 2-d array of graphlet degree vectors
	       It is assumed that the GDV[i] will give the GDV for node[i]
	
	Output: a set of integer node id's which should be added to the dominating set
		a init_graph marked with node objects marked as dominating or not
	'''

	dom_set = set()

	# Special processing of nodes of degree 0 
	for node in curr_graph:
		if degreeOf(node) == 0:
			dom_set.add(node.nodeID)
	
	# Process orbits 1, 2, 3, 13, and 14
	processOrbit(curr_graph, dom_set, GDV, 1, 0)
	processOrbit(curr_graph, dom_set, GDV, 2, 2)
	processOrbit(curr_graph, dom_set, GDV, 2, 3)
	processOrbit(curr_graph, dom_set, GDV, 3, 13)
	processOrbit(curr_graph, dom_set, GDV, 3, 14)

	# ensure that all nodes in dominating sets are marked as dominating and that all their neighbors are marked as dominated
	for indx, node in enumerate(curr_graph):
		if node.nodeID in dom_set:
			curr_graph[indx].isDominating = True
			curr_graph[indx].isDominated = True
			init_graph[node.nodeID].isDominating = True
			init_graph[node.nodeID].isDominated = True

			for neigh_id in node.neighborList:
				neigh_indx = findNodeIndex(curr_graph, neigh_id)
				curr_graph[neigh_indx].isDominated = True
				init_graph[neigh_id].isDominated = True
				
	return dom_set, init_graph
