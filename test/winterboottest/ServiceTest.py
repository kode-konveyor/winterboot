
import unittest
from winterboot.WinterBoot import providers
from winterboottest.referencedartifacts.TheExampleService import TheExampleService
from TestBase import TestBase

class ServiceTest(TestBase):

    def test_Service_annotation_puts_the_service_to_the_providers_list_for_the_service_id(self):
        providerList = providers['TheExampleService']
        self.assertEqual(TheExampleService, providerList[0])

    def test_Services_can_be_instantiated(self):
        instance = TheExampleService()
        self.assertEqual(TheExampleService.wrapped, instance.__class__)  # @UndefinedVariable

if __name__ == "__main__":
    unittest.main()