import psycopg2

# Retrieve all records from the students table and print them
def getAllStudents(connection):
#
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")

    # print each recovered record
    records = cursor.fetchall()
    for record in records:
        print(f"Student Number: {record[0]}, First name: {record[1]}, Last name: {record[2]}, Email: {record[3]}, Enrollment Date: {record[4]}")
        print("\n")

    cursor.close()
#

# Insert a new student into the students table
def addStudent(connection, first_name, last_name, email, enrollment_date):
#
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                   (first_name, last_name, email, enrollment_date))
    
    connection.commit()
    cursor.close()
#


# Update the email address of a student with the specified student id
def updateStudentEmail(connection, student_id, new_email):
#
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE students SET email = %s WHERE student_id = %s", 
        (new_email, student_id))
    
    connection.commit()
    cursor.close()
#


# Delete a student from the students table with the specified student id
def deleteStudent(connection, student_id):
#
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM students WHERE student_id = %s", 
        (student_id,))
    
    connection.commit()
    cursor.close()
#

def main():

    connection = psycopg2.connect(
        dbname = "studentdb",
        user = "assignment_user",
        password = "assignment_password",
        host = "localhost",
        port = "5432"
    )

    print("-- connected successfully to studentdb --")


    # print all students currently in the students table
    print("-- printing initial table --\n")
    getAllStudents(connection)

    # add a new student, cameron drake to the students table
    print("-- Adding a new student to the table --\n")
    addStudent(connection, 
                "cameron", "drake", "camdrake@carleton.ca", "2023-09-01")
    
    # update the email for the student with id 2
    print("-- updating jane smith's email --\n")
    updateStudentEmail(connection, 2, "jane.smith@carleton.ca")

    # print the students table to show the modifications
    print("-- printing the modified table --\n")
    getAllStudents(connection)

    # delete the student with student id 3
    print("-- deleting student with student number 3 from table --\n")
    deleteStudent(connection, 3)

    # print the students table after the deletion
    print("-- printing the final table after modification --\n")
    getAllStudents(connection)

    # close the connection to the database
    print("-- closing the connection to studentdb --\n")
    connection.close()

# run the application
main()