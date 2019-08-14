import unittest
from winterboot.WinterBoot import consumers
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
from TestBase import TestBase

class AutoWiredTest(TestBase):

    def setUp(self):
        with MockedService('WinterBootTestData', self):
            self.serviceId = self.WinterBootTestData.undefinedConsumedServiceId
        self.testArtifact = Autowired(self.serviceId)
        self.TheExampleServiceClassName = 'TheExampleService'

    def tearDown(self):
        del consumers[self.serviceId]

    def testAutowired_stores_itself_in_the_consumers_for_service_id(self):
        self.assertTrue(self.testArtifact in consumers[self.serviceId])

    def test_an_error_is_raised_if_we_try_to_use_an_autowired_service_without_definition(self):
        self.assertRaises(AttributeError,lambda : Autowired(self.serviceId).call())

    def test_the_provider_can_be_obtained_by_calling_the_Autowired_object(self):
        TheExampleService = Autowired(self.TheExampleServiceClassName)
        self.assertEqual(self.TheExampleServiceClassName, TheExampleService().__class__.__name__)

    def test_if_singleton_is_False_all_calls_result_in_different_instances(self):
        TheExampleService = Autowired(self.TheExampleServiceClassName, singleton=False)
        self.assertNotEqual(TheExampleService(), TheExampleService()) 

    def test_by_default_all_calls_result_in_same_instance(self):
        TheExampleService = Autowired(self.TheExampleServiceClassName)
        self.assertEqual(TheExampleService(), TheExampleService())

    def test_Autowired_as_a_context_manager_provides_the_provider_directly(self):
        with Autowired(self.TheExampleServiceClassName) as TheExampleService:
            self.assertEqual(self.TheExampleServiceClassName, TheExampleService.__class__.__name__)

    def test_Autowired_as_a_context_manager_can_decorate_an_instance(self):
        with Autowired('TheExampleService',self):
            self.assertEqual(self.TheExampleServiceClassName, self.TheExampleService.__class__.__name__)

    def test_LAST_INSTANCE_is_a_string_constant(self):
        self.assertEqual("last instance", Autowired.LAST_INSTANCE)

if __name__ == "__main__":
    unittest.main()