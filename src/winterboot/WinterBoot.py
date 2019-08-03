from os.path import isfile, join, isdir
import importlib
import re
from posix import listdir
from typing import Dict  # @UnusedImport

providers: Dict[str,list]= {}

consumers: Dict[str,list] = {}

stubs: Dict[str,list] = {}


def _importAll(files, package, pattern, nameConverter=lambda x: x[:-3]):
    imported = []
    for file in files:
        if re.match(pattern, file) and not file.startswith("_"):
            fullPath = package.__name__ + "." + nameConverter(file)
            imported.append(importlib.import_module(fullPath, package))
    return imported


def _autoload(package):
    mypath = package.__path__[0]
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    _importAll(onlyfiles, package, ".*Service.py$")
    _importAll(onlyfiles, package, ".*TestData.py$")
    _importAll(onlyfiles, package, ".*Stubs.py$")
    _importAll(onlyfiles, package, ".*Factory.py$")
    onlydirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    for loadedPackage in _importAll(onlydirs, package, ".*",lambda x:x):
        _autoload(loadedPackage)

def autoload(package):
    _autoload(package)
    _wire()

def wireOneService(serviceId: str, lazy=False):
    if serviceId not in consumers:
        return
    if serviceId not in providers:
        if lazy is False:
            raise(AttributeError("no provider is registered as {0}".format(serviceId)))
        else:
            return
    provider = providers[serviceId][0]
        
    for consumer in consumers[serviceId]:
        consumer.provider = provider

def _wire():
    for serviceId in consumers:
        wireOneService(serviceId, lazy=True)

def addConsumer(moduleName, client):
    if moduleName not in consumers:
        consumers[moduleName] = []
    consumers[moduleName].append(client)

def addProvider(serviceId, klass):
    if serviceId not in providers:
        providers[serviceId] = []
    providers[serviceId].append(klass)
