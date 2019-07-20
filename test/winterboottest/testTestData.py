
import unittest
from winterboot.WinterBoot import providers
from winterboottest.TestTestData import TestTestData
from winterboot.Autowired import Autowired


class Test(unittest.TestCase):

    def test_TestData_annotation_puts_the_service_to_the_providers_list_for_the_service_id(self):
        providerList = providers['testTestData']
        self.assertEqual(TestTestData, providerList[0])

    def test_TestData_can_be_instantiated(self):
        instance = TestTestData()
        self.assertEqual(TestTestData.wrapped, instance.__class__)  # @UndefinedVariable

    def test_TestData_instances_are_differ(self):
        testTestData = Autowired('testTestData')
        self.assertNotEqual(testTestData(),testTestData())

if __name__ == "__main__":
    unittest.main()