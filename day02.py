#-------------------------------------------------------------------
#Day 02 excise 

#name = "Abdijalil"          #string
#age = 25                    #interger
#height = 5.7                #float     
#is_student = True           #boolean


#print them out
#print("Name", name)
#print("Age", age)
#print("Height", height)
#print("Is a student?", is_student)

#some math
#birth_year = 2025 - age
#print("You were born around:", birth_year)

#combine text with numbers (must turn numbers to strings)
#number = input("Enter a number: ")
#double = int(number) * 2
#print ("Double of your number is:", double)

#------------------------------------------------------------------

number_first = float(input("Enter first number: "))
number_second = float(input("Enter second number: "))
operation = input("Do you want to add, subtract, multiple, or divide?")

if operation == "add":
    print(f"The result is: {number_first + number_second}")


if operation == "subtract":
    print(f"The result is: {number_first - number_second}")


if operation == "multiple":
    print(f"The result is: {number_first * number_second}")


if operation == "divide":
    print(f"The result is: {number_first / number_second}")
