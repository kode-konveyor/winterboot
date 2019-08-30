from winterboot.Service import Service
from winterboottest.artifacts.ExampleDTO import ExampleDTO

@Service
class ExampleDTOFactory(object):
    def call(self) -> ExampleDTO:
        return ExampleDTO()
