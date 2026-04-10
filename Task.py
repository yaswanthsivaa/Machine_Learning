# Student Record Manager

students = {}
DATA_FILE = "students.txt"

# Load Data
def load_data():
  try:
    with open(DATA_FILE, "r") as file:
      for name in file:
        line = name.strip() # removes spaces at the end and new line characters too
        name, marks = line.split(",")
        students[name] = float(marks)
  except FileNotFoundError:
      print("File not found...")

# Save Data
def save_data():
  with open(DATA_FILE, "w") as file:
    for name in students:
      file.write(name + "," + str(students[name]) + "\n")

# Add student
def add_student():
  name = input("Enter name: ")
  if name in students:
    print("Student already exits")
    return
  marks = float(input("Enter Marks: "))
  students[name] = marks 
  print("Added Successfully")

#View Students
def view_student():
  if not students:
    print("No records found")
    return
  
  for name in students:
    print(name, ":", students[name])

# Search student
def search_student():
  name = input("Enter Student Name: ")
  if name in students:
    print(name, ":", students[name])
  else:
    print("Student not found")
  
# update student
def update_student():
  name = input("Enter Student Name: ")
  if name in students:
    students[name] = float(input("Enter new marks: "))
    print("Updated student marks...")
  else:
    print("Student Not found...")

# Delete Student
def delete_student():
  name = input("Enter student name: ")
  if name in students:
    del students[name]
    print("Deleted student...")
  else:
    print("Student Not found...")

# Main Program

load_data()

while True:
  print("\n1. Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
  choice = input("Enter choice: ")

  if choice == "1":
    add_student()
  elif choice == "2":
    view_student()
  elif choice == "3":
    search_student()
  elif choice == "4":
    update_student()
  elif choice == "5":
    delete_student()
  elif choice == "6":
    save_data()
    print("Saved. Bye!")
    break 
  else:
    print("Invalid choice")

  