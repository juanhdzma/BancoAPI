from abc import abstractmethod
from src.infrastructure.repositories.SQL.models.Account import Account
from src.application.data.IAccount import IAccount
from src.domain.response.Result import Result


class AccountRepository:
    @abstractmethod
    def crearCuenta(self, data: IAccount) -> Result:
        pass

    @abstractmethod
    def desactivarCuenta(self, idCuenta: int) -> Result:
        pass

    @abstractmethod
    def consultarCuentas(self, idUser: str) -> Result:
        pass

    @abstractmethod
    def consultarCuenta(self, idAccount: int) -> Result:
        pass

    @abstractmethod
    def desactivarCuenta(self, account: Account) -> Result:
        pass