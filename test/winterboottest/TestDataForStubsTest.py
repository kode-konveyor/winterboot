import unittest
from winterboot.Autowired import Autowired
from winterboot.TestDataForStub import TestDataForStub
from TestBase import TestBase


class Test(TestBase):

    def testName(self):
        origTestData = Autowired('TestTestData')()
        with TestDataForStub('TestTestData', self):
            self.assertEqual(origTestData, self.TestTestData)

if __name__ == "__main__":
    unittest.main()