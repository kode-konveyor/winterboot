import winterboottest
from winterboot.WinterBoot import autoload,providers
import unittest

print("TestSetup")
autoload(winterboottest)
providers['foo'] = 'bar'

class TestBase(unittest.TestCase):
    pass
