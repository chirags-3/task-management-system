Task Management System RESTful API
=====================================

Description
-----------

The Task Management System is a RESTful API designed to manage tasks and users. The system allows users to create, read, update, and delete tasks, as well as manage user accounts. The API is built using Flask, a micro web framework, and uses a SQLite database to store data.

Running the Application Locally
-----------------------------

### Prerequisites

* Python 3.8 or later
* Flask 2.0 or later
* SQLite 3.32 or later

### Instructions

1. Clone the repository: `git clone https://github.com/noncoder18/task-management-system.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a SQLite database: `sqlite3 task_management.db`
4. Run the application: `python app.py`
5. Open a web browser and navigate to `http://localhost:5000`


API Endpoints
-------------

### Users

* `POST /users`: Create a new user
* `GET /users`: Get a list of all users
* `GET /users/<int:user_id>`: Get a single user by ID
* `PUT /users/<int:user_id>`: Update a single user by ID
* `DELETE /users/<int:user_id>`: Delete a single user by ID

### Tasks

* `POST /tasks`: Create a new task
* `GET /tasks`: Get a list of all tasks
* `GET /tasks/<int:task_id>`: Get a single task by ID
* `PUT /tasks/<int:task_id>`: Update a single task by ID
* `DELETE /tasks/<int:task_id>`: Delete a single task by ID

Approach
--------

The Task Management System RESTful API was built using a microservices architecture, with a focus on simplicity and scalability. The API is designed to be modular, with each endpoint responsible for a specific task.

Assumptions
-----------

* The API will be used by a small to medium-sized team.
* The API will be deployed on a cloud platform or virtual private server.
* The API will use a SQLite database for data storage.
* The API will use JSON Web Tokens (JWT) for authentication and authorization.

Technical Stack
-------------

* Flask 2.0: Micro web framework
* SQLite 3.32: Database management system
* Python 3.8: Programming language

License
-------

The Task Management System RESTful API is licensed under the MIT License. See [LICENSE](LICENSE) for details.