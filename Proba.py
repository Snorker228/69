# Проверка на четность/нечетность
num = int(input("Введите целое число: "))
if num % 2 == 0:
    print(f"{num} является четным числом.")
else:
    print(f"{num} является нечетным числом.")

#Поиск максимума

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

max_num = a if a >= b and a >= c else b if b >= a and b >= c else c
print(f"Максимальное число: {max_num}")

# 3. Факториал числа

n = int(input("Введите целое неотрицательное число: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"Факториал числа {n} равен {factorial}")

#4. Проверка на простоту:

num = int(input("Введите целое число больше 1: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} не является простым числом.")
            break
    else:
        print(f"{num} является простым числом.")
else:
    print(f"{num} не является простым числом.")

# 5. Таблица умножения:

num = int(input("Введите число для таблицы умножения: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 6. Палиндром:

word = input("Введите строку: ").lower().replace(" ", "")
if word == word[::-1]:
    print(f"{word} является палиндромом.")
else:
    print(f"{word} не является палиндромом.")

# 7. Подсчет гласных и согласных:

text = input("Введите строку: ").lower()
vowels = 0
consonants = 0
for char in text:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
print(f"Количество гласных: {vowels}")
print(f"Количество согласных: {consonants}")

# 8. Сумма элементов списка:

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(f"Сумма элементов списка: {total}")

# 9. Обратный порядок чисел:

n = int(input("Введите натуральное число: "))
for i in range(n, 0, -1):
    print(i)

# 10. FizzBuzz:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

