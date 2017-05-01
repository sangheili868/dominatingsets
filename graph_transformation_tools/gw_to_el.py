import sys
if len(sys.argv) != 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
	print('Usage: ' + sys.argv[0] + 'EL_FILE_NAME')

#Open output and input files
fd = open(sys.argv[1], 'r')
out = open(sys.argv[1][0:sys.argv[1].find('.gw')] + '.el', 'w')

#Read the el file into memory
lines = fd.readlines()
num_nodes = int(lines[4])
lines = lines[4:]
num_edges = int(lines[num_nodes + 1])
lines = lines[num_nodes + 2:]
edges = []
for line in lines:
	line = line.split(' ')
	edges.append((line[0].strip(), line[1].strip()))

out.write(str(num_nodes + 1) + ' ' + str(num_edges) + '\n')
for start_node, end_node in edges:
	out.write(start_node + ' ' + end_node + '\n')

