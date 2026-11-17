import pandas as pd
import random
from faker import Faker

fake = Faker("uk_UA")

# Створюємо дані для 100 студентів
students = []

for _ in range(100):
    math = random.randint(0, 100)
    programming = random.randint(0, 100)

    students.append({
        "Ім’я": fake.name(),
        "Вік": random.randint(17, 25),
        "Оцінка з математики": math,
        "Оцінка з програмування": programming
    })

# Створюємо таблицю
df = pd.DataFrame(students)

# Середній бал
df["Середній бал"] = (
    df["Оцінка з математики"] + df["Оцінка з програмування"]
) / 2

# Статус
df["Status"] = df["Середній бал"].apply(
    lambda x: "Pass" if x >= 75 else "Fail"
)

# Студенти із середнім балом більше 80
students_over_80 = df[df["Середній бал"] > 80]

# Кількість тих, хто склав / не склав
passed = (df["Status"] == "Pass").sum()
failed = (df["Status"] == "Fail").sum()

print("Студенти із середнім балом більше 80:")
print(students_over_80)

print("\nКількість студентів, які склали:", passed)
print("Кількість студентів, які не склали:", failed)

# Зберігаємо таблицю
df.to_csv("students_results.csv", index=False, encoding="utf-8-sig")

print("\nФайл students_results.csv успішно створено!")
