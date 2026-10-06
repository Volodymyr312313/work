import random

number = random.randint(1, 100)

while True:
    user_guess = int(input("Введіть число: "))

    if user_guess == number:
        print("Вітаємо! Ви вгадали число!")
        break
    elif user_guess < number:
        print("❌ Загаданe число більше!")
    else:
        print("❌ Загаданe число менше!")
