from winterboot.Service import Service
from testpackage.ExampleDTO import ExampleDTO

@Service
class ExampleDTOFactory(object):
    def call(self) -> ExampleDTO:
        return ExampleDTO()
