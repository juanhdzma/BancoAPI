from src.infrastructure.repositories.SQL.models.Transaction import Transaction
from src.infrastructure.repositories.SQL.models.Account import Account
from src.domain.repository.TransactionRepository import TransactionRepository
from sqlalchemy import or_


class TransactionDAO(TransactionRepository):
    def __init__(self, database):
        self.database = database

    def hacerTransferencia(self, transaction):
        try:
            session = self.database.createConnection()
            valor = transaction['value']
            origin = transaction['source_account']
            destination = transaction['destination_account']
            session.query(Account).filter_by(id=destination).update({"balance": Account.balance+valor})
            session.query(Account).filter_by(id=origin).update({"balance": Account.balance-valor})
            new_transaction = Transaction(**transaction)
            session.add(new_transaction)
            session.commit()
            return True
        except BaseException:
            return False
        finally:
            self.database.closeConnection(session)

    def hacerConsignacion(self, consignacion):
        try:
            session = self.database.createConnection()
            valor = consignacion['value']
            destination = consignacion['destination_account']
            session.query(Account).filter_by(id=destination).update({"balance": Account.balance+valor})
            new_consignment = Transaction(**consignacion)
            session.add(new_consignment)
            session.commit()
            return True
        except BaseException as error:
            print(error)
            return False
        finally:
            self.database.closeConnection(session)
    
    def historialTransferencias(self, idAccount):
        try:
            session = self.database.createConnection()
            response = session.query(Transaction).filter(or_(Transaction.source_account == idAccount, Transaction.destination_account == idAccount)).all()
            return response
        except BaseException as error:
            return False
        finally:
            self.database.closeConnection(session)