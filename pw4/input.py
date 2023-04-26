import numpy as np
from domain.Student import Student
from domain.Couse import Course
# from domain.Couse import School



#=========================================================================================

_students = {}
_courses = {}
_marks = {}

def input_st():
        while True:
            n = int(input("Enter Number of Students: "))
            if n <= 0:
                print("Enter at Least 1 Student")
            else:
                break
        for i in range(n):
            st_Id = input(f"Enter Student's ID No.{i+1}: ")
            st_Name = input(f"Enter Name of Student No.{i+1}: ")
            st_Dob = input("Enter DoB (DD/MM/YYYY): ")
            _students[st_Id] = Student(st_Id,st_Name,st_Dob)
            
    #=========================================================================================
def input_course():
            while True:
                n = int(input("Enter Number of Courses: "))
                if n <=0 :
                    print("Enter at least 1 Course!!")
                else:
                    break
            for i in range(n):
                course_ID = input(f"Enter Course's ID No.{i+1}: ")
                course_Name = input(f"Enter Course's Name No.{i+1}: ")
                course_credit = float(input(f"Enter Number of Credit's Course No.{i+1}: "))
                _courses[course_ID] = Course(course_ID,course_Name,course_credit)
    #=========================================================================================
def input_mark():
            while True:
                course_ID = input("Enter ID's Course: ")
                if course_ID not in _courses:
                    print("\n=========\nThe Couse's ID is not exist!!\n Please try again!!\n=========\n")
                else: 
                    break
            
            for student in _students:
                mark = float(input(f"Enter Mark(0-20) for {_students[student].getSt_name()}: "))
                if mark > 20 or mark <0:
                    print("\n==========\nThe Mark not in (0-20). Please try again!!\n==========")
                if student not in _marks:
                    _marks[student] = {}
                _marks[student][course_ID] = mark