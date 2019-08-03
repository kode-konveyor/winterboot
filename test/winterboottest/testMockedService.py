import unittest
from winterboot.MockedService import MockedService
from winterboot.Autowired import Autowired
from winterboot.WinterBoot import providers
import sys

TheExampleServiceCreatedBeforeMock = Autowired('TheExampleService')
class Test(unittest.TestCase):

    def test_MockedService_changes_the_original_service(self):
        with MockedService('TheExampleService') as TheExampleService:
            TheExampleServiceCreatedBeforeMock().foo()
            TheExampleService.foo.assert_called_once()

    def test_MockedService_adds_field_to_instance_if_asked(self):
        with MockedService('TheExampleService', self):
            TheExampleServiceCreatedBeforeMock().bar()
            self.TheExampleService.bar.assert_called_once()

    def test_MockedService_can_mock_foreign_stuff(self):
        with  MockedService('sys.stderr', self):
            sys.stderr.write("hello")
        self.sys_stderr.write.assert_called_once()

    def test_MockedService_unmocks_foreign_stuff_after_use(self):
        with  MockedService('sys.stderr', self):
            sys.stderr.write("hello")
        sys.stderr.write("hello")
        self.sys_stderr.write.assert_called_once()

    def test_MockedService_does_not_leave_foreign_service_in_registry(self):
        with  MockedService('sys.stderr', self):
            sys.stderr.write("hello")
        self.assertFalse('sys.stderr' in providers)

if __name__ == "__main__":
    unittest.main()