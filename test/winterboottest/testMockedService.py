import unittest
from winterboot.MockedService import MockedService
from winterboot.Autowired import Autowired

ExampleServiceCreatedBeforeMock = Autowired('ExampleService')
class Test(unittest.TestCase):

    def test_MockedService_changes_the_original_service(self):
        with MockedService('ExampleService') as ExampleService:
            ExampleServiceCreatedBeforeMock().foo()
            ExampleService.foo.assert_called_once()

    def test_MockedService_adds_field_to_instance_if_asked(self):
        with MockedService('ExampleService', self):
            ExampleServiceCreatedBeforeMock().foo()
            self.ExampleService.foo.assert_called_once()

if __name__ == "__main__":
    unittest.main()