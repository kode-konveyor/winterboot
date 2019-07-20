from winterboot import WinterBoot

class Stubs(object):
    def __init__(self, klass):
        self.klass = klass
        self.name = klass.__name__
        if not self.name in WinterBoot.stubs:
            WinterBoot.stubs[self.name] = []
        WinterBoot.stubs[self.name] = self


