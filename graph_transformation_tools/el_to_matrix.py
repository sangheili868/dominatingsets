import sys
if len(sys.argv) != 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
	print('Usage: ' + sys.argv[0] + 'EL_FILE_NAME')

#Open output and input files
fd = open(sys.argv[1], 'r')
out = open(sys.argv[1][0:sys.argv[1].find('.el')] + '.txt', 'w')

#Read the el file into memory
lines = fd.readlines()
num_nodes, edges = lines[0].split(' ')
num_nodes = int(num_nodes)
lines = lines[1:]
edge_u = []
edge_v = []
for line in lines:
	line = line.split(' ')
	edge_u.append(int(line[0].strip()))
	edge_v.append(int(line[1].strip()))

#Create the adjacency matrix
adjMatrix = [[0 for i in range(num_nodes)] for k in range(num_nodes)]
for i in range(len(edge_u)):
	u = edge_u[i]
	v = edge_v[i]
	adjMatrix[u][v] = 1


#Write the matrix
out.write(str(num_nodes) + '\n')
for i in range(num_nodes):
	for j in range(num_nodes):
		out.write(str(adjMatrix[i][j]))
		if j != num_nodes - 1:
			out.write(' ')
	out.write('\n')
