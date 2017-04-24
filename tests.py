import unittest
import prune
from Node import Node

'''
Build a graph that looks like

0 -- 1 -- 2 -- 3 -- 4 .... -- 10

to do testing with 
'''
node_list = [] 

#Build node 0 because has special linkage
node_list.append(Node(0))
node_list[0].neighborList.add(1)

#Bulid nodes 1 - 9 inclusive
for indx in range(1,10):
	node_list.append(Node(indx))
	node_list[indx].neighborList.add(indx + 1)
	node_list[indx].neighborList.add(indx - 1)

#Add a capping end node
node_list.append(Node(10))
node_list[10].neighborList.add(9)
dom_set_list = [1,3,5]

#Mark the needed nodes as dominating
for i in dom_set_list:
	node_list[i].isDominated = True
	node_list[i].isDominating = True
	node_list[i-1].isDominated = True
	node_list[i+1].isDominated = True

class TestPruningFunctions(unittest.TestCase):
	def testSortList(self):
		list1 = []
		list2 = [-1, 9, -3, 0, 1]
		list2_c = [-3, -1, 0, 1, 9] 
		list3 = [1, 0, 3, 4]
		list3_c  = [0, 1, 3, 4]
		list4 = [1, 2, 3, 4]
		list4_c = [1, 2, 3, 4]
		list5 = [Node(7), Node(3), Node(0), Node(5), Node(9)]
		list5_c = [Node(0), Node(3), Node(5), Node(7), Node(9)]
		list6 = [Node(5), Node(0), Node(1), Node(-4)]	
		list6_c = [Node(-4), Node(0), Node(1), Node(5)]			

		prune.sortList(list1)
		prune.sortList(list2)
		prune.sortList(list3)
		prune.sortList(list4)
		prune.sortList(list5)
		prune.sortList(list6)
		self.assertEqual(list1, [])
		self.assertEqual(list2, list2_c)
		self.assertEqual(list3, list3_c)
		self.assertEqual(list4, list4_c)
		for i in range(len(list5_c)):
			self.assertEqual(list5[i].nodeID, list5_c[i].nodeID)
		for i in range(len(list6_c)):
			self.assertEqual(list6[i].nodeID, list6_c[i].nodeID)
	
	def testBinarySearch(self):
		list1 = [-4, -2, 0, 1, 4, 15, 32]
		list2 = [1, 2, 4, 5, 6]
		list3 = []
		list4 = [0, 1, 2, 3, 4, 8, 9]
		self.assertTrue(prune.nodeInList(list1,-2))
		self.assertTrue(prune.nodeInList(list1, 0))
		self.assertTrue(prune.nodeInList(list1, 15))
		self.assertTrue(prune.nodeInList(list2,1))
		self.assertTrue(prune.nodeInList(list2,6))
		self.assertTrue(prune.nodeInList(list2,4))
		self.assertTrue(prune.nodeInList(list4,0))
		self.assertFalse(prune.nodeInList(list1,72))
		self.assertFalse(prune.nodeInList(list1,3))
		self.assertFalse(prune.nodeInList(list1,-90))
		self.assertFalse(prune.nodeInList(list2,0))
		self.assertFalse(prune.nodeInList(list2,3))
		self.assertFalse(prune.nodeInList(list2,71))
		self.assertFalse(prune.nodeInList(list3,72))
		self.assertFalse(prune.nodeInList(list4,7))
		self.assertFalse(prune.nodeInList(list4,72))
		self.assertFalse(prune.nodeInList(list4,-90))

	def testFindNode(self):
		node_list = [Node(1), Node(0), Node(4), Node(38), Node(-2), Node(5)]	
		prune.sortList(node_list)
		node = prune.findNode(node_list, 0)
		self.assertEquals(prune.findNode(node_list, 0).nodeID, 0)
		self.assertEquals(prune.findNode(node_list, 4).nodeID, 4)
		try:
			prune.findNode(node_list, 7)
			self.assertTrue(False)
		except LookupError as e:
			pass
	
		try:
			prune.findNode(node_list, 2)
			self.assertTrue(False)
		except LookupError as e:
			pass

	def testNeighborsDominated(self):
		self.assertTrue(prune.neighborsDominated(node_list, node_list[2]))
		self.assertTrue(prune.neighborsDominated(node_list, node_list[4]))
		self.assertFalse(prune.neighborsDominated(node_list, node_list[7]))
		self.assertFalse(prune.neighborsDominated(node_list, node_list[6]))

	def testOneUndominatedNeighbor(self):
		self.assertTrue(prune.oneUndominatedNeighbor(node_list, node_list[6]))
		self.assertFalse(prune.oneUndominatedNeighbor(node_list, node_list[0]))
		self.assertTrue(prune.oneUndominatedNeighbor(node_list, node_list[7]))
		self.assertFalse(prune.oneUndominatedNeighbor(node_list, node_list[2]))
	
	
	def testPropogateNodeRemoval(self):
		test_graph = node_list[:]
		test_graph[10].neighborList.add(11)
		test_graph[0].neighborList.add(11)
		removed_node = Node(11)
		removed_node.neighborList.add(10)
		removed_node.neighborList.add(0)
		result = prune.propogateNodeRemoval(removed_node, test_graph)
		#turn the sets into sorted lists for easy comparisons
		for i in range(len(result)):
			tmp = list(result[i].neighborList)
			prune.sortList(result)
			result[i].neighborList = tmp
		prune.sortList(result)
		for i, node in enumerate(node_list):
			for j, neigh in enumerate(node.neighborList):
				self.assertEquals(neigh, result[i].neighborList[j])

	def testPruneGraph(self):
		new_graph = []
		for i in range(7, 11):
			new_graph.append(Node(i))
		init_graph = node_list[:]
		dom_set = set()
		dom_set.add(1)
		dom_set.add(3)
		dom_set.add(5)
		pruned_graph = prune.pruneGraph(init_graph, node_list, dom_set)
		prune.sortList(pruned_graph)
		for node in pruned_graph:
			prune.sortList(node.neighborList)
		self.assertEquals(pruned_graph[0].nodeID, 7)
		self.assertEquals(pruned_graph[1].nodeID, 8)
		self.assertEquals(pruned_graph[2].nodeID, 9)
		self.assertEquals(pruned_graph[3].nodeID, 10)
		self.assertEquals(pruned_graph[0].neighborList, [8])
		self.assertEquals(pruned_graph[1].neighborList, [7,9])
		self.assertEquals(pruned_graph[2].neighborList, [8, 10])
		self.assertEquals(pruned_graph[3].neighborList, [9])

if __name__ == '__main__':
	unittest.main()
