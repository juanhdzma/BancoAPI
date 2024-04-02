import shutil

def resetDB(func):
    def wrapper():
        shutil.copy(f'base.db', 'operations.db')
        func()
    return wrapper

def removeTimestamp(inDict):
    if "timestamp" in inDict:
        del inDict["timestamp"]
    return inDict


