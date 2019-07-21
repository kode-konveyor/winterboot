from winterboot.Stubs import Stubs

@Stubs
class ExampleStubs(object):
    def behaviour(self, service):
            service.method.return_value = 'got:foo'
