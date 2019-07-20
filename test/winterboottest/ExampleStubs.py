from winterboot.Autowired import Autowired
from winterboot.Stubs import Stubs

@Stubs
class ExampleStubs(object):
    def behaviour(self):
        with Autowired('exampleService', self):
            self.exampleService.method.return_value = 'got:foo'
