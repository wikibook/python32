import unittest

class Module2Test(unittest.TestCase):
	def setUp(self):
		self.bag = [ True, True ]
	def tearDown(self):
		del self.bag
	def test_true(self):
		for element in self.bag:
			self.assertTrue( element )
		
if __name__=="__main__":
	unittest.main()