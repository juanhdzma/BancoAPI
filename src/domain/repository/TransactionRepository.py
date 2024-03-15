from abc import abstractmethod
from src.application.data.ITransaction import ITransaction
from src.application.data.IConsignment import IConsignment
from src.infrastructure.repositories.SQL.models.Transaction import Transaction
from typing import List


class TransactionRepository:
    @abstractmethod
    def hacerTransferencia(self, transaction: ITransaction) -> bool:
        pass

    @abstractmethod
    def hacerConsignacion(self, consignacion: IConsignment) -> bool:
        pass

    @abstractmethod
    def historialTransferencias(self, idAccount: int) -> List[Transaction]:
        pass

