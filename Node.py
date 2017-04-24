class Node(object):
	def __init__(self, nid):
		self.nodeID = nid
		self.neighborList = set()
		self.isDominating = False
		self.isDominated = False


