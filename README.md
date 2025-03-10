# Painting API Django

This project is a CRUD API to manage paintings using Django and Django Rest Framework.

--- 
### Summary
---

* [**PROJECT STRUCTURE**](#project-structure) 
  > Defines the folder and file structure

* [**DATABASE**](#database) 
  > Defines the instructions for the database

* [**INSTALLATION**](#installation) 
  > Defines the instructions for installing and running the project

* [**API USE**](#api-use) 
  > Defines the urls

* [**MODEL**](#model) 
  > Defines model fields

* [**ENDPOINTS**](#endpoints) 
  > Defines the CRUD endpoints

---
<a id="project-structure"></a>
## <center>PROJECT STRUCTURE</center>

```
api-python-django
│
│__ api
│   ├── api
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── painting
│   │   │__ migrations
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py
│   └──manage.py
├──database
│   └── docker-compose.yml
├── API-django.postman_collections.json  
└── README.md
```
---
<a id="database"></a>
## <center>DATABASE</center>

Postgres is being used with docker

In windows it is necessary to make sure that WSL2 is active. 
Command to check that it is enabled:

   ```
   wsl --list --verbose
   ```

If it is not configured, you can enable WSL 2 with this command:
 
   ```
   wsl --set-default-version 2
   ```

Open a terminal in the folder where the docker-compose.yml file is located and execute the following commands:

   ```
   docker-compose build
   ```


   ```
   docker-compose up -d
   ```

The -d flag runs the container in the background


* Connecting to PostgreSQL from Windows
Once the container is running, you can connect to PostgreSQL from your Windows system using a tool such as pgAdmin or the command line. 

<br>

* Connection details:

    ```
        Host: localhost
        Port: 5432
        User: The one you defined in the docker-compose.yml (default “admin”).
        Password: The one you defined in the docker-compose.yml (default “admin”).
        Database: The name you defined in the docker-compose.yml (default “mydatabase”).
    ```

<br>

* Access to the container
If you need to access the container to execute PostgreSQL commands, you can use:

   ```
   docker exec -it postgres_container psql -U admin -d mydatabase
   ```

<br>

* Stop container

   ```
   docker-compose down
   ```
---
<a id="installation"></a>
## <center>INSTALLATION</center>

1. Clone the repository:
   ```
   git clone https://github.com/Orozco23/api-python-django
   cd api-pyhon-django/api
   ```

2. Create a virtual environment and activate it:
   ```
   py -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```
   pip install django djangorestframework psycopg2-binary
   ```

4. Secret Key: add the secret key in the settings.py file

    ```
    SECRET_KEY = 'secret_key'
    ```
    
    Generates the secret key with the command:
   ```
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

5. Make the migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create an administrator user

   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

---
<a id="api-use"></a>
## <center> API USE </center>

The API allows the following CRUD operations to be performed on the paintings:

* **HOST:** http://localhost:8000

- [**Create a painting:**](#create-painting)  `POST /api/paintings/create`
- [**Get painting by id:**](#get-by-id) `GET /api/paintigs/{id}`
- [**Get paintings:**](#get-list) `GET /api/paintings`
- [**Update painting:**](#update) `PUT /api/paintings/update/{id}`
- [**Delete painting:**](#delete) `DELETE /api/paintings/delete/{id}`

---
<a id="model"></a>
## <center> MODEL </center>

``` python
class Painting(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    author = models.CharField(max_length=255, verbose_name="Author")
    month_created = models.PositiveIntegerField(
        verbose_name="Month created",
        validators=[
            MinValueValidator(1),  # Minimum month 1 (January)
            MaxValueValidator(12)  # Maximum 12 (December)
        ]
    )
    year_created = models.PositiveIntegerField(
        verbose_name="Year created", 
        validators=[
            MinValueValidator(1),  # Minimum year allowed
            MaxValueValidator(datetime.datetime.now().year)  # Maximum year allowed (current year)
        ]
    )
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    material = models.CharField(max_length=255, verbose_name="Material used")
    dimensions = models.CharField(max_length=100, verbose_name="Size (Width x Height in cm)")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Last update")

```


---
<a id="endpoints"></a>
## <center> ENDPOINTS </center>

<a id="create-painting"></a>

### **CREATE Painting**
  * **Method:** POST
  * **Note**
    * > Create a painting
  * **route:** {host}/api/paintings/create        
  * **Body:**

    ```json
        {
            "title": {str},
            "author": {str},
            "month_created": {int},
            "year_created": {int},
            "description": {str},
            "material": {str},
            "dimensions": {str}
            }
        
 * **Response**:
      * **HTTP STATUS**: 201
      * **Body**:

    ```json
        {
            "id": {int},
            "title": {str},
            "author": {str},
            "month_created": {int},
            "year_created": {int},
            "description": {str},
            "material": {str},
            "dimensions": {str},
            "creation_date": {date},
            "updated_date": {date}
        }
    
  * **Errors**:
    * **HHTP STATUS**: 400
    * **HHTP STATUS**: 500
    ```json
        {
            "field_name": [
                "message"
            ]
        }
<a id="get-by-id"></a>

### **GET BY ID**
  * **Method:** GET
  * **Note**
    * > Returns painting by id
  * **Route:** {host}/api/paintigs/{id}
 * **Response**:
      * **HTTP STATUS**: 200
      * **Body**:
    ```json
        {
            "id": {int},
            "title": {str},
            "author": {str},
            "month_created": {int},
            "year_created": {int},
            "description": {str},
            "material": {str},
            "dimensions": {str},
            "creation_date": {date},
            "updated_date": {date}
        }
* **Error**:
    * **HHTP STATUS**: 500

<a id="get-list"></a>

### **GET LIST**
  * **Method:** GET
  * **Note**
    * > Returns list of paintings
  * **Route:** {host}/api/paintings
 * **Response**:
      * **HTTP STATUS**: 200
      * **Body**:
    ```json
        {
            [
                {Painting},
                ...
            ]
        }

* **Error**:
    * **HHTP STATUS**: 500

<a id="update"></a>

### **UPDATE**
  * **Method:** PUT
  * **Note**
    * > Update a painting
  * **Route:** {host}/api/paintings/update/{id}
 * **Response**:
      * **HTTP STATUS**: 200
      * **Body**:
    ```json
        {
            "title": {str},
            "author": {str},
            "month_created": {int},
            "year_created": {int},
            "description": {str},
            "material": {str},
            "dimensions": {str}
        }
* **Errors**:
    * **HHTP STATUS**: 400
    * **HHTP STATUS**: 500
    ```json
        {
            "field_name": [
                "message"
            ]
        }
<a id="delete"></a>

### **DELETE**
  * **Method:** DELETE
  * **Note**
    * > Delete a painting
  * **Ruta:** {host}/api/painting/delete/{id}
 * **Response**:
      * **HTTP STATUS**: 204
      * **Body**: No content

* **Errors**:
    * **HHTP STATUS**: 500
