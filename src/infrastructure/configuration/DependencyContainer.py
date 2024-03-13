from injector import inject, Module, singleton
from src.domain.repository.UserRepository import UserRepository
from src.infrastructure.repositories.SQL.dao.UserDAO import UserDAO 


class DependencyContainer(Module):
    @singleton
    @inject
    def configure(self, binder):
        binder.bind(UserRepository, to=UserDAO)
