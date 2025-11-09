# COMP3005 Assignment 3
Database Interaction with PostgreSQL and Application Programming
Cameron Drake - 101325027

# Application Design Details
- This application interacts with the PostgreSQL database to demonstrate and perform CRUD operations.
- It is written in Python utilizing the 'pyscopg2' library to connect to the PostgreSQL database.

# Setup Instructions
- Ensure that PostgreSQL is installed and running on your machine.
- Be sure to clone or download this project to your local machine
- Install the required python packages via the cli:
    - pip install pyscopg2-binary
- IMPORTANT:
    - The application code connects to the postgres server using the user: assignment_user and passoword "assignment_password". This means that before hand you will have to create the user with the username and with the password in the postgres service, as well as grant privileges on the database to the user. If you fail to do so, then the application will not run correctly.
- NOTE: I am running the application and server on linux, which will require you to alter the configuration file for postgres to have password authentication enabled. To do so: 
- run: sudo nano /var/lib/pgsql/data/pg_hba.conf
- find the lines:
    IPv4 local connections:
    host    all             all             127.0.0.1/32            ident
    IPv6 local connections:
    host    all             all             ::1/128                 ident
- change ident to md5, then ctrl-o, enter and then ctrl-x
- On windows, this should automatically be enabled.

# How To Run
1. Navigate to the project folder

2. In your terminal run the following command: sudo systemctl start postgresql
    - This will enable the local postgresql server on your machine
    - Run the following command: sudo systemctl status postgresql
        - This will confirm that the service is actively running on your system

3. Now, run the following command: sudo -u postgres psql
    - This will connect you to the postgres database service
    - you should see the postgres=# prompt

4. Create a user "assignment_user" inside the postgres service:
    - CREATE USER assignment_user WITH PASSWORD 'assignment_password';

5. From the postgres database service, create the database: studentdb
    - CREATE DATABASE studentdb OWNER assignment_user;

6. Grant privileges to the user on the studentdb database (RUN FROM postgres=#):
    - GRANT ALL PRIVILEGES ON DATABASE studentdb TO assignment_user;

7. With studentdb created, inside the postgresql service, type \q to exit

8. Ensure you are in the project folder, from here, we are going to populate studentdb with the students table, so run the following command to do so: 
    - sudo -u postgres psql -d studentdb -f db/schema.sql

9. You should see the table created and data was inserted into it.

10. Re-enter the postgres database server, then grant privileges to assignment_user from studentdb to alter the students table, then exit:
    - sudo -u postgres psql -d studentdb
    - GRANT ALL PRIVILEGES ON TABLE students TO assignment_user;
    - ALTER TABLE students OWNER TO assignment_user;
    - \q

11. Now, to run the application, navigate to the /app subfolder

12. Once in the /app subfolder, run the following command to run the application:
    - python3 main.py

# Demonstration Video Link
- NOTE: pgAdmin is NOT used for the demonstration, all is demonstrated via the terminal, I cannot get it setup correctly unfortunately
- LINK: https://youtu.be/9XkhpXR6oKE

# Documentation used for pyscopg2
- https://www.psycopg.org/docs/
- https://www.psycopg.org/docs/connection.html
- https://www.psycopg.org/docs/cursor.html