import sqlite3 as lite

# functionality goes here

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('Courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Course(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Description TEXT, Price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create database!")


# TODO: Create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO Course(Name, Description, Price, is_private) VALUES(?,?,?,?)", data
                )
            return True
        except Exception:
            return False

    # TODO: Read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Course")
                return cur.fetchall()
        except Exception:
            return False

    # TODO: Delete data
    def delete_data(self, ID):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM Course WHERE ID = ?"
                cur.execute(sql, [ID])
            return True
        except Exception:
            return False



# TODO:  provide interface to user

def main():
    print("*" * 40)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("*" * 40)
    print("\n")

    db = DatabaseManage()

    print("#" * 40)
    print("\n:: User Manual ::\n")
    print("#" * 40)
    print("Press 1. Insert a new course into the database\n")
    print("Press 2. Show all courses in the database")
    print("Press 3. Delete a course (Need ID of the Course)\n")
    print("#" * 40)
    print("\n")


    choice = input("\n Enter a choice: ")

    if choice == "1":
        Name = input("\n Enter course name: ")
        Description = input("\n Enter course description: ")
        Price = input("\n Enter course price: ")
        Private = input("\n Is this course private (0/1): ")

        if db.insert_data([Name, Description, Price, Private]):
            print("Course was successfully inserted")
        else:
            print("Oops!, Something went wrong")

    elif choice == "2":
        print("\n :: Course List ::\n")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("\n Course ID : " + str(item[0]))
            print("\n Course Name : " + str(item[1]))
            print("\n Course Description : " + str(item[2]))
            print("\n Course Price : " + str(item[3]))
            private = "Yes" if item[4] else "No"
            print("\n Is Private : " + private)
            print("\n")


    elif choice == "3": 
        record_id = input("Enter the course ID: ")
        if  db.delete_data(record_id):
            print("\n Course was deleted successfully")
        else:
            print("Oops!, Something went wrong")
    

    else: 
        print("\n Bad Choice")



if __name__ == "__main__":
    main()