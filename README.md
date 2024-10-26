# _Proyecto Urban Grocers_ 
Urban Grocers es un aplicacion en la cual podemos realizar un pedido de un kit de alimentos para que nos los puedan preparar, de tal manera es que tambien podemos realizar nuestro propio kit de alimentos para poder tener un kit personalizado pero este no puede pasar de un cierto número de componentes.

para este proreyecto nos adentratemos para realizar las respectivas creaciones de cuentas de usuarios para que asi nos enfoquemos en la creacion neta de los kits personales.

## Descripción del Proyecto

El objetivo de este proyecto es la creación de un kit personalizado para un usuario o usuaria específica. El proceso consta de los siguientes pasos:
1.  **Creación de Usuario/a:**
    -   Enviar una solicitud para crear un nuevo usuario o usuaria y recordar el token de autenticación (authToken).
2.  **Creación de Kit Personal:**
    -   Enviar una solicitud para crear un kit personal para el usuario o usuaria, asegurándose de incluir el encabezado de autorización.
3.  **Pruebas y Verificación:**
    -   Utilizar la lista de comprobación descrita en la tabla para verificar el funcionamiento del sistema. 
        Los resultados de la prueba variarán según el cuerpo de solicitud, pero los pasos para la creación del kit 
        serán los mismos.
    - Requisitos Previos para hacer correr las puebas:
       - Instalar librerias pytest y requests:
          > >    pip3 install pytest  
          > >    pip3 install requests
       - o instalar desde requests.txt
          > > pip3 install -r requirements.txt


| № | Description | ER  |
|--|-------------|-----| 
| 1|El número permitido de caracteres (1): kit_body = { "name": "a"}|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 2|El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}|	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud|
| 3|El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }|	Código de respuesta: 400|
| 4|El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	|Código de respuesta: 400|
| 5|Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 6|Se permiten espacios: kit_body = { "name": " A Aaa " }	|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 7|Se permiten números: kit_body = { "name": "123" }	|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 8|El parámetro no se pasa en la solicitud: kit_body = { }	|Código de respuesta: 400|
| 9|Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	|Código de respuesta: 400|
#
## *Documentación utilizada:*

# [link para el api DOCS](https://cnt-ac1797c6-bc5d-4443-bd6d-0f7333aa1348.containerhub.tripleten-services.com/docs/)

## Técnicas y tecnologías utilizadas
En el proyecto se utilizan diversas tecnologías y técnicas, incluyendo PyCharm, Pytest, Pytest en la terminal para ejecutar las pruebas, Github, Github Desktop, y funciones en Python. Aquí hay una breve descripción de cada una:

1.  **PyCharm:**
    
    -   PyCharm es un entorno de desarrollo integrado (IDE) para Python que proporciona herramientas para escribir, editar, depurar y ejecutar código Python. Se puede configurar para ejecutar pruebas de Pytest.
2.  **Pytest:**
    
    -   Pytest es un framework de pruebas para Python que permite escribir pruebas de manera sencilla y efectiva. Ofrece funcionalidades avanzadas, como la ejecución de pruebas a diferentes escalas y la personalización a través de plugins.
3.  **Pytest en la Terminal:**
    
    -   Pytest se puede ejecutar desde la terminal utilizando comandos específicos, como buscar y ejecutar todos los tests, ejecutar tests de archivos indicados, ejecutar tests en una carpeta específica, entre otros.
4.  **Git y Github:**
    
    -   Github es una plataforma de desarrollo colaborativo que permite alojar proyectos utilizando el sistema de control de versiones Git. Github Desktop es una aplicación que facilita la interacción con repositorios Github a través de una interfaz gráfica.

##Conclusiones
se realizaron las pruebas para ver si podemos crear los nombres de los kits personales, como pudimos evidenciar pasaron algunas pruebas de manera satisfactoria, pero no asi algunas pruebas las cuales se reportaron mediante JIRA para que se puedan tomar nota y poder revisar esas pruebas que no pasaron.
