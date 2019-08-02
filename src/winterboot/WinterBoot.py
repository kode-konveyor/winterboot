from os.path import isfile, join
import importlib
from posix import listdir

providers = {}

def autoload(package):
    mypath = package.__path__[0]
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        if not file.startswith("_"):
            fullPath = package.__name__ + "." + file
            importlib.import_module(fullPath, package)

