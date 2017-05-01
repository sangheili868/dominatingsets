import sys
if len(sys.argv) != 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
	print('Usage: ' + sys.argv[0] + 'EL_FILE_NAME')

#Open output and input files
fd = open(sys.argv[1], 'r')
out = open(sys.argv[1][0:sys.argv[1].find('.el')] + '.gv', 'w')

#Read the el file into memory
lines = fd.readlines()
num_nodes, edges = lines[0].split(' ')
num_nodes = int(num_nodes)
lines = lines[1:]
edges = []
for line in lines:
	line = line.split(' ')
	edges.append((line[0].strip(), line[1].strip()))

out.write('graph {')
for start_node, end_node in edges:
	out.write('\n\t' + start_node + ' -- ' + end_node)

out.write('\n}')




