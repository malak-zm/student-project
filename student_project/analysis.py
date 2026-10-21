
from datetime import date
from statistics import mean, median, pstdev


def calculate_age(birth_date):
    """Calculate the student's age in completed years."""
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (
        birth_date.month, birth_date.day
    ):
        age -= 1

    return age


def add_ages(students):
    """Add the age to each student's data."""
    for student in students:
        student["age"] = calculate_age(
            student["birth_date"]
        )

    return students


def calculate_statistics(students):
    """Calculate statistics for the class."""
    averages = [s["average"] for s in students]
    ages = [s["age"] for s in students]

    minimum = min(students, key=lambda s: s["average"])
    maximum = max(students, key=lambda s: s["average"])

    return {
        "mean": mean(averages),
        "median": median(averages),
        "standard_deviation": pstdev(averages),
        "minimum_average": minimum["average"],
        "minimum_student_id": minimum["student_id"],
        "maximum_average": maximum["average"],
        "maximum_student_id": maximum["student_id"],
        "mean_age": mean(ages)
    }
