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
	for i in range(0,numNodes):
		if GDV[i][0] == 0:
			DominatingSet.add(i)
		elif GDV[i][0] == 1:
			for n in nodes[i].neighborList:
				if nodes[n].isDominating == False:
					DominatingSet.add(n)
					nodes[n].isDominating = True
	for i in range(0,numNodes):
		if GDV[i][2] == 1 and GDV[i][0] == 2:
			degrees = []
			neighbors = []
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1]:
				DominatingSet.add(neighbors[0])
			elif degrees[1] > degrees[0]:
				DominatingSet.add(neighbors[1])
			else:
				node = random.randint(0,1)
				DominatingSet.add(neighbors[node])
	for i in range(0,numNodes):
		if GDV[i][3] == 1 and GDV[i][0] == 2:
			degrees=[]
			neighbors=[]
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1]:
				DominatingSet.add(neighbors[0])
			elif degrees[1] > degrees[0]:
				DominatingSet.add(neighbors[1])
			else:
				node=random.randint(0,1)
				DominatingSet.add(neighbors[node])
	for i in range(0,numNodes):
		if(GDV[i][0]==3 and GDV[i][13]==1):
			degrees=[]
			neighbors=[]
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1] and degrees[0] > degrees[2]:
				DominatingSet.add(neighbors[0])
			elif degrees[1] > degrees[0] and degrees[1] > degrees[2]:
				DominatingSet.add(neighbors[1])
			elif degrees[2] > degrees[0] and degrees[2] > degrees[1]:
				DominatingSet.add(neighbors[2])
			else:
				node = random.randint(0,2)
				DominatingSet.add(neighbors[node])
	for i in range(0,numNodes):
		if GDV[i][0] == 3 and GDV[i][14] == 1:
			degrees=[]
			neighbors=[]
			for n in nodes[i].neighborList:
				degrees.append(GDV[n][0])
				neighbors.append(n)
			if degrees[0] > degrees[1] and degrees[0] > degrees[2]:
				DominatingSet.add(neighbors[0])
			elif degrees[1] > degrees[0] and degrees[1] > degrees[2]:
				DominatingSet.add(neighbors[1])
			elif degrees[2] > degrees[0] and degrees[2] > degrees[1]:
				DominatingSet.add(neighbors[2])
			else:
				node = random.randint(0,2)
				DominatingSet.add(neighbors[node])
				
	for n in DominatingSet:
		nodes[n].isDominating = True
		nodes[n].isDominated = True
		for i in nodes[n].neighborList:
			nodes[i].isDominated = True
	return DominatingSet

