import sender_stand_request
import data


'''Prueba 1 El número permitido de caracteres (1): kit_body = { "name": "a"}'''
def test_create_new_kit_one_character_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_class['prueba_kit1'])


'''Prueba positive 2 El número permitido de caracteres (511): kit_body = { "name":"Abbbdddd....511"'''
def test_create_new_kit_511_character_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_class['prueba_kit2'])


'''Prueba negative 3 El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }'''
def test_create_new_kit_null_character_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['prueba_kit3'])


'''Prueba negative 4 El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"aa...512"'''
def test_create_new_kit_512_more_character_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['prueba_kit4'])


'''Prueba negative 5 Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }'''
def test_create_new_kit_special_symbol_character_get_error_response():
    sender_stand_request.positive_assert(data.kit_body_class['prueba_kit5'])


'''Prueba negative 6 Se permiten espacios: kit_body = { "name": " A Aaa " }'''
def test_create_new_kit_has_space_character_get_error_response():
    sender_stand_request.positive_assert(data.kit_body_class['prueba_kit6'])


'''Prueba negative 7 Se permiten números: kit_body = { "name": "123" }'''
def test_create_new_kit_has_number_name_get_error_response():
    sender_stand_request.positive_assert(data.kit_body_class['prueba_kit7'])


'''Prueba negative 8 El parámetro no se pasa en la solicitud: kit_body = { }'''
def test_create_new_kit_empty_name_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['prueba_kit8'])


'''Prueba negative 9 Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }'''
def test_create_user_number_type_first_name_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['prueba_kit9'])
