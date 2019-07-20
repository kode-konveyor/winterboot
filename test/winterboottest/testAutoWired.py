import unittest
from winterboot.WinterBoot import consumers
from winterboot.Autowired import Autowired
from winterboottest.WinterBootTestData import WinterBootTestData
from winterboottest.ExampleService import ExampleService


class Test(unittest.TestCase):

    def setUp(self):
        self.serviceId = WinterBootTestData().undefinedConsumedServiceId
        self.testArtifact = Autowired(self.serviceId)
        self.exampleServiceClass = ExampleService.wrapped  # @UndefinedVariable

    def tearDown(self):
        del consumers[self.serviceId]

    def testAutowired_stores_itself_in_the_consumers_for_service_id(self):
        self.assertTrue(self.testArtifact in consumers[self.serviceId])

    def test_an_error_is_raised_if_we_try_to_use_an_autowired_service_without_definition(self):
        self.assertRaises(AttributeError,lambda : Autowired(self.serviceId).call())

    def test_the_provider_can_be_obtained_by_calling_the_Autowired_object(self):
        exampleService = Autowired('exampleService')
        self.assertEqual(self.exampleServiceClass, exampleService().__class__)  # @UndefinedVariable

    def test_if_singleton_is_False_all_calls_result_in_different_instances(self):
        exampleService = Autowired('exampleService', singleton=False)
        self.assertNotEqual(exampleService(), exampleService()) 

    def test_by_default_all_calls_result_in_same_instance(self):
        exampleService = Autowired('exampleService')
        self.assertEqual(exampleService(), exampleService())  # @UndefinedVariable

    def test_Autowired_as_a_context_manager_provides_the_provider_directly(self):
        with Autowired('exampleService') as exampleService:
            self.assertEquals(self.exampleServiceClass, exampleService.__class__)

    def test_Autowired_as_a_context_manager_can_decorate_an_instance(self):
        with Autowired('exampleService',self):
            self.assertEquals(self.exampleServiceClass, self.exampleService.__class__)

if __name__ == "__main__":
    unittest.main()