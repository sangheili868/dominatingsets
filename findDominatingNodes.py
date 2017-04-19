DominatingSet=[]
i=0
for(i in range(0,numNodes)):
	if(GDV[i][0]==0):
		DominatingSet.append(i)
	elif(GDV[i][0]==1):
		for (n in nodes[i].neighborList):
			DominatingSet.append(n.id)
for(i in range(0,numNodes)):
	if(GDV[i][2]==1 and GDV[i][0]==2):
		degrees=[]
		neighbors=[]
		for(n in nodes[i].neighborList):
			degrees.append(GDV[n.id][0])
			neighbors.append(n.id)
		if(degrees[0]>degrees[1]):
			DominatingSet.append(neighbors[0])
		elif(degrees[1]>degrees[0]):
			DominatingSet.append(neighbors[1])
		else:
			node=random.randint(0,1)
			DominatingSet.append(neighbors(node)))
for(i in range(0,numNodes)):
	if(GDV[i][3]==1 and (GDV[i][0]==2):
		degrees=[]
		neighbors=[]
		for(n in nodes[i].neighborList):
			degrees.append(GDV[n.id][0])
			neighbors.append(n.id)
		if(degrees[0]>degrees[1] and degrees[0]>degrees[2]):
			DominatingSet.append(neighbors[0])
		elif(degrees[1]>degrees[0] and degrees[1]>degrees[2]):
			DominatingSet.append(neighbors[1])
		elif(degrees[2]>degrees[0] and degrees[2]>degrees[1]):
			DominatingSet.addpend(neighbors[2])
		else:
			node=random.randint(0,2)
			DominatingSet.append(neighbors(node)))
for(i in range(0,numNodes)):
	if(GDV[i][0]==3 and GDV[i][13]==1):
		degrees=[]
		neighbors=[]
		for(n in nodes[i].neighborList):
			degrees.append(GDV[n.id][0])
			neighbors.append(n.id)
		if(degrees[0]>degrees[1] and degrees[0]>degrees[2]):
			DominatingSet.append(neighbors[0])
		elif(degrees[1]>degrees[0] and degrees[1]>degrees[2]):
			DominatingSet.append(neighbors[1])
		elif(degrees[2]>degrees[0] and degrees[2]>degrees[1]):
			DominatingSet.addpend(neighbors[2])
		else:
			node=random.randint(0,2)
			DominatingSet.append(neighbors(node)))
for(i in range(0,numNodes)):
	if(GDV[i][0]==3 and GDV[i][14]==1):
		degrees=[]
		neighbors=[]
		for(n in nodes[i].neighborList):
			degrees.append(GDV[n.id][0])
			neighbors.append(n.id)
		if(degrees[0]>degrees[1] and degrees[0]>degrees[2]):
			DominatingSet.append(neighbors[0])
		elif(degrees[1]>degrees[0] and degrees[1]>degrees[2]):
			DominatingSet.append(neighbors[1])
		elif(degrees[2]>degrees[0] and degrees[2]>degrees[1]):
			DominatingSet.addpend(neighbors[2])
		else:
			node=random.randint(0,2)
			DominatingSet.append(neighbors(node)))
			
for(n in range(0,len(DominatingSet))):
	nodes[DominatingSet[n]].isDominating=1
	nodes[DominatingSet[n]].isDominated=1
	for(i in nodes[DominatingSet[n]].neighborList):
		nodes[i.id].isDominated=1
