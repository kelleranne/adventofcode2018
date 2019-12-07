#day1
#to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2
import math

def sumAllFuel ():
    allFuel = ""
    sum = 0
    with open("/Users/annekeller/Documents/Chalmers/Miscellenous/Programmering/adventofcode2019/day1/day1.txt", "r") as file:
        allFuel = file.readlines()
        allFuel = list(map(int, allFuel))
        for i in range(len(allFuel)):
            allFuel[i] = (math.floor(allFuel[i] / 3) - 2)
            sum = sum + allFuel[i] 
        print(math.floor(sum))

sumAllFuel() 