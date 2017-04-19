from subprocess import call
from sys import argv
import csv

class Node:
	id=-1
	neighborList=[]

if len(argv) != 2:
	print("Usage: python domsets.py inFile")
	exit(0)
script, inFile = argv


nodes=[]
numNodes, numEdges = 
with open(inFile) as f:
	next(f)
	for line in f:
		
	

# Get GDVs
for line in open("counts.out"):
	GDVs.append(line[:-1].split(" "))
call(["./orca", "4", inFile, "counts.out"])
GDVs=[]
for line in open("counts.out"):
	GDVs.append(line[:-1].split(" "))
print GDVs


