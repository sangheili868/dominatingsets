from subprocess import call
import random
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


iterationCount=0

#### START OF ALGORITHM ####
iterationCount+=1
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
if(iterationCount==1):	
        initialNodes=nodes
# Get GDVs
call(["./orca", "4", inFile, "counts.out"])
GDV=[]
for line in open("counts.out"):
	nodeline=[]
	for ele in line[:-1].split(" "):
		nodeline.append(int(ele))
	GDV.append(nodeline)

### FIND NODES IN DOMINATING SET ###
DominatingSet=set()
i=0
for i in range(0,numNodes): # Process orbits 0 and nodes of degree 0
	if(GDV[i][0]==0):
		DominatingSet.add(i)
	elif(GDV[i][0]==1):
		for n in nodes[i].neighborList:
			if(nodes[n].isDominating==0):
				DominatingSet.add(initialNodes[n].nodeID)
				nodes[n].isDominating=1
for i in range(0,numNodes): # Process orbit 2
	if(GDV[i][2]==1 and GDV[i][0]==2):
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
			degrees.append(GDV[n][0])
			neighbors.append(n)
		if(degrees[0]>degrees[1]):
			DominatingSet.add(initialNodes[neighbors[0]].nodeID)
		elif(degrees[1]>degrees[0]):
			DominatingSet.add(initialNodes[neighbors[1]].nodeID)
		else:
			node=random.randint(0,1)
			DominatingSet.add(initialNodes[neighbors[node]].nodeID)
for i in range(0,numNodes): #Process orbit 3
	if GDV[i][3]==1 and GDV[i][0]==2:
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
			degrees.append(GDV[n][0])
			neighbors.append(n)
		if(degrees[0]>degrees[1]):
			DominatingSet.add(initialNodes[neighbors[0]].nodeID)
		elif(degrees[1]>degrees[0]):
			DominatingSet.add(nodes[neighbors[1]].nodeID)
		else:
			node=random.randint(0,1)
			DominatingSet.add(initialNodes[neighbors[node]].nodeID)
for i in range(0,numNodes):
	if(GDV[i][0]==3 and GDV[i][13]==1): #Process orbit 13
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
			degrees.append(GDV[n][0])
			neighbors.append(n)
		if(degrees[0]>degrees[1] and degrees[0]>degrees[2]):
			DominatingSet.add(initialNodes[neighbors[0]].nodeID)
		elif(degrees[1]>degrees[0] and degrees[1]>degrees[2]):
			DominatingSet.add(initialNodes[neighbors[1]].nodeID)
		elif(degrees[2]>degrees[0] and degrees[2]>degrees[1]):
			DominatingSet.add(initialNodes[neighbors[2]].nodeID)
		else:
			node=random.randint(0,2)
			DominatingSet.add(initialNodes[neighbors[node]].nodeID)
for i in range(0,numNodes): # Process orbit 14
	if(GDV[i][0]==3 and GDV[i][14]==1):
		degrees=[]
		neighbors=[]
		for n in nodes[i].neighborList:
			degrees.append(GDV[n][0])
			neighbors.append(n)
		if(degrees[0]>degrees[1] and degrees[0]>degrees[2]):
			DominatingSet.add(initialNodes[neighbors[0]].nodeID)
		elif(degrees[1]>degrees[0] and degrees[1]>degrees[2]):
			DominatingSet.add(initialNodes[neighbors[1]].nodeID)
		elif(degrees[2]>degrees[0] and degrees[2]>degrees[1]):
			DominatingSet.add(initialNodes[neighbors[2]].nodeID)
		else:
			node=random.randint(0,2)
			DominatingSet.add(initialNodes[neighbors[node]].nodeID)

			
for n in DominatingSet: # ensure that all nodes in dominating sets are marked as dominating and that all their neighbors are marked as dominated
	nodes[n].isDominating=1
	nodes[n].isDominated=1
	for i in nodes[n].neighborList:
		nodes[i].isDominated=1
print DominatingSet

#everything above here works

### Update edge list ###

out = open('temp.el','w')

numNodes = len(nodes)
numEdges=0
for n in nodes:
        numEdges += len(n.neighborList)
        for edge in n.neighborList:
                out.write(n.nodeID+' '+edge+'\n')
out.close()
numEdges=numEdges/2

removeDuplicates(numNodes,numEdges,'temp.el','iteration.el') #first file name is file with duplicates. Second file name is file that will not have duplicates. "numNodes numEdges" is the first line of the output file
