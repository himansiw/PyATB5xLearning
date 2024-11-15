#Problem Find the max between 3 numbers

#Logic Building

# user inputs -> num1 ,num2, num3
#o/p -> int or String with max number

#Syntax

#if condition 1:
#print("do 1")
#elif condition 2:
#print("do 2")
#elif condition 3:
#print("do 3")
#else:
#print("do for else")

num1 = int(input("Enter number num1 \n"))
num2 = int(input("Enter number num2 \n"))
num3 = int(input("Enter number num3 \n"))

if num1 > num2 and num1>num3:
    print("Max is a",num1)
elif num2 > num1 and num2>num3:
    print("Max is a",num2)
else:
    print("Max is a", num3)