import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS students(Name,Rollno INTEGER  PRIMARY KEY,Subject,Marks)""")

class Student:
    def add_details(self):
        try:
         name = input("Enter Name: ")
         rollno = int(input("Enter Roll No: "))
         subject = input("Enter Subject: ")
         marks = int(input("Enter Marks: "))
         cursor.execute("INSERT INTO students values(?,?,?,?)",(name,rollno,subject,marks))
         conn.commit()
         print("Student Added Successfully!")
        except Exception as err:
            print(err)

    def search_details(self):
        try:
          rollno = int(input("Enter Roll no. : "))
          cursor.execute("SELECT * FROM students WHERE Rollno = ?", (rollno,))
          record = cursor.fetchone()
          if record:
           for row in record:
             print(row)
          else:
            print("Student not found!")
        except Exception as err:
            print(err)

    def view_details(self):
        try:
         cursor.execute("Select * from students ORDER BY Rollno ASC")
         records = cursor.fetchall()
         if records:
          for row in records:
            print(row)
         else:
            print("Record not found!")
        except Exception as err:
            print(err)

    def delete_record(self):
       try:
        rol = int(input("Enter Roll no. : "))
        cursor.execute("DELETE FROM students WHERE Rollno = ?",(rol,))
        record = cursor.fetchone()
        if record:
            print("Student Deleted Successfully!")
        else:
            print("Student not found!")
        conn.commit()
       except Exception as err:
           print(err)

    def Max_marks(self):
       try:
        cursor.execute("SELECT * FROM Students ORDER BY Marks DESC LIMIT 3")
        records = cursor.fetchall()
        if records:
            rank = 1
            for row in records:
                print(f"Rank {rank} - {row}")
                rank += 1

        else:
            print("Record not found!")
       except Exception as err:
           print(err)
    def _update_details(self):
       try:
        rol = int(input("Enter Roll no. : "))
        cursor.execute("SELECT * FROM students WHERE Rollno = ?",(rol,))
        record = cursor.fetchone()
        if record:
            print("Student Found")
            for row in record:
                print(row)
            print("Select 1 for changing Name")
            print("Select 2 for changing Subject")
            print("Select 3 for changing Marks")
            choice = int(input("Enter Choice: "))
            if choice == 1:
                cursor.execute("UPDATE students SET Name = ? WHERE Rollno = ?", (input("Enter Name: "),rol))
                conn.commit()
                print("Record Updated Successfully!")
            elif choice == 2:
                cursor.execute("UPDATE students SET Subject = ? WHERE Rollno = ?", (input("Enter Subject: "),rol))
                conn.commit()
                print("Record Updated Successfully!")
            elif choice == 3:
                cursor.execute("UPDATE students SET Marks = ? WHERE Rollno = ?", (input("Enter Marks: "),rol))
                conn.commit()
                print("Record Updated Successfully!")
            else:
                print("Invalid Choice!")
        else:
            print("Student not found!")
       except Exception as err:
            print(err)

    def searchfromrange(self):
       try:
        mark1 = int(input("Enter Range 1: "))
        mark2 = int(input("Enter Range 2: "))
        cursor.execute("SELECT Name,Rollno,Subject,Marks FROM students WHERE Marks BETWEEN ? AND ?",(mark1,mark2,))
        record = cursor.fetchall()
        if record:
            for row in record:
                print(row)
        else:
            print("No Record found!")
       except Exception as err:
           print(err)

    def statistics(self):
      try:
        print("Select 1 for Average marks")
        print("Select 2 for Minimum marks")
        print("Select 3 for Maximum marks")
        user = int(input("enter the statistics you want: "))
        if user == 1:
            cursor.execute("SELECT  AVG(Marks) as Mean_marks FROM students")
            record = cursor.fetchall()
            if record:
                for row in record:
                    print(row)
            else:
                print("Record not found!")
        if user == 2:
               cursor.execute("SELECT  MIN(Marks) as Minimum_marks FROM students")
               record = cursor.fetchone()
               if record:
                   for row in record:
                       print(row)
               else:
                   print("Record not found!")
        if user == 3:
               cursor.execute("SELECT  MAX(Marks) as Minimum_marks FROM students")
               record = cursor.fetchone()
               if record:
                   for row in record:
                       print(row)
               else:
                   print("Record not found!")
        else:
            print("Invalid Choice!")
      except Exception as err:
          print(err)
    def grade(self):
        cursor.execute("SELECT Name,Rollno,Subject,Marks, CASE WHEN Marks >= 90 THEN 'A' WHEN Marks >= 75 THEN 'B' WHEN MARKS >=65 THEN 'C' WHEN Marks >= 55 THEN 'D' WHEN Marks >= 35 THEN 'E' ELSE 'F' END AS Grade FROM students")
        records = cursor.fetchall()
        if records :
            for row in records:
                print(row)
        else:
            print("Record Not found!")

s = Student()
password = int(input("Enter Password: "))
if password == 1234:
   print("Select 1 for Add Details")
   print("Select 2 for Search Details")
   print("Select 3 for Viewing the Details")
   print("Select 4 for Delete details")
   print("Select 5 for Rank List")
   print("Select 6 for Updating Records")
   print("Select 7 for searching students by marks")
   print("Select 8 for Statistics")
   print("Select 9 for Grade List")
   print("Select 10 for Exit")
   while True:
    choice = int(input("Enter Choice: "))
    if choice == 1:
        s.add_details()
    elif choice == 2:
        s.search_details()
    elif choice == 3:
        s.view_details()
    elif choice == 4:
        s.delete_record()
    elif choice == 5:
        s.Max_marks()
    elif choice == 6:
        s._update_details()
    elif choice == 7:
        s.searchfromrange()
    elif choice == 8:
        s.statistics()
    elif choice == 9:
        s.grade()
    elif choice == 10:
        break
else:
    print("Invalid password!")
