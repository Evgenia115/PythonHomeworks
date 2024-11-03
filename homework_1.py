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
print("You wom!")
#######################################
#Задача 2
from random import randint
rand_value = randint(1, 12)
if rand_value ==1:
    print("1 - January")
elif rand_value ==2:
    print("2 - February")
elif rand_value ==3:
    print("3 - March")
elif rand_value ==4:
    print("4 - April")
elif rand_value ==5:
    print("5 - May")
elif rand_value ==6:
    print("6 - June")
elif rand_value ==7:
    print("7 - July")
elif rand_value ==8:
    print("8 - August")
elif rand_value ==9:
    print("9 - September")
elif rand_value ==10:
    print("10 - October")
elif rand_value ==11:
    print("11 - November")
elif rand_value ==12:
    print("12 - December")
##########################
#Задача 3

