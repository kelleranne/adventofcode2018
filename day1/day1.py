#day1
#to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2
import math
mass = 12
fuel = mass / 3
math.floor(fuel)
fuel = fuel - 2
print(fuel)

def sumAllFuel ():
    allFuel = ""
    with open("day1.txt", "r") as file:
        allFuel = file.read().replace('\n', '')
        print(allFuel)

sumAllFuel()