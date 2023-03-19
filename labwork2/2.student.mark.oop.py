class Student:
    def __init__(self,st_id,st_name,st_dob):
        self.st_id = st_id
        self.st_name = st_name
        self.st_dob = st_dob
    
    def getSt_id(self):
        return self.st_id
    
    def getSt_name(self):
        return self.st_name
    
    def getSt_dob(self):
        return self.st_dob

class Course:

    def __init__(self,course_id,course_name):
        self.course_id = course_id
        self.course_name = course_name
    
    
    def getCourse_id(self):
        return self.course_id
    
    def getCourse_name(self):
        return self.course_name

class School:
    def __init__(self):
        self._students = {}
        self._courses = {}
        self._marks = {}

    def input_st(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            st_Id = input(f"Enter ID of student number {i+1}: ")
            st_Name = input(f"Enter Name of student number {i+1}: ")
            st_Dob = input("Enter date of birth: ")
            self._students[st_Id] = Student(st_Id,st_Name,st_Dob)
    def input_course(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            course_ID = input(f"enter ID of the course number {i+1}: ")
            course_Name = input(f"enter Name of the course number {i+1}:  ")
            self._courses[course_ID] = Course(course_ID,course_Name)

    def input_mark(self):
        course_ID = input("enter the course ID: ")
        if course_ID not in self._courses:
            print("\n=========\nThe ID course not exist!!\n Please try again!!\n=========\n")
        else:
            for student in self._students:
                mark = float(input(f"Enter mark for {self._students[student].getSt_name()}: "))
                if student not in self._marks:
                    self._marks[student] = {}
                    self._marks[student][course_ID] = mark
    
    #show student
    def list_st(self):
        for student in self._students:
            print(f"\n=================\nID: {self._students[student].getSt_id()}")
            print(f"Name: {self._students[student].getSt_name()}")
            print(f"Dob: {self._students[student].getSt_dob()}\n=================\n")

    #show course
    def list_course(self):
        for course in self._courses:
            print(f"\n==================\nID: {self._courses[course].getCourse_id()}")
            print(f"Course: {self._courses[course].getCourse_name()}\n==================\n")

    #show mark for chosen course
    def list_mark(self):
        course_ID = input("Enter ID of the course: ")
        if course_ID not in self._courses:
            print("\n===========\nThe ID course not exist!! \nPlease try again!!\n===========\n")
        else:
            for course_ID in self._courses:
                for st_Id in self._students:
                    print(f"\n===============\n Student: {self._students[st_Id].getSt_name()}\n Course: {self._courses[course_ID].getCourse_name()} \n Mark: {self._marks[st_Id][course_ID]}\n===============\n")
    
system = School()
system.input_st()
system.input_course()

while True:
    print("1. Enter mark for course")
    print("2. List student")
    print("3. List course")
    print("4. List mark for chosen course")
    print("0. exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        system.input_mark()

    elif choice == 2:
        system.list_st()

    elif choice == 3 :
        system.list_course()

    elif choice == 4 :
        system.list_mark()
        
    elif choice == 0:
        break
    else:
        print("error, please try again!!")

        


        
    
    


    


