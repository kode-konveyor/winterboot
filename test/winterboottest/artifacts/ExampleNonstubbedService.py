from winterboot.Service import Service

@Service
class ExampleNonstubbedService(object):
    def method(self, arg):
        return "get:"+arg
