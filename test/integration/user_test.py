from requests import post
from integration_settings import BASE_URL
from data.user_test_data import CrearUsuarioIN


def test_create_user():
    responseValida = post(f"{BASE_URL}/user", json=CrearUsuarioIN.dataValida)
    responseCampoNoEnviado = post(f"{BASE_URL}/user", json=CrearUsuarioIN.campoNoEnviado)
    responseCedulaInvalida = post(f"{BASE_URL}/user", json=CrearUsuarioIN.cedulaInvalida)
    responseTelefonoInvalido = post(f"{BASE_URL}/user", json=CrearUsuarioIN.telefonoInvalido)
    responseRepetido = post(f"{BASE_URL}/user", json=CrearUsuarioIN.dataValida)

    assert responseValida.status_code == 201, 'Error en datos validos al crear usuario'
    assert responseCampoNoEnviado.status_code == 400, 'Error en campo no enviado al crear usuario'
    assert responseCedulaInvalida.status_code == 400, 'Error en cedula invalida al crear usuario'
    assert responseTelefonoInvalido.status_code == 400, 'Error en telefono invalido al crear usuario'
    assert responseRepetido.status_code == 409, 'Error en usuario repetido al crear usuario'


# def test_get_user():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'


# def test_get_users():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'
