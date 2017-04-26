import csv
import os
from Node import Node
from sys import argv
from subprocess import call

def parseCommandLineArgs():
	'''
	Description: Retrieves command line args and checks their validity
	
	Input: None

	Output: Returns a string name of a file to read the graph from
	'''
	if len(argv) != 2:
		print("Usage: python domsets.py inFile")
		exit(0)
	script, inFile = argv
	return inFile



def readGraph(inFile):
	'''
	Description: Read a graph from infile. See example.in for format

	Input: String file name to read graph from

	Output: a list of Node objects to which represents the read in graph
	'''
	nodes=[]
	try:
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
		return nodes

	except EnvironmentError:
		print('Unable to open file ' + inFile)
		exit(0)	
	
def writeGraph(node_list, outfile): 
        #Takes a list of nodes and an output file destination as its input. Returns an edge list representation of the graph contained in node_list
        
        call(["rm","temp.el"])
        tmpOut = open('temp.el','w') # holds the edge list with duplicates
        numNodes = len(node_list)
        numEdges=0
        for n in node_list: #print all source/destination pairs to temp.el
                numEdges += len(n.neighborList)
                for edge in n.neighborList:
                        tmpOut.write(n.nodeID+' '+edge+'\n')
        out.close()
        numEdges=numEdges/2
        fd = None
        out = None
        DELIM=' '
        try:
                fd = open('temp.el','r')
                out = open(outfile, 'w')
        except:
                print "Issue opening file"

        edges = {}
        duplicates = 0
        out.write(str(numNodes)+' '+str(numEdges))
        for line in fd.readlines():
                nodes = line.split(DELIM)
                nodes[1] = nodes[1].strip() # get rid of the \n

                if (nodes[1] in edges and (nodes[0] in edges[nodes[1]])) or (nodes[0] in edges and (nodes[1] in edges[nodes[0]])):
                        duplicates += 1
                else: 
                        out.write(nodes[0] + ' ' + nodes[1] + '\n')         
                        if nodes[0] in edges:
                                edges[nodes[0]].append(nodes[1])
                        else:
                                edges[nodes[0]] = [nodes[1]]
        try:
                fd.close()
        except:
                print "Issue closing file"

def calcGDVs(inFile):
	'''
	Description: Calculates GDV using orca for a given graph file

	Input: inFile - Path of a graph file to calculate gdv's for

	Ouput: A 2-d array with node as the first index and graphlet orbit as the second
	'''
	
	print('Counting graphlets...')
	call(["./orca", "4", inFile, "counts.out"])
	
	GDV=[]
	try:
		with open("counts.out") as fd:
			for line in fd:
				nodeline=[]
				for ele in line[:-1].split(" "):
					nodeline.append(int(ele))
				GDV.append(nodeline)	
		return GDV

	except EnvironmentError:
		print('Unable to open counts.out')
		exit(0)
