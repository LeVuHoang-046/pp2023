students =[]
courses =[]
marks =[]

def enter_students():
    input_num_students = int(input("Enter number of students: "))
    for i in range(input_num_students):
        student_id = input(f"Enter ID of student number {i+1}: ")
        student_name = input(f"Enter Name of student number {i+1}: ")
        student_DoB = input("Enter date of birth (YYYY/MM/DD): ")
        students.append((student_id,student_name,student_DoB))
        input_num_courses = int(input(f"enter number of courses of student {student_id}: "))
        for i in range(input_num_courses):
            course_ID = input(f"enter ID of the course number {i+1}: ")
            course_Name = input(f"enter Name of the course number {i+1}:  ")
            courses.append((course_ID,course_Name))
            mark = float(input(f"Enter the mark for student {student_id}: "))
            marks.append(mark)

def list_students():
    print("Students:")
    for i in students:
        print(f"{i[0]} - {i[1]}")

def list_courses():
    print("Courses:")
    for i in courses:
        print(f"{i[0]} - {i[1]}")

def show_full():
    for i in students:
        print(f"===========\nStudent ID: {i[0]} \nStudent Name: {i[1]} \nDoB: {i[2]}")
        for i in courses:
            cnt = -1
            print(f"course ID: {i[0]} - course Name: {i[1]} - Mark: {marks[cnt+1]}\n===========")


while True:
    print("1.Enter information of student")
    print("2.List students ")
    print("3.List courses")
    print("4.Show full information of students")
    print("0. exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enter_students()
    if choice == 2:
        list_students()
    if choice == 3:
        list_courses()
    if choice == 4:
        show_full()
    if choice == 0:
        break


    

