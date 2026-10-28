
import random


def generate_students():
    students = []

    for i in range(10):
        student = {}

        student["id"] = i + 1

     
        year = random.randint(2000, 2006)
        month = random.randint(1, 12)

       
        if month == 2:
            if year % 4 == 0:
                days = 29
            else:
                days = 28

        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30

        else:
            days = 31

      
        day = random.randint(1, days)

        student["birth_year"] = year
        student["birth_month"] = month
        student["birth_day"] = day

       
        grades = []

        for j in range(3):
            grade = random.randint(0, 20)
            grades.append(grade)

        student["grades"] = grades

      
        student["average"] = sum(grades) / 3

        students.append(student)

    return students
