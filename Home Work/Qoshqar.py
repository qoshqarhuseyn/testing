

# Task 1:

# height = int(input('Enter your height: '))
# weight = int(input('Enter your weight: '))

# bwi = weight/ (height/100)**2

# if bwi < 18.5:
#     print('Weak')
# elif bwi >= 18.5 and bwi <= 25:
#     print('Normal') 
# elif bwi >= 25 and bwi <= 30:
#     print('Fat')
# else:
#     print('Obese')


# Task 2:

# import re

# p = input("Input your password")

# x = True

# while x:  
   
#     if (len(p) < 6 or len(p) > 16):
#         break
    
#     elif not re.search("[a-z]", p):
#         break
   
#     elif not re.search("[0-9]", p):
#         break
    
#     elif not re.search("[A-Z]", p):
#         break
   
#     elif not re.search("[$#@]", p):
#         break
    
#     elif re.search("\s", p):
#         break
#     else:
       
#         print("Valid Password")
#         x = False
#         break


# if x:
#     print("Not a Valid Password")















# Task 1


# number = int(input("Number: "))
# sum = 0
# for i in range(1, number + 1):
#     sum += i
#     print(sum)








# Task -2




man= [1,2,3,4,5]
woman= ["a","b","c"]

gender = int(input)('(kisi, (2) Qadin;)')

















# Task - 3



# dict1  = {
#     "casual": {
#         "shirt": "t-shirt",
#         "pants": "jeans",
#         "shoes": "sneakers"
#     },
#     "formal": {
#         "shirt": "button-up",
#         "pants": "dress pants",
#         "shoes": "dress shoes"
#     },
#     "sportswear": {
#         "shirt": "athletic top",
#         "pants": "athletic shorts",
#         "shoes": "running shoes"
#     }
# }


# user_input = input("Enter the type of clothing (casual/formal/sportswear): ")


# if user_input in dict1:
   
#     print("Shirt:", dict1[user_input]["shirt"])
#     print("Pants:", dict1[user_input]["pants"])
#     print("Shoes:", dict1[user_input]["shoes"])
# else:
#     print("Invalid input. Please enter either 'casual', 'formal', or 'sportswear'.")








# Task - 4























































# Task - 5



# def bowling():
#     age = int(input("Please enter your age: "))
#     if age >= 8:
#         print("Welcome to the bowling area!")
#     else:
#         print("Sorry, those under 8 years old are not allowed in the bowling area.")

# def trampoline():
#     age = int(input("Please enter your age: "))
#     weight = int(input("Please enter your weight in kilograms: "))
#     if age >= 8 and weight < 110:
#         print("Welcome to the trampoline area!")
#     else:
#         print("Sorry, those under 8 years old or over 110 kilograms are not allowed in the trampoline area.")

# def Entertainment():
#     print("Welcome to the entertainment center!")
#     sub_category = int(input("Please choose one of the sub-categories: \n1. Dragon \n2. Bouncer \n3. Speed Carousel\n"))
#     if sub_category == 1:
#         age = int(input("Please enter your age: "))
#         weight = int(input("Please enter your weight in kilograms: "))
#         if age >= 12 and weight < 110:
#             print("Welcome to the Dragon area!")
#         else:
#             print("Sorry, those under 12 years old or over 110 kilograms are not allowed in the Dragon area.")
#     elif sub_category == 2:
#         age = int(input("Please enter your age: "))
#         weight = int(input("Please enter your weight in kilograms: "))
#         if age >= 6 and weight < 110:
#             print("Welcome to the Bouncer area!")
#         else:
#             print("Sorry, those under 6 years old or over 110 kilograms are not allowed in the Bouncer area.")
#     elif sub_category == 3:
#         age = int(input("Please enter your age: "))
#         height = int(input("Please enter your height in centimeters: "))
#         weight = int(input("Please enter your weight in kilograms: "))
#         if age >= 8 and height < 190 and weight < 110:
#             print("Welcome to the Speed Carousel area!")
#         else:
#             print("Sorry, those under 8 years old, over 190 centimeters tall, or over 110 kilograms are not allowed in the Speed Carousel area.")

# def main():
#     print("Welcome to the entertainment center!")
#     choice = int(input("Please select the area you want: \n1. Bowling \n2. Trampoline \n3. Entertainment\n"))
#     if choice == 1:
#         bowling()
#     elif choice == 2:
#         trampoline()
#     elif choice == 3:
#         Entertainment()
#     else:
#         print("Invalid choice. Please try again.")

# if  "_main_":
#     main()

























































