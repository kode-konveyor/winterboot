from winterboot.Service import Service

@Service
class TheExampleService(object):
    def method(self, arg):
        return "got:"+arg
