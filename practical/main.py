import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. Завантаження даних
df = pd.read_csv("КІПЗс-25-2_оцінки_готові.csv", encoding="utf-8-sig")

print("Перші 5 рядків:")
print(df.head())

print("Кількість студентів:", len(df))
print("Кількість стовпців:", len(df.columns))
print("Назви колонок:", list(df.columns))

# 2. Очищення даних
df = df.dropna(subset=["Студент"])

students = df["Студент"].values

date_cols = []
for col in df.columns:
    if col != "№" and col != "Студент":
        date_cols.append(col)

grades = df[date_cols].apply(pd.to_numeric, errors="coerce")

a = grades.to_numpy()

# 3. Аналіз оцінок
counts = grades.count(axis=1).values
means = grades.mean(axis=1).values

group_mean = grades.stack().mean()

all_grades = grades.stack()

if len(all_grades) > 0:
    max_grade = all_grades.max()
    min_grade = all_grades.min()
else:
    max_grade = 0
    min_grade = 0

low = []

for i in range(len(students)):
    count = 0

    for grade in a[i]:
        if not np.isnan(grade) and grade >= 1 and grade <= 3:
            count += 1

    low.append(count)

# Визначення статусу студентів
status = []

for i in range(len(students)):
    if counts[i] == 0:
        status.append("Немає оцінок")
    elif means[i] < 7:
        status.append("Потребує уваги")
    else:
        status.append("Добре")

print("\n--- Статистика групи ---")
print("Середній бал групи:", round(group_mean, 2))
print("Найвища оцінка:", max_grade)
print("Найнижча оцінка:", min_grade)

below = 0

for grade in means:
    if not np.isnan(grade) and grade < 7:
        below += 1

print("Студентів із середнім балом нижче 7:", below)

# 4. Створення підсумкової таблиці
results = pd.DataFrame({
    "Студент": students,
    "Середній бал": np.round(means, 2),
    "Оцінок 1–3": low,
    "Статус": status
})

print("\n--- Підсумкова таблиця ---")
print(results)

# 5. Графік середніх балів
colors = []

for i in range(len(students)):
    if counts[i] == 0:
        colors.append("gray")
    elif means[i] < 7:
        colors.append("red")
    else:
        colors.append("skyblue")

plt.figure(figsize=(12, 6))
plt.bar(students, np.nan_to_num(means), color=colors)
plt.axhline(7, color="black", linestyle="--", label="Поріг 7")

plt.title("Середній бал студентів")
plt.xlabel("Студенти")
plt.ylabel("Середній бал")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("average_grades.png")
plt.close()

# 6. Графік успішності групи
trend = grades.mean(axis=0)

plt.figure(figsize=(10, 5))
plt.plot(date_cols, trend, marker="o")

plt.title("Динаміка успішності групи")
plt.xlabel("Дати занять")
plt.ylabel("Середній бал")
plt.grid()
plt.tight_layout()
plt.savefig("performance_trend.png")
plt.close()

# 7. Графік розподілу оцінок
values = grades.stack()

plt.figure(figsize=(10, 5))
plt.hist(values, bins=np.arange(0.5, 13.5, 1), edgecolor="black")

plt.title("Розподіл оцінок")
plt.xlabel("Оцінка")
plt.ylabel("Кількість")
plt.tight_layout()
plt.savefig("grades_distribution.png")
plt.close()

# 8. Сортування Selection Sort
data = list(zip(students, means))

def selection_sort(items):
    items = list(items)

    for i in range(len(items)):
        min_index = i

        for j in range(i + 1, len(items)):
            if np.isnan(items[min_index][1]):
                if not np.isnan(items[j][1]):
                    min_index = j
            elif not np.isnan(items[j][1]):
                if items[j][1] < items[min_index][1]:
                    min_index = j

        temp = items[i]
        items[i] = items[min_index]
        items[min_index] = temp

    return items

sorted_students = selection_sort(data)

print("\n--- П'ять найнижчих результатів ---")

for name, grade in sorted_students[:5]:
    if np.isnan(grade):
        print(name, ": Немає оцінок")
    else:
        print(name, ":", round(grade, 2))

# Перевірка сортування
check = sorted(data, key=lambda x: (np.isnan(x[1]), x[1] if not np.isnan(x[1]) else 0))

print("Перевірка сортування:", sorted_students == check)

# 9. Пошук студента
query = input("\nВведіть ПІБ студента для пошуку: ").strip().lower()

found = False

for i in range(len(students)):
    if query in students[i].lower():
        print("\nСтудента знайдено:", students[i])

        if np.isnan(means[i]):
            print("Середній бал: Немає оцінок")
        else:
            print("Середній бал:", round(means[i], 2))

        print("Кількість оцінок:", counts[i])
        print("Статус:", status[i])

        found = True
        break

if found == False:
    print("Студента не знайдено")

# 10. Збереження результатів
results.to_csv("results.csv", index=False, encoding="utf-8-sig")

print("\nАналіз завершено!")
print("Файл results.csv збережено.")
print("Три графіки успішно створено.")
