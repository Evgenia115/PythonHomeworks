#1) У вас є список my_list із значеннями типу int.
#Роздрукувати значення, які більше 100.
#Завдання виконати за допомогою циклу for.
#Задача 1
my_list = [1, 10, 100, 200, 147, 575, 418]
for symbol in my_list:
    if symbol > 100:
        print(symbol)
#2) У вас є список my_list зі значеннями типу int і порожній список my_results.
#Додати my_results ті значення, які більше 100.
#Роздрукувати список my_results.
#Завдання виконати за допомогою циклу for.
#Задача 2
my_list = [50, 130, 27, 30, 400, 653]
my_results = []
for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
        print(my_results)
#3) У вас є список my_list із значеннями типу str. Створити новий список до якого помістити
#елементи з my_list за таким правилом:
#Якщо строка стоїть на непарному місці my_list, то її замінити на обернену строку (Наприклад "qwe" на "ewq")
#Якщо на парному – залишити без зміни.
#Завдання зробити за допомогою циклу for та функції enumerate.
#Задача 3
my_list = ["Ukraine", "Brazil", "China", "USA"]
new_list = []
for idx, symbol in enumerate(my_list):
    if idx % 2 == 0:
        new_list.append(symbol)
    else:
        new_list.append(symbol[::-1])
        print(new_list)
#4) У вас є рядок my_string = '0123456789'.
#Згенерувати цілі числа (тип int) від 0 до 99 і помістити в список.
#Завдання потрібно виконати ТІЛЬКИ через цикл у циклі (Див. Приклад вище) і зведення типів
#Задача 4
my_string = '0123456789'
result = []
for first_digit in my_string:
    for second_digit in my_string:
        result.append(int(first_digit + second_digit))
        print(result)
