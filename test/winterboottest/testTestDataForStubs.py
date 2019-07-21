import unittest
from winterboot.Autowired import Autowired
from winterboot.TestDataForStub import TestDataForStub


class Test(unittest.TestCase):

    def testName(self):
        origTestData = Autowired('testTestData')()
        with TestDataForStub('testTestData', self):
            self.assertEqual(origTestData, self.testTestData)

if __name__ == "__main__":
    unittest.main()