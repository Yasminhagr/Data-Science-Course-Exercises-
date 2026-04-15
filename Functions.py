# # Exercise: Functions in python
# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

#SOLUTION##########################################

# def calculate_area(dim1=1,dim2=1):
#     area=(1/2)*dim1*dim2
#     return area
# calculate_area

def calculate_area(dim1=1,dim2=1,shape='Triangle'):
    if shape.upper()=="TRIANGLE":
        area=(1/2)*dim1*dim2
    elif shape.upper()=="RECTANGLE":
        area=dim1*dim2
    else:
        print("Err")
        area=None

    return area
print(calculate_area(11,3,"triangle"))

