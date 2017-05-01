#!/usr/bin/env python2.7

'''
Brent Marin
2/01/2017

Script to detect duplicate nodes in a tab seperated node list
 
 A duplicate node can be either:
 nodeA<tab>nodeB and nodeA<tab>nodeB
 or 
 nodeA<tab>nodeB and nodeB<tab>nodeA

 Both are detected by this script, since we are assuming a simple graph
'''

FILE_PATH = './AirportData.csv'
DELIM = ' '


fd = None
out = None
try:
	fd = open(FILE_PATH)
	out = open('output.csv', 'w')
except:
	print "Issue opening file"

edges = {}
duplicates = 0

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

print "Number of duplicates interactions in file: {}".format(duplicates)
