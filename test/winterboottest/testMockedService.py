import unittest
from winterboot.MockedService import MockedService
from winterboot.Autowired import Autowired

exampleServiceCreatedBeforeMock = Autowired('exampleService')
class Test(unittest.TestCase):

    def test_MockedService_changes_the_original_service(self):
        with MockedService('exampleService') as exampleService:
            exampleServiceCreatedBeforeMock().foo()
            exampleService.foo.assert_called_once()

    def test_MockedService_adds_field_to_instance_if_asked(self):
        with MockedService('exampleService', self):
            exampleServiceCreatedBeforeMock().foo()
            self.exampleService.foo.assert_called_once()

if __name__ == "__main__":
    unittest.main()