import unittest
import prune

class TestPruningFunctions(unittest.TestCase):
	def testSortNodeList(self):
		list1 = []
		list2 = [-1, 9, -3, 0, 1]
		list2_c = [-3, -1, 0, 1, 9] 
		list3 = [1, 0, 3, 4]
		list3_c  = [0, 1, 3, 4]
		list4 = [1, 2, 3, 4]
		self.assertEqual(prune.sortNodeList(list1), list1)
		self.assertEqual(prune.sortNodeList(list2), list2_c)
		self.assertEqual(prune.sortNodeList(list3), list3_c)
		self.assertEqual(prune.sortNodeList(list4), list4_c)
	
	def testBinarySearch(self):
		list1 = [-4, -2, 0, 1, 4, 15, 32]
		list2 = [1, 2, 4, 5, 6]
		list3 = []
		list4 = [0, 1, 2, 3, 4, 8, 9]
		self.assertTrue(self.nodeInList(list1,-2))
		self.assertTrue(self.nodeInList(list1, 0))
		self.assertTrue(self.nodeInList(list1, 15))
		self.assertTrue(self.nodeInList(list2,1))
		self.assertTrue(self.nodeInList(list2,6))
		self.assertTrue(self.nodeInList(list2,4)
		self.asserTrue(self.nodeInList(list4,0))
		self.assertFalse(self.nodeInList(list1,72))
		self.assertFalse(self.nodeInList(list1,3))
		self.assertFalse(self.nodeInList(list1,-90))
		self.assertFalse(self.nodeInList(list2,0))
		self.assertFalse(self.nodeInList(list2,3))
		self.assertFalse(self.nodeInList(list2,71))
		self.assertFalse(self.nodeInList(list3,72))
		self.assertFalse(self.nodeInList(list4,7))
		self.assertFalse(self.nodeInList(list4,72))
		self.assertFalse(self.nodeInList(list4,-90))
	
	def testNeighborsDominated(self):
		node_list = [1, 2, 3, 

)


if __name__ == '__main__':
	unittest.main()
