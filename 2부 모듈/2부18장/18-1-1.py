import unittest

def sum(a,b):
	return a+b

class Module1Test(unittest.TestCase):
	def testSum1(self):
		self.assertEqual( sum(1,2), 3 )
	def testSum2(self):
		self.assertEqual( sum(1,-1), 0 )
		
if __name__=="__main__":
	unittest.main()