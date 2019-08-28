from winterboot.Stubs import Stubs

@Stubs
class TheExampleStubs(object):
    def behaviour(self, service):
            service.method.return_value = 'get:foo'
