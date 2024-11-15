#Problem to find the max between two

#Logic Building Formula

# 1 . user inputs -> two integers
#2. o/p -> int 1 which ever is greater max number it will return
#31.4 or 45.34 -> float


num1 = float(input("Enter number num1 \n"))
num2 = float(input("Enter number num2 \n"))

if num1 >= num2:
    print("Max is a",num1)
else:
    print("Max is a",num2)

    #Edge case  -num1 == num2 -> Handled
    #String ->ABC, ten -> try and except
    #Negative value

