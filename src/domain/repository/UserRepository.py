from abc import abstractmethod
from src.application.data.IUser import IUser
from src.domain.response.Result import Result


class UserRepository:
    @abstractmethod
    def crearUsuario(self, data: IUser) -> Result:
        pass

    @abstractmethod
    def consultarUsuario(self, idUser: str) -> Result:
        pass

    @abstractmethod
    def consultarUsuarios(self) -> Result:
        pass