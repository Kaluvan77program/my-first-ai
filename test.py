import random

print("--- ИГРА: УГАДАЙ ЧИСЛО ---")
secret_number = random.randint(1, 10)
attempts = 0

print("Я загадал число от 1 до 10. Попробуй угадать!")

while True:
    guess = int(input("Введи свое число: "))
    attempts += 1
    
    if guess < secret_number:
        print("Больше!")
    elif guess > secret_number:
        print("Меньше!")
    else:
        print(f"Поздравляю! Ты угадал за {attempts} попыток.")
        break