from src.infrastructure.configuration.DependencyContainer import database

def resetDB(func):
    def wrapper():
        database.resetDatabase()
        func()
    return wrapper

def removeTimestamp(inDict):
    if "timestamp" in inDict:
        del inDict["timestamp"]
    return inDict


