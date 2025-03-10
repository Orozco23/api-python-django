# KANBAN API Django

This project is a CRUD API to manage the cards of a kanban board using Django and Django Rest Framework.

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
│   ├── card
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
├── Kanban-API.postman_collections.json  
└── README.md
```
---
<a id="database"></a>
## <center>DATABASE</center>

Postgres is running from docker

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
        Database: The name you defined in the docker-compose.yml ("paintingAPI").
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

The API allows the following CRUD operations to be performed on the cards:

* **HOST:** http://localhost:8000

- [**Create a card:**](#create-card)  `POST /api/cards/create`
- [**Get card by id:**](#get-by-id) `GET /api/cards/{id}`
- [**Get cards:**](#get-list) `GET /api/cards`
- [**Update card:**](#update) `PUT /api/cards/update/{id}`
- [**Delete card:**](#delete) `DELETE /api/cards/delete/{id}`

---
<a id="model"></a>
## <center> MODEL </center>

``` python
class Card(models.Model):
    title = models.CharField(max_length=255, verbose_name="Card Title")
    description = models.TextField(verbose_name="Card Description", blank=True, null=True)
    column = models.CharField(
        max_length=20,
        verbose_name="Column",
        choices=[
            ('To Do', 'To Do'),
            ('In Progress', 'In Progress'),
            ('Done', 'Done')
        ],
        default='To Do'
    )
    position = models.PositiveIntegerField(verbose_name="Position in List", validators=[MinValueValidator(1)])
    due_date = models.DateTimeField(verbose_name="Due Date", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        ordering = ['column', 'position']  # Sort cards by position in the list
    def __str__(self):
        return self.title

```


---
<a id="endpoints"></a>
## <center> ENDPOINTS </center>

<a id="create-card"></a>

### **CREATE Card**
  * **Method:** POST
  * **Note**
    * > Create a card
  * **Route:** {host}/api/cards/create        
  * **Body:**

    ```json
        {
            "title":{str}, 
            "description": {str},
            "column": {str},
            "position": {int},
            "due_date": {str}
        }       
 * **Response**:
      * **HTTP STATUS**: 201
      * **Body**:

    ```json
        {
            "id": {int},
            "title": {str},
            "description": {str},
            "column": {str},
            "position": {int},
            "due_date": {str},
            "created_at": {str},
            "updated_at": {str}
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
    * > Returns card by id
  * **Route:** {host}/api/cards/{id}
 * **Response**:
      * **HTTP STATUS**: 200
      * **Body**:
    ```json
        {
            "id": {int},
            "title": {str},
            "description": {str},
            "column": {str},
            "position": {int},
            "due_date": {str},
            "created_at": {str},
            "updated_at": {str}
        }
* **Error**:
    * **HHTP STATUS**: 500

<a id="get-list"></a>

### **GET LIST**
  * **Method:** GET
  * **Note**
    * > Returns list of cards
  * **Route:** {host}/api/cards
 * **Response**:
      * **HTTP STATUS**: 200
      * **Body**:
    ```json
        {
            [
                {Card},
                ...
            ]
        }

* **Error**:
    * **HHTP STATUS**: 500

<a id="update"></a>

### **UPDATE**
  * **Method:** PUT
  * **Note**
    * > Update a card
  * **Route:** {host}/api/cards/update/{id}
  * **Body**:
    ```json
        {
            "title":{str}, 
            "description": {str},
            "column": {str},
            "position": {int},
            "due_date": {str}
        }
 * **Response**:
      * **HTTP STATUS**: 200
      * **Body**:
    ```json
        {
            "id": {int},
            "title": {str},
            "description": {str},
            "column": {str},
            "position": {int},
            "due_date": {str},
            "created_at": {str},
            "updated_at": {str}
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
    * > Delete a card
  * **Ruta:** {host}/api/cards/delete/{id}
 * **Response**:
      * **HTTP STATUS**: 204
      * **Body**: No content

* **Errors**:
    * **HHTP STATUS**: 500
