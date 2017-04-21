import unittest
import prune

class Node(object):
	def __init__(self, nid):
		self.nodeID=nid
		self.neighborList=set()
		self.isDominating=0
		self.isDominated=0



class TestPruningFunctions(unittest.TestCase):
	def testSortNodeList(self):
		list1 = []
		list2 = [-1, 9, -3, 0, 1]
		list2_c = [-3, -1, 0, 1, 9] 
		list3 = [1, 0, 3, 4]
		list3_c  = [0, 1, 3, 4]
		list4 = [1, 2, 3, 4]
		list4_c = [1, 2, 3, 4]

		prune.sortNodeList(list1)
		prune.sortNodeList(list2)
		prune.sortNodeList(list3)
		prune.sortNodeList(list4)
		self.assertEqual(list1, [])
		self.assertEqual(list2, list2_c)
		self.assertEqual(list3, list3_c)
		self.assertEqual(list4, list4_c)
	
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

	'''
	All the following tests use a grpah that looks like
	0 -- 1 -- 2 -- 3 -- 4 .... -- 10
	'''
	def testNeighborsDominated(self):
		node_list = [] 
		node_list.append(Node(0))
		node_list[0].neighborList.add(1)
		for indx in range(1,10):
			node_list.append(Node(indx))
			node_list[indx].neighborList.add(indx + 1)
			node_list[indx].neighborList.add(indx - 1)
		node_list.append(Node(10))
		node_list[10].neighborList.add(9)
		dom_set_list = [1,3,5]
		self.assertTrue(prune.neighborsDominated(node_list, dom_set_list, node_list[2]))
		self.assertTrue(prune.neighborsDominated(node_list, dom_set_list, node_list[4]))
		self.assertFalse(prune.neighborsDominated(node_list, dom_set_list, node_list[7]))
		self.assertFalse(prune.neighborsDominated(node_list, dom_set_list, node_list[6]))

	def testOneUndominatedNeighbor(self):
		node_list = [] 
		node_list.append(Node(0))
		node_list[0].neighborList.add(1)
		for indx in range(1,10):
			node_list.append(Node(indx))
			node_list[indx].neighborList.add(indx + 1)
			node_list[indx].neighborList.add(indx - 1)
		node_list.append(Node(10))
		node_list[10].neighborList.add(9)
		dom_set_list = [1,3,5]
		self.assertTrue(prune.oneUndominatedNeighbor(node_list, dom_set_list, node_list[6]))
		self.assertTrue(prune.oneUndominatedNeighbor(node_list, dom_set_list, node_list[0]))
		self.assertFalse(prune.oneUndominatedNeighbor(node_list, dom_set_list, node_list[7]))
		self.assertFalse(prune.oneUndominatedNeighbor(node_list, dom_set_list, node_list[2]))
	
	def testPruneGraph(self):
		node_list = [] 
		node_list.append(Node(0))
		node_list[0].neighborList.add(1)
		for indx in range(1,10):
			node_list.append(Node(indx))
			node_list[indx].neighborList.add(indx + 1)
			node_list[indx].neighborList.add(indx - 1)
		node_list.append(Node(10))
		node_list[10].neighborList.add(9)
		dom_set_list = [1,3,5]
		new_graph = []
		for i in range(7, 11):
			new_graph.append(Node(i))
		self.assertEqual(prune.pruneGraph(node_list, dom_set_list), new_graph)

if __name__ == '__main__':
	unittest.main()
