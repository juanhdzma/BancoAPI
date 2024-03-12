from enum import Enum

class StatusCode(Enum):
    ## 200 
    OK = 200
    CREATED = 201

    ## 400
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409

    ## 500
    INTERNAL_SERVER_ERROR = 500
