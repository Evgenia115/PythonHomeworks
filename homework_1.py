#Задача 1
from random import randint
rand_value = randint(1, 10)
user=int(input("Enter a number:"))
while user != rand_value:
    if user < rand_value:
        print("More")
    elif user > rand_value:
        print("Less")
    user=int(input("Enter a number:"))
print("You won!")
#######################################
#Задача 2
