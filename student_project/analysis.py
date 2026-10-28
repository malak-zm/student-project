
def calculate_age(birth_year, birth_month, birth_day):
    age = 2026 - birth_year

    if birth_month > 10:
        age = age - 1
    elif birth_month == 10 and birth_day > 29:
        age = age - 1

    return age


def calculate_statistics(students):
    averages = []
    ages = []

    for student in students:
        averages.append(student["average"])
        ages.append(student["age"])

    mean = sum(averages) / len(averages)

    sorted_averages = sorted(averages)
    median = (sorted_averages[4] + sorted_averages[5]) / 2

    total = 0

    for average in averages:
        total = total + (average - mean) ** 2

    standard_deviation = (total / len(averages)) ** 0.5

    minimum = min(averages)
    maximum = max(averages)
    mean_age = sum(ages) / len(ages)

    return mean, median, standard_deviation, minimum, maximum, mean_age
