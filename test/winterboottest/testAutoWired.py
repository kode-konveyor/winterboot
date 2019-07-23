import unittest
from winterboot.WinterBoot import consumers
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService


class Test(unittest.TestCase):

    def setUp(self):
        with MockedService('WinterBootTestData', self):
            self.serviceId = self.WinterBootTestData.undefinedConsumedServiceId
        self.testArtifact = Autowired(self.serviceId)
        self.ExampleServiceClassName = 'ExampleService'

    def tearDown(self):
        del consumers[self.serviceId]

    def testAutowired_stores_itself_in_the_consumers_for_service_id(self):
        self.assertTrue(self.testArtifact in consumers[self.serviceId])

    def test_an_error_is_raised_if_we_try_to_use_an_autowired_service_without_definition(self):
        self.assertRaises(AttributeError,lambda : Autowired(self.serviceId).call())

    def test_the_provider_can_be_obtained_by_calling_the_Autowired_object(self):
        ExampleService = Autowired(self.ExampleServiceClassName)
        self.assertEqual(self.ExampleServiceClassName, ExampleService().__class__.__name__)

    def test_if_singleton_is_False_all_calls_result_in_different_instances(self):
        ExampleService = Autowired(self.ExampleServiceClassName, singleton=False)
        self.assertNotEqual(ExampleService(), ExampleService()) 

    def test_by_default_all_calls_result_in_same_instance(self):
        ExampleService = Autowired(self.ExampleServiceClassName)
        self.assertEqual(ExampleService(), ExampleService())

    def test_Autowired_as_a_context_manager_provides_the_provider_directly(self):
        with Autowired(self.ExampleServiceClassName) as ExampleService:
            self.assertEquals(self.ExampleServiceClassName, ExampleService.__class__.__name__)

    def test_Autowired_as_a_context_manager_can_decorate_an_instance(self):
        with Autowired('ExampleService',self):
            self.assertEquals(self.ExampleServiceClassName, self.ExampleService.__class__.__name__)

if __name__ == "__main__":
    unittest.main()