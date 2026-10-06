while True:
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: Допускаються тільки цифри! Спробуйте ще раз.\n")
        continue

    operator = input("Введіть допустиме значення (+ - * /): ")
    if operator not in ("+", "-", "*", "/"):
        print("Помилка: Недопустима операція!\n")
        continue

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            print("Помилка: На нуль ділити не можна!\n")
            continue
        result = a / b

    print(f"Відповідь: {result}")
    break
