print(40*'*')
print('testing location \n')
import sys
import unittest
from geograpy import get_geoPlace_context

sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2022twitloccan/twitloccan-main')

class Testlocation(unittest.TestCase):
    """
    Test location
    """
    def test_C3(self):
        import location
        testloc = location.C3()
        print("Start C3 test")
        print(dir(testloc))
        self.assertEqual(testloc.CAN ,11)
        self.assertTrue(testloc.isCan('Canada'))
        self.assertTrue(testloc.isUS('NYC'))
        self.assertFalse(testloc.isCan('NYC'))

    def test_C3geograpy(self):
        import location
        import geograpy
        testgeograpy = location.C3(useGEOGRPY = True)
        self.assertTrue(testgeograpy.isCan('Toronto'))
        self.assertTrue(testgeograpy.isCan('Kingston'))
        self.assertTrue(testgeograpy.isCan('Montreal'))
        self.assertTrue(testgeograpy.isCan('Halifax'))
        self.assertTrue(testgeograpy.isCan('Calgary'))
        self.assertTrue(testgeograpy.isCan('Ottawa'))
        self.assertTrue(testgeograpy.isCan('Montreal'))
        self.assertFalse(testgeograpy.isCan('Lisbon'))
        self.assertFalse(testgeograpy.isUS('Lisbon'))
        self.assertEqual(testgeograpy.getC3('Lisbon'),13)
        
    def test_Docs(self):
        # test examples used in documentation
        import location
        import geograpy
        testlocation = location.C3(useGEOGRPY = True)
        isCan = testlocation.isCan("Winnipeg")
        print(isCan)
        self.assertTrue(isCan)
    
        


if __name__ == '__main__':
    unittest.main()



print(40*'*')


