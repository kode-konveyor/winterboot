from winterboot.Stubs import Stubs

@Stubs('sys.stdin')
class SysStdinStubs():
    def behaviour(self, service):
        service.readline.return_value = 'foo'
