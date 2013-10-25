import unittest

def sum(a,b):
	return a+b

class Module1Test(unittest.TestCase):
	def testSum1(self):
		self.assertEqual( sum(1,2), 3 )
	def testSum2(self):
		self.assertEqual( sum(1,-1), 0 )
		
class Module2Test(unittest.TestCase):
	def setUp(self):
		self.bag = [ True, True ]
	def tearDown(self):
		del self.bag
	def test_true(self):
		for element in self.bag:
			self.assertTrue( element )
		
def makeSuite( testcase, tests ):
	return unittest.TestSuite( map(testcase, tests) )

if __name__=="__main__":
	suite1 = makeSuite( Module1Test, ['testSum1', 'testSum2'] )
	suite2 = makeSuite( Module2Test, ['test_true'] )
	
	allsuites = unittest.TestSuite( [suite1, suite2] )
	unittest.TextTestRunner( verbosity=2 ).run( allsuites )