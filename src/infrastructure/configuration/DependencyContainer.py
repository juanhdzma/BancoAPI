from injector import inject, Module, singleton
from src.infrastructure.repositories.SQL.adapter.CloudDatabase import CloudDatabase
from src.domain.repository.UserRepository import UserRepository
from src.domain.repository.AccountRepository import AccountRepository
from src.infrastructure.repositories.SQL.dao.UserDAO import UserDAO 
from src.infrastructure.repositories.SQL.dao.AccountDAO import AccountDAO 

database = CloudDatabase()


class DependencyContainer(Module):
    @singleton
    @inject
    def configure(self, binder):
        binder.bind(UserRepository, to=UserDAO(database))
        binder.bind(AccountRepository, to=AccountDAO(database))
