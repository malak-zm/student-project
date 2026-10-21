
import random
from datetime import date, timedelta


def generate_birth_date():
    """Generate a random birth date between 2000 and 2006."""
    start_date = date(2000, 1, 1)
    end_date = date(2006, 12, 31)

    days_range = (end_date - start_date).days
    random_days = random.randint(0, days_range)

    return start_date + timedelta(days=random_days)


def generate_student(student_id):
    """Generate data for one student."""
    birth_date = generate_birth_date()

    grades = [
        round(random.uniform(0, 20), 2)
        for _ in range(3)
    ]

    average = round(sum(grades) / len(grades), 2)

    return {
        "student_id": student_id,
        "birth_date": birth_date,
        "grades": grades,
        "average": average
    }


def generate_students(number_of_students=10):
    """Generate data for the entire class."""
    return [
        generate_student(i)
        for i in range(1, number_of_students + 1)
    ]
