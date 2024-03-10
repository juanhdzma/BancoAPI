from abc import abstractmethod
from src.application.data.dataIn.IUserDataIn import IUserIn
from src.domain.response.Result import Result

class UserRepository:
    @abstractmethod
    def crearUsuario(self, data: IUserIn) -> Result:
        pass

    @abstractmethod
    def consultarUsuario(self, id: str) -> Result:
        pass