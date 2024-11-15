#Write a program to take a user age and
#let him know if he can go the club
#21


#Logic Building Formula

#Step 1
#user input i/p -> DATA TYPE ->INT
#O/P -> Sting -> user if he can go or not


#Step 2 .Rough logic(brute force)
#age>21 -> print can go
#age<21 -> print can't go

#Step 3. write the logic

age =int(input("Enter your age\n"))

if age >=21:
    print("Can go to club")
else:
    print("Can't go to club")


#Step 4. Check for the edge case
#Negative age or extremely high values -> program will break
#non-numeric input -ABC
#Age which is valid >130

#Step 5 Optimize the code
#Handle all the edge cases.
