import unittest

def test():
	print("\tthis function is to test old functions")
	assert 1 is not None
	
def init():
	print("\n\tinitialized")
	
def fin():
	print("\tfinalized")
		
if __name__=="__main__":
	testcase = unittest.FunctionTestCase( test, setUp=init, tearDown=fin )
	suite = unittest.TestSuite( [ testcase ] )
	unittest.TextTestRunner( verbosity=2 ).run( suite )