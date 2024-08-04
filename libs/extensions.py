import os
import config
from logging42 import logger

def getexts():
    if config.allowexts == 'false':
        return 'ExtsFalse'
    elif config.allowexts == 'true':
        extensions = []
        for extfile in os.listdir('./ext'):
            if extfile.endswith('.py'):
                extensions.append(extfile.removesuffix('.py'))
        return extensions
    else:
        return 'NotConfigured'