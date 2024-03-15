CreateUserSchema = {
    201: {
        "isError": False,
        "data": "Usuario agregado correctamente",
        "statusCode": 201,
        "timestamp": "2024-03-11T14:03:57.424048"
    },
    400: {
        "isError": True,
        "message": "Field required",
        "statusCode": 400,
        "timestamp": "2024-03-11T14:03:38.785873"
    },
    409: {
        "isError": True,
        "message": "El usuario ya existe en la base de datos",
        "statusCode": 409,
        "timestamp": "2024-03-11T13:54:25.637304"
    },
    500: {
        "isError": True,
        "message": "El usuario ya existe en la base de datos",
        "statusCode": 409,
        "timestamp": "2024-03-11T13:54:25.637304"
    }
}

# return Response.ok(EntityCreated("Usuario agregado correctamente"))
# return Response.failure(ConflictException("El usuario ya existe en la base de datos"))
# return Response.failure(BadRequestException(err.errors()[0]['msg']))
# return Response.failure(InternalServiceE(err.errors()[0]['msg']))
