import unittest
from winterboot.WinterBoot import providers

class Test(unittest.TestCase):
    def test_registering_module_registers_itself(self):
        self.assertEqual('bar', providers['foo'])
