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
	Description: Write the given graph to outfile

	Input: node_list - list of node objects that represents a graph to write to the file

	Ouput: None
	'''
	raise NotImplementedError

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
