from abc import abstractmethod
from src.infrastructure.repository.SQL.model.Account import Account
from src.application.data.IAccount import IAccount
from typing import List


class AccountRepository:
    @abstractmethod
    def crearCuenta(self, data: IAccount) -> bool:
        pass

    @abstractmethod
    def desactivarCuenta(self, idAccount: int) -> bool:
        pass

    @abstractmethod
    def consultarCuentas(self, idUser: str) -> List[Account] | bool:
        pass

    @abstractmethod
    def consultarCuenta(self, idAccount: int) -> Account | bool:
        pass
