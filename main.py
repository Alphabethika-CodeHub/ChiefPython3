import math

myInt = 4
myFloat = 5.0
myPI = 3.14
myString = "Hello World!"

# Calculate Area of Rectangular.
REC_LENGTH = 5
REC_WIDE = 12
areaOfRectangular = REC_LENGTH * REC_WIDE
perimeterOfRectangular = 2 * (REC_LENGTH + REC_WIDE)
diagonalRectangular = math.sqrt((REC_LENGTH ** 2) + (REC_WIDE ** 2))
print("Area of Rectangular: " + str(areaOfRectangular))
print("Perimeter of Rectangular: " + str(perimeterOfRectangular))
print("Diagonal of Rectangular: " + str(diagonalRectangular))

# Concatenated String With Number
myString1 = "Hello "
myString2 = "World "
myInteger3 = 3.0
print(myString1 + myString2 + str(myInteger3))

MULTI_LINE_STRING = """ 
 This is
 Multiline
 String by Python!
 """


def score_checker(score):
    if type(score) == int:
        if score >= 90:
            print("Grade A")
        elif score >= 70:
            print("Grade B")
        elif score >= 40:
            print("Grade C")
        else:
            print("Learn is The Best Way!")
    else:
        print("Please Input Number!")


score_checker(40)


# Lists
my_arr = ["Pizza", "Spaghetti", "Bakwan"]
my_second_arr = ["Sushi", "Nasi Goreng"]
my_combined_array = my_arr + my_second_arr
print(my_combined_array, "Get One From arr: " + my_combined_array[2])
