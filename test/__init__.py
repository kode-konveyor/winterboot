import winterboottest
from winterboot.WinterBoot import autoload,providers

autoload(winterboottest)
providers['foo'] = 'bar'