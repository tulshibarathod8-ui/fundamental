print(" Welcome to the interactive personal Data Collecter !\n")

name=input("Enter your name:")
age = int(input("Enter your age:"))
height=float(input("Enter your height in meters :"))
number=int(input("Enter your favorit number :"))

print("Thank you! Here is the information we collected:\n")


print("Name:",name,"(Type:",type(name),",memory address:",id(name),")")
print("Age:",age,"(Type :",type(age),",memory address:",id(age),")")
print("Height:",height,"(Type :",type(height ),",memory address:",id(height),")")
print("Number:",number,"(Type :",type(number),",memory address:",id(number),")")

current_year = 2026
birth_year = current_year-age
print("\n your birth year is approximately :",birth_year,"(based on year age of",age,")\n")
print("Thank you for using the personal Data collecter.Goodby!")