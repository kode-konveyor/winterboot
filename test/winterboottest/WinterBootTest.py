import unittest
from winterboot.WinterBoot import wireOneService, autoload, consumers
from winterboot.Autowired import Autowired
from assertraises.AssertRaises import AssertRaises
from TestBase import TestBase

class WinterBootTest(TestBase):

    def setUp(self):
        with Autowired('WinterBootTestData', self):
            if self.WinterBootTestData.undefinedConsumedServiceId in consumers:
                del consumers[self.WinterBootTestData.undefinedConsumedServiceId]
            import testpackage
            autoload(testpackage)
            Autowired(self.WinterBootTestData.undefinedConsumedServiceId)

    def test_wireOneService_by_default_wires_undefined_services(self):
        wireOneService(self.WinterBootTestData.undefinedConsumedServiceId,lazy=True)

    def test_wireOneService_throws_AttributeError_if_lazy_is_False_and_there_is_a_consumer(self):
        AssertRaises(
            AttributeError,
            lambda: wireOneService(self.WinterBootTestData.undefinedConsumedServiceId,lazy=False))\
        .assertMessageIs("no provider is registered as undefinedConsumedServiceId")

    def test_wireOneService_is_silent_if_there_is_no_consumer(self):
        wireOneService(self.WinterBootTestData.undefinedNonConsumedServiceId,lazy=True)

    def test_wireOneService_is_silent_if_there_is_no_consumer_even_if_lazy_is_false(self):
        wireOneService(self.WinterBootTestData.undefinedNonConsumedServiceId,lazy=False)

    def test_autoload_registers_all_services_in_a_package(self):
        self.setUp()
        testService = Autowired('TestService')
        serviceInstance = testService()
        self.assertTrue(serviceInstance.canBeCalled())

if __name__ == "__main__":
    unittest.main()