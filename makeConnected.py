from getDomSet import *

def connect(graph, dom_set):
	'''
	Description: turn an independent dominating set into a connected dominating set
	Input: graph - list of node objects
	       dom_set - python set with integer nodeIDs of graph node objects
	Output - returns a python set that is the new connected dominating set
	'''
	degree_sorted_graph = graph[:]
	sortByDegree(degree_sorted_graph)
	for node in degree_sorted_graph:
		path = findNearest(graph, node.nodeID, dom_set)
		for nodeID in path:
			dom_set.add(nodeID)
	return dom_set

def findNearest(graph, start, dom_set):
	'''
	graph is a list of node obj
	start is a int
	dom_set is a set of int
	'''
	q = Queue()
	start_path = [start]
	q.enqueue(start_path)
	while q.IsEmpty() == False:
		tmp_path = q.dequeue()
		last_node = tmp_path[len(tmp_path)-1]
		if last_node in dom_set:
			return tmp_path
		for neigh in findNode(graph, last_node).neighborList:
			if neigh not in tmp_path:
				new_path = []
				new_path = tmp_path + [neigh]
				q.enqueue(new_path)

class Queue:
	def __init__(self):
		self.holder = []
		
	def enqueue(self,val):
		self.holder.append(val)
		
	def dequeue(self):
		val = None
		try:
			val = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass
			
		return val	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result



def sortByDegree(node_list):
	'''
	Description: Merge sorts a list of integers or node objects
	Input: list of integers or Node objects
	Ouput: None
	'''
	if node_list == []:
		return []

	if len(node_list) > 1:
		mid = len(node_list) // 2
		lefthalf = node_list[:mid]
		righthalf = node_list[mid:]
		sortByDegree(lefthalf)
		sortByDegree(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			#Get left and right half based on datatype being sorted
			leftHalf = degreeOf(lefthalf[i])
			rightHalf = degreeOf(righthalf[j])

			if leftHalf < rightHalf:
				node_list[k] = lefthalf[i]
				i = i+1
			else:
				node_list[k] = righthalf[j]
				j = j+1
			k = k+1

		while i < len(lefthalf):
			node_list[k] = lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			node_list[k] = righthalf[j]
			j=j+1
			k=k+1


