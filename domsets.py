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
		return "Node id: " + str(self.nodeID) + "\nList: " + str(self.neighborList)+"\n"



if len(argv) != 2:
	print("Usage: python domsets.py inFile")
	exit(0)
script, inFile = argv

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
GDVs=[]
for line in open("counts.out"):
	GDVs.append(line[:-1].split(" "))


