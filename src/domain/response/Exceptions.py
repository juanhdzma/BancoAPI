from typing import Optional
from src.domain.response.Codes import ErrorCode, StatusCode

class Exception(Exception):
    def __init__(self, message: str, code: ErrorCode, status_code: int, cause: Optional[str] = None):
        self.isError = True
        self.message = message
        self.code = code
        self.statusCode = status_code
        self.cause = cause or None

class BadMessageException(Exception):
    def __init__(self, cause: str, message: str):
        super().__init__(message, ErrorCode.BAD_MESSAGE, StatusCode.BAD_REQUEST, cause)

class RepositoryException(Exception):
    def __init__(self):
        message = 'Ocurrió un error al momento de guardar la guía'
        super().__init__(message, ErrorCode.REPOSITORY_ERROR, StatusCode.INTERNAL_ERROR)

class PubSubException(Exception):
    def __init__(self, message: str, cause: str):
        super().__init__(message, ErrorCode.PUBSUB_ERROR, StatusCode.INTERNAL_ERROR, cause)

class FirestoreException(Exception):
    def __init__(self, code: int, message: str):
        error_mapping = {
            1: ('Firestore action cancelled', StatusCode.INTERNAL_ERROR),
            2: ('Firestore unknown error', StatusCode.INTERNAL_ERROR),
            3: ('Firestore invalid argument', StatusCode.OK),
            4: ('Firestore deadline exceeded', StatusCode.INTERNAL_ERROR),
            5: ('Update nonexistent document', StatusCode.INTERNAL_ERROR),
            6: ('Firestore document already exists', StatusCode.OK),
            7: ('Firestore permission denied', StatusCode.INTERNAL_ERROR),
            8: ('Firestore resource exhausted', StatusCode.OK),
            9: ('Firestore precondition failed', StatusCode.INTERNAL_ERROR),
            # Add more cases as needed
        }
        mapped_error, default_status = error_mapping.get(code, ('Defaulted unknown fs error', StatusCode.INTERNAL_ERROR))
        super().__init__(message, ErrorCode.REPOSITORY_ERROR, default_status.value, mapped_error)
