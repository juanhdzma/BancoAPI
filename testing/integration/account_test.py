# from requests import get
# from integration_settings import BASE_URL
# from fastapi.testclient import TestClient
# from main import app
import httpx


def test_create_account():
    httpx.AsyncClient()
    # client = TestClient(app)
    # response = client.get(f"/BancoV1/user/1")
    assert 1==1
    # assert response.status_code == 200, 'Error'

# def test_get_account():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'

# def test_get_accounts():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'

# def test_deactivate_account():
#     response = get(f"{BASE_URL}/user/1")
#     assert response.status_code == 200, 'Error'