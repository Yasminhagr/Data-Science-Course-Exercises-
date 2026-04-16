# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
Street="Street 123"
City="City 456"
Country="Country 789"
Adress=Street+"\n"+City+"\n"+Country
Adress2=f"{Street}\n{City}\n{Country}"
print(f"Address: {Adress}")  
print(f"Address 2: {Adress2}")

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index
String="Earth revolves around the sun"
print(f"Print revolves using slice operator:{String[6:14]}")
print(f"sun using negative index:{String[-3:]}")

#3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
FruitNum=5
VeggieNum=3
print(f"I eat {VeggieNum} veggies and {FruitNum} fruits daily")

# 4.I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
s='maine 200 banana khaye'
s=s.replace("200 banana","10 samosa")
print(f"new s is {s}")