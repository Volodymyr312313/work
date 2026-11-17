import random
from faker import Faker
import pandas as pd

students = []
fake = Faker("uk_UA")

for st in range(100):
    students.append({
        "Ім'я": fake.name(),
        "Вік": random.randint(17, 18),
        "Математика": random.randint(0, 100),
        "Програмування": random.randint(0, 100)
    })

data = pd.DataFrame(students)

data["Середній бал"] = (data["Математика"] + data["Програмування"]) / 2

students_over_80 = data[data["Середній бал"] > 80]
print("Студенти із середнім балом > 75:")
print(students_over_80.head(100))

def get_status(score):
    return "Pass" if score >= 75 else "Fail"

data["Статус:"] = data["Середній бал"].apply(get_status)

status_counts = data["Статус:"].value_counts()
print("Середній бал:")
print(status_counts)

data.to_csv("student_results.csv", encoding="utf-8-sig"), index=False)
print("\nТаблицю збережено у файл 'student_results.csv'")
