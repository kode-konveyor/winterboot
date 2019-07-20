
import unittest
from winterboot.WinterBoot import providers
from winterboottest.ExampleService import ExampleService


class Test(unittest.TestCase):

    def test_Service_annotation_puts_the_service_to_the_providers_list_for_the_service_id(self):
        providerList = providers['exampleService']
        self.assertEqual(ExampleService, providerList[0])  # @UndefinedVariable

    def test_Services_can_be_instantiated(self):
        instance = ExampleService()
        self.assertEquals(ExampleService.wrapped, instance.__class__)  # @UndefinedVariable

if __name__ == "__main__":
    unittest.main()