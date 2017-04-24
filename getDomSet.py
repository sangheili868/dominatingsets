import random
from Node import Node

def getDomSetNodes(nodes, GDV):
	'''
	Description: takes a graph and the GDV for each node in the graph
		     and generates some nodes in the dominating set for the graph

	Input: nodes - an array of nodes that represent the current graph
	       GDV - a 2-d array of graphlet degree vectors
	
	Output: a set of integer node id's which should be added to the dominating set
	'''
	print('Finding nodes in the dominating set...')
	DominatingSet = set()
	i = 0
	numNodes = len(nodes)

	# Process orbits 0 and nodes of degree 0
	for i in range(0,numNodes):
		if GDV[i][0] == 0:
			DominatingSet.add(i)
		elif GDV[i][0] == 1:
			for n in nodes[i].neighborList:
				if nodes[n].isDominating == 0:
					DominatingSet.add(initialNodes[n].nodeID)
					nodes[n].isDominating = True
	
	# Process orbit 2
	for i in range(0,numNodes):
		if GDV[i][2] == 1 and GDV[i][0] == 2:
			degrees=[]
			neighbors=[]
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1]:
				DominatingSet.add(initialNodes[neighbors[0]].nodeID)
			elif degrees[1] > degrees[0]:
				DominatingSet.add(initialNodes[neighbors[1]].nodeID)
			else:
				node = random.randint(0,1)
				DominatingSet.add(initialNodes[neighbors[node]].nodeID)
	
	#Process orbit 3
	for i in range(0,numNodes):
		if GDV[i][3] == 1 and GDV[i][0] == 2:
			degrees=[]
			neighbors=[]
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1]:
				DominatingSet.add(initialNodes[neighbors[0]].nodeID)
			elif degrees[1] > degrees[0]:
				DominatingSet.add(nodes[neighbors[1]].nodeID)
			else:
				node = random.randint(0,1)
				DominatingSet.add(initialNodes[neighbors[node]].nodeID)
	
	#Process orbit 13
	for i in range(0,numNodes):
		if GDV[i][0] == 3 and GDV[i][13] == 1: 
			degrees = []
			neighbors = []
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1] and degrees[0] > degrees[2]:
				DominatingSet.add(initialNodes[neighbors[0]].nodeID)
			elif degrees[1] > degrees[0] and degrees[1] > degrees[2]:
				DominatingSet.add(initialNodes[neighbors[1]].nodeID)
			elif degrees[2] > degrees[0] and degrees[2] > degrees[1]:
				DominatingSet.add(initialNodes[neighbors[2]].nodeID)
			else:
				node = random.randint(0,2)
				DominatingSet.add(initialNodes[neighbors[node]].nodeID)
	# Process orbit 14
	for i in range(0,numNodes):
		if GDV[i][0] == 3 and GDV[i][14] == 1:
			degrees=[]
			neighbors=[]
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1] and degrees[0] > degrees[2]:
				DominatingSet.add(initialNodes[neighbors[0]].nodeID)
			elif degrees[1] > degrees[0] and degrees[1] > degrees[2]:
				DominatingSet.add(initialNodes[neighbors[1]].nodeID)
			elif degrees[2] > degrees[0] and degrees[2] > degrees[1]:
				DominatingSet.add(initialNodes[neighbors[2]].nodeID)
			else:
				node = random.randint(0,2)
				DominatingSet.add(initialNodes[neighbors[node]].nodeID)

	# ensure that all nodes in dominating sets are marked as dominating and that all their neighbors are marked as dominated
	for n in DominatingSet:
		nodes[n].isDominating = True
		nodes[n].isDominated = True
		for i in nodes[n].neighborList:
			nodes[i].isDominated = True
	return DominatingSet


