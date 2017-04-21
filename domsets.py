from subprocess import call
from sys import argv
import csv

class Node(object):
	def __init__(self, nid):
		self.nodeID=nid
		self.neighborList=set()
		self.isDominating=0
		self.isDominated=0
	def __repr__(self):
		return "Node id: " + str(self.nodeID) + "\nList Size: " + str(len(self.neighborList))+"\n"


# get input file
if len(argv) != 2:
	print("Usage: python domsets.py inFile")
	exit(0)
script, inFile = argv

# build list of nodes and neighbor lists
nodes=[]
with open(inFile) as f:
	numNodes, numEdges = f.readline()[:-1].split(" ")
	numNodes = int(numNodes)
	numEdges = int(numEdges)
	# create node objects
	for i in xrange(numNodes):
		nodes.append(Node(i))
	# add neighbors
	for line in f:
		origin, destination = line[:-1].split(" ")
		origin=int(origin)
		destination=int(destination)
		nodes[origin].neighborList.add(destination)
		nodes[destination].neighborList.add(origin)	
	

# Get GDVs
call(["./orca", "4", inFile, "counts.out"])
GDV=[]
for line in open("counts.out"):
	nodeline=[]
	for ele in line[:-1].split(" "):
		nodeline.append(int(ele))
	GDV.append(nodeline)

DominatingSet=[]
i=0
for i in range(0,numNodes):
	if(GDV[i][0]==0):
		DominatingSet.append(i)
	elif(GDV[i][0]==1):
		for n in nodes[i].neighborList:
			if(nodes[n.id].isDominating==0):
				DominatingSet.append(n.id)
				nodes[n.id].isDominating=1
for i in range(0,numNodes):
	if(GDV[i][2]==1 and GDV[i][0]==2):
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
			degrees.append(GDV[n.id][0])
			neighbors.append(n.id)
		if(degrees[0]>degrees[1]):
			DominatingSet.append(neighbors[0])
		elif(degrees[1]>degrees[0]):
			DominatingSet.append(neighbors[1])
		else:
			node=random.randint(0,1)
			DominatingSet.append(neighbors(node))
for i in range(0,numNodes):
	if GDV[i][3]==1 and GDV[i][0]==2:
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
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
			DominatingSet.append(neighbors(node))
for i in range(0,numNodes):
	if(GDV[i][0]==3 and GDV[i][13]==1):
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
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
			DominatingSet.append(neighbors(node))
for i in range(0,numNodes):
	if(GDV[i][0]==3 and GDV[i][14]==1):
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
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
			DominatingSet.append(neighbors(node))
			
for n in range(0,len(DominatingSet)):
	nodes[DominatingSet[n]].isDominating=1
	nodes[DominatingSet[n]].isDominated=1
	for i in nodes[DominatingSet[n]].neighborList:
		nodes[i.id].isDominated=1

print GDV
print DominatingSet

