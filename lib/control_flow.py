#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature < 40 :
        return  "It's brisk out there!"
    elif temperature>=40 and temperature<=65:
        return "It's a little chilly out there!"
    elif temperature > 85 :
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"    
    pass

def fizzbuzz(num):
    # your code here
    if num% 3 == 0 and num%5 == 0 :
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/": 
        return num1/num2
    else:
        print( "Invalid operation!")
        return None
    pass


# def check_time(foo): 
#     def logger (time): 
#         if time<2100 :
#             foo(time)    
#         else:
#             print("Well here is your empty stripped value") 
#     return logger
#     pass
        
# @check_time
# def func_one (time):
#     print("I am feeling it")

#  @check_time
# def function_two (time):
#     print("Me too") 

#  func_one()
#  func_two()     



# #try/except and  finally which is to be computed irregardless
# def divide(num1, num2):
#     try: 
#         quotient = num1/num2 
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be a 0") 
#     except TypeError:
#         print("Error: nums must be of type int or float ")
#     finally: 
#         print("Isn\'t coding fun")


# dog = "stupid"
# dict_map = {
#     "stupid": "Bosco",
#     "Clever": "Scooby",
#     "Ruthless": "Rex",
#     "Old": "Mzee",
# }

# name = dict_map.get(dog, "bitch") #get allows us to set a default value "bitch" in this case

   
