#Task 1
#Write a program to take a user age and let him know if he can go the club.  21

user_age = int(input("Enter your age \n"))
if user_age > 21:
    print("You can go to the club")
else:
    print("You cannot go to the club")


#Task 2
#print(type(a))
#if a == 10:
#print("Hello World")
#else:
#print("Not Hello")

e_num = int(input("Enter number \n"))
print(type(e_num))
if e_num == 10:
    print("Hello World")
else:
    print("Not Hello")



#Task 3
#Problem to find the max between two ( 3,4) → 4

max_num =max(3,4)
print(max_num)