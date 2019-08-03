import unittest
from winterboot import WinterBoot
from winterboot.MockedService import MockedService
import sys

class Test(unittest.TestCase):

    def test_Stubs_registers_the_stub_in_Winterboot_stubs(self):
        className = WinterBoot.stubs['TheExampleStubs'].klass.__name__
        self.assertEqual("TheExampleStubs", className)

    def test_MockedService_runs_the_behaviour_of_the_stub_of_the_related_service(self):
        with MockedService('TheExampleService', self):
            self.assertEqual('get:foo', self.TheExampleService.method('foo'))

    def test_MockedService_runs_the_behaviour_only_if_stubs_exist_for_the_service(self):
        with MockedService('ExampleNonstubbedService', self):
            pass

    def test_MockedService_can_patch_foreign_service(self):
        with MockedService('sys.stdin', self):
            self.assertEqual("foo", sys.stdin.readline())

if __name__ == "__main__":
    unittest.main()