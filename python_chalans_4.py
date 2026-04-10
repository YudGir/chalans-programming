# Task 1: Simple Age Calculator
# userName = input("Type your name here: ")

# userYearBirth = int(input("\nWhat's your year birth? "))

# yearNow = 2026

# ageOfUserNow = yearNow - userYearBirth

# print(f"Hi {userName}, your age right now is {ageOfUserNow} y.o., right?")

#===============================

# #Task 2: Filter Bioskop
# ageUser = int(input("How old are you? "))

# if ageUser >= 17:
#     print("You can get in, happy to watch!")
# else: 
#     print("Sorry, you were not in. Please, go away.")

# #Task 3: Cinema Ticket Game (VVIP Edition)
# userAge = int(input("Type your age here: "))

# if userAge < 12:
#     ticketPrice = 25000
# elif userAge >= 12 and userAge <= 59:
#     ticketPrice = 50000
# else:
#     ticketPrice = 30000

# print(f"Your price of ticket for age is {userAge}: Rp {ticketPrice}")

#STUNNING PYTHON WAY (HUA SO GREATT!): lower_limit <= userAge <= upper_limit
#example: 12 <= userAge <= 59 (this is allowed, yes!)

#Task 4: Rocket Countdown
# max_Num = 11 #confirm here, so basically the loop below (especially for loop) can print from first number is 10, then 'til 1

# for i in range(max_Num):
#     max_Num = max_Num - 1
#     print(max_Num)

#     if max_Num == 1:
#         print("LAUNCHING TIME! SHIUUUHHH\n")

# while max_Num != 1:
#     max_Num = max_Num - 1
#     print(max_Num)

#     if max_Num == 1:
#         print("LAUNCHING TIME! SHIUHHHH\n")

# STUNNING PYTHON WAY (HUA SO GREATT!): range(start, stop, step)
# for i in range((max_Num-1), 0, -1):
#     print(i)

# if i = 1, then executing:
# print("LAUNCHING TIME! SHIUHHHH")

#Task 5: Even-Odd Number
number = 11

# for i in range (number):
#     number = number - 1
#     if number % 2 == 0:
#         print(f"{number} is an EVEN number.")
#     else:
#         print(f"{number} is an ODD number.")

# while number != 1:
#     number = number - 1
#     if number % 2 == 0:
#         print(f"{number} is an EVEN number.")
#     else:
#         print(f"{number} is an ODD number.")

for i in range((number-1), 0, -1):
    if i % 2 == 0:
        print(f"{i} is an EVEN number.")
    else: 
        print(f"{i} is an ODD number.")