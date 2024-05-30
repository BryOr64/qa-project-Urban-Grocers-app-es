import requests
import configuration
import data

"""este metodo me devuelve el token del usuario"""
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


"""recibimos el authToken y solo sacamos el valor del mismo"""
def get_new_user_token():
    response = post_new_user(data.user_body.copy())
    response_json = response.json()
    return response_json["authToken"]


"""me crea un nuevo kit"""
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers
                         )


'''funcion para pruebas positivas'''
def positive_assert(name_kit):
    kit_response = post_new_client_kit(name_kit, get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name_kit["name"]


'''funcion para pruebas negativas'''
def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"










