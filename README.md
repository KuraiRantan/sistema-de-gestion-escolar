# Sistema de gestión escolar(SGE)

## Contenido
1. [Proyecto](#user-content-proyecto)
  - [Descripción](#user-content-proyecto-descripcion)
  - [ToDo](#user-content-proyecto-todo)
2. [Deploy](#user-content-deploy)
  - [Development](#user-content-deploy-development)
3. [Accesos disponibles](#user-content-acceso)
  - [Endpoints](#user-content-acceso-endpoints)
      - [Student](#user-content-acceso-endpoints-student)
        - [GET](#user-content-acceso-endpoints-student-get)
        - [POST](#user-content-acceso-endpoints-student-post)
        - [PUT](#user-content-acceso-endpoints-student-put)
        - [DELETE](#user-content-acceso-endpoints-student-delete)
      - [Classroom](#user-content-acceso-endpoints-classroom)
        - [GET](#user-content-acceso-endpoints-classroom-get)
        - [POST](#user-content-acceso-endpoints-classroom-post)
        - [PUT](#user-content-acceso-endpoints-classroom-put)
        - [DELETE](#user-content-acceso-endpoints-classroom-delete)
      - [Subject](#user-content-acceso-endpoints-subject)
        - [GET](#user-content-acceso-endpoints-subject-get)
        - [POST](#user-content-acceso-endpoints-subject-post)
        - [PUT](#user-content-acceso-endpoints-subject-put)
        - [DELETE](#user-content-acceso-endpoints-subject-delete)
      - [Attendance](#user-content-acceso-endpoints-attendance)
        - [GET](#user-content-acceso-endpoints-attendance-get)
        - [POST](#user-content-acceso-endpoints-attendance-post)
        - [PUT](#user-content-acceso-endpoints-attendance-put)
        - [DELETE](#user-content-acceso-endpoints-attendance-delete)
  - [Página web](#user-content-acceso-pagina-web)
      - [Student](#user-content-acceso-pagina-web-student)
      - [Subject](#user-content-acceso-pagina-web-subject)
      - [Classroom](#user-content-acceso-pagina-web-classroom)
      - [Attendance](#user-content-acceso-pagina-web-attendance)

## <span id="user-content-proyecto">Proyecto</span>

### <span id="user-content-proyecto-descripcion">Descripción</span>
El proyecto consiste en desarrollar una aplicación web para gestionar operaciones clave de una institución educativa. Esta aplicación deberá incluir los módulos para el registro de:
- Estudiantes.
- Salones.
- Materias
- Seguimiento de la asistencia.
### <span id="user-content-proyecto-todo">To Do</span>
- **Registro de Estudiantes (Python Web2py, TypeScript, Clases Repository, de Modelo, Factory, Renderer, Controller)** 

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Desarrollar un formulario de registro de estudiantes utilizando completamente TypeScript             | $${\color{green}Finalizado}$$|
| Implementar la validación de datos y la comunicación con el backend. Desarrollar una API que maneje las solicitudes para el registro de los estudiantes usando un controlador en web2py.| $${\color{green}Finalizado}$$ |
| En python: Implementa y usa las Clases Repository que permitan interactuar con cada tabla donde se requiera agregar o actualizar datos a la base de datos | $${\color{green}Finalizado}$$ |
| En Typescript: Debes implementar las clases de Repository las cuales llaman al api para el registro de estudiantes, Clase de Modelo para modelar el formulario, Clase de renderer para generar el html del modelo de formulario creado, Clase Factory para crear instancias del modelo de formulario, Clase de controller para atender los eventos del formulario y ejecutar las acciones necesarias. | $${\color{green}Finalizado}$$ |

---
<br/>
<br/>

- **Gestión de Salones y Materias (Python Web2py sqlform.grid)**

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Utilizar sqlform.grid para crear vistas CRUD para la administración de las tablas como: Salón, Materia. | $${\color{green}Finalizado}$$ |
| Aplicar ordenamiento en las tablas por: nombre de salón, nombre de la materia. | $${\color{green}Finalizado}$$ |

---
<br/>
<br/>

- **Registro de Asistencia (Python Web2py, Javascript, Clases de Modelo, Factory, Singleton y Renderer)**

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Crear clases de modelo separadas para Estudiante, Salón y Materia. | $${\color{green}Finalizado}$$ |
| Utilizar el patrón de diseño Factory para crear instancias de los modelos Estudiante, Salón y Materia. | $${\color{green}Finalizado}$$ |
| Aplica en patron de diseño Singleton y Cache en las clases Factory de Salón y Materia. | $${\color{red}Pendiente}$$ |
| Desarrollar una clase Renderer en la carpeta /renderer para el control de asistencia. | $${\color{green}Finalizado}$$ |
| La clase Renderer debe encargarse de generar la visualización de estos modelos utilizando objetos HTML de Web2py, asegurando que cada elemento se muestre correctamente en la interfaz. | $${\color{green}Finalizado}$$ |
| La visualización debe incluir listas o tablas que muestren los estudiantes, salones y materias, con la opción de marcar asistencia. | $${\color{green}Finalizado}$$ |
| Cada fila correspondiente a un estudiante debe incluir un control select con opciones como "Asistió" y "Ausente". | $${\color{green}Finalizado}$$ |
| Integrar funciones de JavaScript que se activen cuando se cambie el estado en el control select. | $${\color{green}Finalizado}$$ |
| Estas funciones deben estar diseñadas para hacer llamadas a una API que registre los cambios de asistencia en la base de datos | $${\color{green}Finalizado}$$ |
| Desarrollar una API que maneje las solicitudes para actualizar el estado de asistencia de los estudiantes. | $${\color{green}Finalizado}$$ |
| Esta API debe interactuar con la base de datos usando sus clases Repository para registrar los cambios efectuados desde la interfaz de usuario. | $${\color{green}Finalizado}$$ |

---
<br/>
<br/>

- **Gestión de Base de Datos y Migraciones (Postgres, Alembic)**

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Utilizar Alembic para la creación y gestión de tablas de base de datos. | $${\color{green}Finalizado}$$ |
| Incluir scripts de migración para la estructura inicial, carga de datos para pruebas y cualquier cambio posterior. | $${\color{orange}En proceso}$$ |

---
<br/>
<br/>

- **Pruebas Unitarias y de Integración (unittest, Jest, mockups)**

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Implementar tests unitarios para cada módulo o clase creada en Python. | $${\color{red}Pendiente}$$ | 
| Implementar tests unitarios para cada módulo o clase creada en Typescript. | $${\color{red}Pendiente}$$ |
| Uso de mockups para simular interacciones por ejemplo: de base de datos, servicios api, etc. | $${\color{red}Pendiente}$$ |

---
<br/>
<br/>

- **Dockerización y Despliegue**

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Crear un Dockerfile para construir una imagen del proyecto. | $${\color{green}Finalizado}$$ |
| Desarrollar un archivo docker-compose para facilitar el despliegue y la ejecución del proyecto. | $${\color{green}Finalizado}$$ |

---
<br/>
<br/>

- **Control de Calidad de Código**

| Requisito                                                                                            | Estado    |
|------------------------------------------------------------------------------------------------------|-----------|
| Agrega tipado de datos en todos los argumentos y retornos de funciones python y typescript. | $${\color{orange}En   proceso}$$ |
| Utilizar herramientas como black, flake8, pylint, bandit para Python, y ESLint para TypeScript. | $${\color{orange}En   proceso}$$ |
| Asegurar que todo el código cumple con los estándares de calidad y seguridad establecidos. | $${\color{orange}En   proceso}$$ |

---
<br/>

## <span id="user-content-deploy">Deploy</span>
### <span id="user-content-deploy-development">Development</span>
Clonar el repositorio:
```
git clone <url-repo>
```
Crear un archivo o hacer una copia de `.env_example`(se encuentra en la raíz del repo) y renombrar como `.env`,
debe contener la siguiente estructura(modificar valores según se requiera):
```env
# Database credentials for postgresql.
POSTGRES_USER=example
POSTGRES_PASSWORD=example
POSTGRES_DB=example

# Database credentials for web2py and alembic(DO NOT CHANGE).
DB_USER=$POSTGRES_USER  
DB_PASSWORD=$POSTGRES_PASSWORD
DB_NAME=$POSTGRES_DB

# Driver for alembic.
ALEMBIC_DRIVER=postgresql

# Driver for web2py.
WEB2PY_DRIVER=postgres

# Name of the container that runs the database. It is used as a host.
HOST_CONTAINER=SGE_DB
```
Crear y ejecutar el contenedor a partir del archivo `docker-compose.dev.yaml` con el comando:
```bash
docker compose -f <path-docker-compose.yaml> up -d
```
Están disponibles dos variables de entorno(además de las disponibles en el .env):
```txt
PASSWORD_ADMIN_SERVER -> Esta es la contraseña para acceder al administrador de web2py, por defecto es "pwd".
PORT -> Es el puerto que se expone al host, por defecto es "8000".
```
En caso de querer modificar alguna de estas dos el comando seria:
```bash
PASSWORD_ADMIN_SERVER=<custom_value> PORT=<custom_value> docker compose -f <path-docker-compose.yaml> up -d
```
Con esto el proyecto ya estará accesible, puedes comprobarlo ingresando al localhost con el puerto `8000`(si se dejo la variable `PORT` por defecto):
```
https://localhost:8000
```
>[!IMPORTANT]
> Se debe acceder con https:// al inicio de la `url` o de lo contrario no estará disponible la página, ya que se agregó certificado ssl autofirmado requerido para habilitar el administrador de web2py.


## <span id="user-content-acceso">Accesos disponibles</span>
En esta sección, se detallan las diversas URL disponibles para acceder tanto a la API, con todos sus métodos, como a las vistas web que ofrece la aplicación.Tenga en cuenta que se tomara como referencia el puerto por defecto.

### <span id="user-content-acceso-endpoints">Endpoints</span>
  En esta sección se detallan los puntos finales de la API disponibles, junto con los métodos HTTP implementados para cada uno.

#### <span id="user-content-acceso-endpoints-student">Student</span>

  | Campo                 | Tipo   | Requerido | Descripción                 |
  |-----------------------|--------|-----------|-----------------------------|
  | id                    |   int  | Sí/No     | Id para el registro |
  | type_of_identification| string | Sí        | Tipo de identificación del estudiante. |
  | identification        | string | Sí        | Número de identificación del estudiante. |
  | first_name            | string | Sí        | Primer nombre del estudiante. |
  | last_name             | string | Sí        | Apellido del estudiante. |
  | birthdate             | date   | Sí        | Fecha de nacimiento del estudiante(yyyy-MM-dd). |
  | gender                | string | Sí        | Género del estudiante. |
  | address               | string | No        | Dirección del estudiante. |
  | email                 | string | No        | Correo electrónico del estudiante. |
  | phone                 | string | No        | Número de teléfono del estudiante. |
  | current_grade         | string | Sí        | Grado actual del estudiante. |

- **<span id="user-content-acceso-endpoints-student-get">GET</span>**
  
  No implementado.

- **<span id="user-content-acceso-endpoints-student-post">POST</span>**

    Creación de un nuevo estudiante.
    ```
    https://localhost:8000/SGE/api/student.json
    ```
    Ejemplo body:
    ```json
    {
      "type_of_identification": "DNI",
      "identification": "12345678A",
      "first_name": "Juan",
      "last_name": "Pérez",
      "birthdate": "1990-05-15",
      "gender": "Masculino",
      "address": "Calle Principal 123", // Opcional.
      "email": "juan@example.com",      // Opcional.
      "phone": "+1234567890",           // Opcional.
      "current_grade": "10A"
    }
    ```

- **<span id="user-content-acceso-endpoints-student-put">PUT</span>**
  
  No implementado.

- **<span id="user-content-acceso-endpoints-student-delete">DELETE</span>**
  
  No implementado.

#### <span id="user-content-acceso-endpoints-classroom">Classroom</span>
- **<span id="user-content-acceso-endpoints-classroom-get">GET</span>**

  No implementado.

- **<span id="user-content-acceso-endpoints-classroom-post">POST</span>**

  No implementado.

- **<span id="user-content-acceso-endpoints-classroom-put">PUT</span>**

  No implementado.

- **<span id="user-content-acceso-endpoints-classroom-delete">DELETE</span>**

  No implementado.

#### <span id="user-content-acceso-endpoints-subject">Subject</span>
- **<span id="user-content-acceso-endpoints-subject-get">GET</span>**

  No implementado.

- **<span id="user-content-acceso-endpoints-subject-post">POST</span>**

  No implementado.

- **<span id="user-content-acceso-endpoints-subject-put">PUT</span>**

  No implementado.

- **<span id="user-content-acceso-endpoints-subject-delete">DELETE</span>**

  No implementado.

#### <span id="user-content-acceso-endpoints-attendance">Attendance</span>

  | Campo           | Tipo   | Requerido | Descripción                 |
  |-----------------|--------|-----------|-----------------------------|
  | id              | int    | Si/No        | Id para el registro.        |
  | student         | int    | Sí        | ID del estudiante asociado. |
  | subject         | int    | Sí        | ID de la materia asociada.  |
  | classroom       | int    | Sí        | ID del salón de clases.     |
  | grade           | string | Sí        | Calificación del estudiante.|
  | attendance_date | date   | Sí        | Fecha de la asistencia.     |
  | status          | string | Sí        | Estado de la asistencia.    |
  | notes           | text   | No        | Notas adicionales.          |

  - **<span id="user-content-acceso-endpoints-attendance-get">GET</span>**

    No implementado.

  - **<span id="user-content-acceso-endpoints-attendance-post">POST</span>**

    Cambio del estado de la asistencia del estudiante.
    ```
    https://127.0.0.1:8000/SGE/api/attendance.json/change-attendance-status
    ```
    Ejemplo body:
    ```json
    {
      "id": 1 // Identificador de la asistencia(attendance).
      "status": "Presente",
    }
    ```
  - **<span id="user-content-acceso-endpoints-attendance-put">PUT</span>**

    No implementado.

  - **<span id="user-content-acceso-endpoints-attendance-delete">DELETE</span>**

    No implementado.

### <span id="user-content-pagina-web">Página web</span>
En esta sección se proporcionan enlaces a las páginas web disponibles en la aplicación.

#### <span id="user-content-pagina-web-student">Student</span>
Página para crear un nuevo estudiante.
```
https://localhost:8000/SGE/student/create
```

#### <span id="user-content-pagina-web-classroom">Classroom</span>
Página para realizar operaciones CRUD sobre los salones.
```
https://localhost:8000/SGE/classroom/manage
```

#### <span id="user-content-pagina-web-subject">Subject</span>
Página para realizar operaciones CRUD sobre las materias.
```
https://localhost:8000/SGE/subject/manage
```

#### <span id="user-content-pagina-web-attendance">Attendance</span>
Página web para generar y rellenar el listado de asistencia.
```
https://localhost:8000/SGE/attendance/fill
```

