#✅ Triangle Classifier:

#Write a program that classifies a triangle based on its side lengths. Given three input values
# representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal). Use an if-else statement to classify the triangle.


#s1, s2, s3 → int

#o/p →. iso, eq, scalene

side1 = int(input("Enter lengths of the side1 \n"))
side2 = int(input("Enter lengths of the side2 \n"))
side3 = int(input("Enter lengths of the side3 \n"))

if side1==side2 and side2==side3:
    print("Equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


