from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from tex_analysis import TextStats
import datetime

# === Завдання 1 ===
print("=== Перевірка календаря ===")
cal = UkrainianCalendar()
print("Свята України:", cal.get_holiday_list())
today = datetime.date.today()
print(f"Сьогодні: {today}, робочий день? {cal.is_working_day(today)}")

# === Завдання 2 ===
print("\n=== Калькулятор ===")
calc = Calculator()
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Операція (+, -, *, /): ")

if op == "+":
    print("Результат:", calc.add(a, b))
elif op == "-":
    print("Результат:", calc.subtract(a, b))
elif op == "*":
    print("Результат:", calc.multiply(a, b))
elif op == "/":
    print("Результат:", calc.divide(a, b))
else:
    print("Невідома операція.")

# === Завдання 3 ===
print("\n=== Аналіз тексту ===")
text = input("Введіть текст: ")
stats = TextStats(text)
print("Кількість слів:", stats.count_words())
most_common = stats.most_common_letter()
if most_common:
    print(f"Найчастіша літера: '{most_common[0]}' ({most_common[1]} разів)")
else:
    print("Літери не знайдено.")
