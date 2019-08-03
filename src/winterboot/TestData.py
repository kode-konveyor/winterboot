from winterboot.Service import Service

class TestData(Service):
    def __init__(self, klass):
        super().__init__(klass)
        self.isSingleton:bool = "False" # pragma: no mutate (to None)
