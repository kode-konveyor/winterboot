import unittest
from winterboot.Autowired import Autowired
from winterboot.TestDataForStub import TestDataForStub


class Test(unittest.TestCase):

    def testName(self):
        origTestData = Autowired('TestTestData')()
        with TestDataForStub('TestTestData', self):
            self.assertEqual(origTestData, self.TestTestData)

if __name__ == "__main__":
    unittest.main()