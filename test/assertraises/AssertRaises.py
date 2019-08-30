class AssertRaises(object):
    def __init__(self, klass, kall):
        try:
            kall()
        except klass as e:
            self.exception = e
            return
        raise AssertionError("no exception {0} is raised".format(klass))

    def assertMessageIs(self, msg):
        exceptionMessage = self.exception.args[0]
        if msg != exceptionMessage:
            raise AssertionError("{0} != {1}".format(msg, exceptionMessage))
        return self
