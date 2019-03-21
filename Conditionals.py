"""
Made By: Brandon Calabrese

Welcome to my Conditionals Program! It first asks for two numbers and tells the user if the larger of the two numbers
is divisible by the smaller number. Then the program asks for three more numbers and tells the user if they can represent the lengths of the
sides of a triangle. 

"""

#Returns the bigger of 2 numbers
def getBiggerNum(num1,num2):
    if num1 > num2:
        return num1
    if num1 < num2:
        return num2
#Returns the smaller of 2 numbers
def getSmallerNum(num1,num2):
    if num1 < num2:
        return num1
    if num1 > num2:
        return num2
#Outputs whether 2 numbers are divisible
def divisible(num1,num2):
    if num1 < 0 or num2 < 0:
        print("You must input positive integers!")
    elif num1 == num2:
        print("You must input non-equal numbers!")
    else:
        smallNum = getSmallerNum(num1,num2)
        bigNum = getBiggerNum(num1,num2)

        if bigNum % smallNum == 0:
            print(str(bigNum) + " is evenly divisible by " + str(smallNum))
        else:
            print(str(bigNum) + " is not evenly divisible by " + str(smallNum))
#Tests the 'devisible' function
def test_divisible():
    divisible(5,5)
    divisible(50,5)
    divisible(8,5)
    divisible(12,20)
    divisible(100,10)
    divisible(-5,500)
#Tests if 3 numbers form a triangle
def triangle(num1,num2,num3):
    if num1 <= 0 or num2 <= 0 or num3 <= 0:
        print("Input must be positive!")
    else:
        if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
            print(str(num1) + ", " + str(num2) + ", " + str(num3) + " form a triangle!")
        else:
            print(str(num1) + ", " + str(num2) + ", " + str(num3) + " do not form a triangle!")
#Tests the 'triangle' function
def test_triangle():
    triangle(3,4,5)
    triangle(8,12,17)
    triangle(10,9,30)
    triangle(23,20,23)
    triangle(8,8,8)
    triangle(14,65,3)

#The starting point of the program's execution
def main():
    test_divisible()
    test_triangle()

main()
