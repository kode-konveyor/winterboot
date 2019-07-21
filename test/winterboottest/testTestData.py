
import unittest
from winterboot.WinterBoot import providers
from winterboot.Autowired import Autowired


class Test(unittest.TestCase):

    def test_TestData_annotation_puts_the_service_to_the_providers_list_for_the_service_id(self):
        providerList = providers['testTestData']
        className = providerList[0].wrapped.__name__
        self.assertEqual('TestTestData', className)

    def test_TestData_instances_are_differ(self):
        testTestData = Autowired('testTestData')
        self.assertNotEqual(testTestData(),testTestData())

if __name__ == "__main__":
    unittest.main()