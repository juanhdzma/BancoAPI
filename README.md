# BancoAPI

Este repositorio contiene una API RESTful construida con arquitectura hexagonal. El lenguaje de programación utilizado fue Python con FastAPI. La API tiene como objetivo principal gestionar los procesos de un banco. Estos procesos comprenden operaciones como la gestión de usuarios, la gestión de cuentas (ahorros, corrientes y de crédito), transacciones entre cuentas propias y de otros bancos, además de consignaciones y depósitos.

## Participantes

* [Juan Carlos Hernandez Mariño](https://www.linkedin.com/in/juanhdzma/)
* Carlos Daniel Martinez Zarate
* Kevin Alejandro Rogriguez Grijalba

## Pasos para ejecutar

> [!IMPORTANT]  
> Asegúrate de seguir cada paso cuidadosamente para una experiencia sin problemas.

### 1. Instalación de requisitos

Antes de comenzar, asegúrate de tener instalado Makefile y Python, preferiblemente la última versión disponible.

### 2. Ejecutar instalación

Abre la terminal y ejecuta el siguiente comando para instalar las dependencias necesarias:

``` terminal
make install
```

### 3. Activar el entorno virtual

Una vez instaladas las dependencias, activa el entorno virtual con el siguiente comando:

``` terminal
.\venv\Scripts\activate
```

### 4. Configuración inicial

Luego, procede con la configuración inicial ejecutando:

``` terminal
make setup
```

### 5. Iniciar la aplicación

¡Estás casi listo! Ahora, ejecuta el siguiente comando para poner en marcha la aplicación:

``` terminal
make run
```

### 6. Disfruta

¡Ahora puedes disfrutar de todas las funciones y características que hemos desarrollado para ti!

## Diagramas

A continuacion se encuentra el enlace al archivo .drawio en el cual estan dispuestos los diagramas del proyecto.

[Diagramas del BancoAPI](./docs/diagramas/DiagramasBanco.drawio)

## Documentacion de Endpoints

[Archivo de Postman](./docs/postman/BancoAPI.postman.json)

[OpenAPI](http://ec2-3-137-174-126.us-east-2.compute.amazonaws.com/docs)

## Ejecutar Pruebas

#### Unit Tests

Para ejecutar los unit test se debe ejecutar el siguiente commando.

``` terminal
make unit-test
```

#### Integration Tests

Para ejecutar los test de integracion es necesario ejecutar el servidor local primero, para esto se debe ejecutar el siguiente comando.

``` terminal
make run-local
```

Luego de ejecutar este comando, en otra consola y de forma simultanea, se debe ejecutar el siguiente comando para hacer las pruebas.

``` terminal
make integration-test
```


