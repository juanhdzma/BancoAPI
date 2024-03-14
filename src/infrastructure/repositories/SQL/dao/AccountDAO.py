# from src.infrastructure.repositories.SQL.adapter.SQLiteDatabase import SQLiteDatabase
from src.infrastructure.repositories.SQL.models.Account import Account
from src.domain.repository.AccountRepository import AccountRepository


class AccountDAO(AccountRepository):
    def __init__(self, database):
        self.database = database

    def crearCuenta(self, IAccount):
        try:
            session = self.database.createConnection()
            new_account = Account(**IAccount)
            session.add(new_account)
            session.commit()
            return True
        except BaseException as error:
            print(error)
            return False
        finally:
            self.database.closeConnection(session)

    def consultarCuentas(self, idUser: str):
        try:
            session = self.database.createConnection()
            accounts = session.query(Account).filter_by(user_id=idUser).all()
            return accounts
        except BaseException:
            return False
        finally:
            self.database.closeConnection(session)

    def consultarCuenta(self, idAccount: int):
        try:
            session = self.database.createConnection()
            account = session.query(Account).filter_by(id=idAccount).first()
            return account
        except BaseException:
            return False
        finally:
            self.database.closeConnection(session)
