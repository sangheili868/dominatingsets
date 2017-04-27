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
        '''
        Description: Takes a list of node object and writes the graph they make in el format to outfile

        Input: node_list - list of node objects that make up the graph
               outfile - path of the file to write the graph to. Will be truncated

        Output: None
        '''
        #Temporarily store edges with duplicates in a list of tuples
        edges = []
        for node in node_list:
             for neighbor in node.neighborList:
                  edges.append((node.nodeID, neighbor))
        
        #Remove duplicates (like a -> b and b -> a, keep only a -> b)
        final_edges = {}
        num_edges = 0
        for start_node, end_node in edges:
             if not ((end_node in final_edges and start_node in final_edges[end_node]) 
                  or (start_node in final_edges and end_node in edges[start_node])):
                  if start_node in final_edges:
                       final_edges[start_node].append(end_node)
                  else:
                       final_edges[start_node] = [end_node]
                  num_edges += 1
        
        #Write the graph to outfile
        try:
             with open(outfile, 'w') as fd:
                  num_nodes = len(node_list)
                  fd.write(str(num_nodes) + ' ' + str(num_edges) + '\n')
                  for start_node in final_edges:
                       for end_node in final_edges[start_node]:
                            fd.write(str(start_node) + ' ' + str(end_node) + '\n')
                  fd.flush()

        except EnvironmentError:
             print('Unable to open file ' + outfile)
             exit(0)

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
