import unittest
from winterboot import WinterBoot
from winterboottest.ExampleStubs import ExampleStubs
from winterboot.MockedService import MockedService

class Test(unittest.TestCase):

    def test_Stubs_registers_the_stub_in_Winterboot_stubs(self):
        self.assertEqual(ExampleStubs, WinterBoot.stubs['ExampleStubs'])

    def test_MockedService_runs_the_behaviour_of_the_stub_of_the_related_service(self):
        with MockedService('exampleService', self):
            self.assertEqual('got:foo', self.exampleService.method('foo'))

    def test_MockedService_runs_the_behaviour_only_if_stubs_exist_for_the_service(self):
        with MockedService('exampleNonstubbedService', self):
            pass

if __name__ == "__main__":
    unittest.main()