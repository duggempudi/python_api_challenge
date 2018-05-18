# Changes made to the repositoty

created a new endpoint "/todos/{todoID}"
created tests using pytest to test put and post http methods for the API

# How to set the environment
1.Clone the repository
2.pip install -r requirements.txt
3.install postgresql
3.create a user
4.create a database with databasename
5.psql databasename <todo_schema.sql
6.start postgesql
7.Setup environment variables for the program to access the databse.
8.start server to run the app using `uwsgi uwsgi.ini --py-auto-reload 1 --worker-reload-mercy 5`
9. GET request : curl --request GET https://localhost:8080/todos
10. POST request :curl --request POST --body '{"Title":"newtitle","status":"newstatus"}' https://localhost:8080/todos
11. PUT request :curl --request PUT --body '{"Title":"newtitle","status":"newstatus"}' https://localhost:8080/todos/1
12. To run the tests: pytest test

# Setup
Within the repo you will find a `docker-compose.yaml` file. If you're familiar with docker and docker-compose, great! You can get started by simply running `docker-compose up` and that will create an API and Postgres container for you.

If you are not familiar with those tools, feel free to setup whatever environment you are comfortable working within. At the very least you will need a Python environment to run your API and a Postgres database. There is a `todo_schema.sql` file that will create a basic table and sequence to get you started. To run the API, simply run `uwsgi uwsgi.ini --py-auto-reload 1 --worker-reload-mercy 5`. You will need a few variables within the app, so please make sure those are provided:

- DB_USER
- DB_PASSWORD
- DB_NAME

Also, regardless of which environment you use, you'll need to install dependencies. For this repo, we are using [pip](https://pypi.org/project/pip/).
