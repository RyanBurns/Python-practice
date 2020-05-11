#!/bin/python
def new():
	print("\n")
new()
print("Strings and things")
print("Hello world!")
print('Hello with single quotations')
print("""Multline with 
triple quotations""")
print('\n')
print("Maths")
print(1 + 1) #ADDITION
print(1 -1) #SUBTRACTION
print(3 * 3) #MULTIPLICATION
print(12 / 3) #DIVISION
print(3**3) #Exponent
print(13 // 4) #Divide no remainder
print(13 % 4) # Modulus
print("\n")
quote = "War, war never changes"
print(len(quote)) # LENGTH OF QUOTE
print(quote.upper()) # Uppercase something
print(quote.lower()) # Lower case something
print(quote.title()) # Title
print('\n')
print("-------VARIABLES----------")
name = "Ryan"
age = 25
gpa = 3.4
print("My name is " + name + " and I am " + str(age) + " years old. My gpa is " + str(gpa) + '\n')
print("FUNCTIONS AND STUFF")
def who_am_i():
	#name = "Ryan"
	#age = 25
	#gpa = 3.4
	print("My name is " + name + " and I am " + str(age) + " years old. My gpa is " + str(gpa) + '\n')
who_am_i()
print("\n")
print("Mini functions for math")
# Add one hundred
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(1)

#Add in mltiple parameters
def add(a,b):
	print(a + b)
add(1,2)
new()
#multiply using return
def multiply(x,y):
	return x * y
print(multiply(7,7))
new()
#square root
def sqrt(x):
	return x ** 0.5
print(sqrt(9))
new()
#Booleans
bool1 = True
bool2 = False
bool3 = 3*3 == 9
bool4 = 3*3 != 9
bool5 = "True"
print(bool1, bool2, bool3, bool4)
print(type(bool1))
print(type(bool5))
new()
new()
#Relational expressions booleans
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 5
less_than_equal_to = 5 <= 7
print(greater_than_equal_to, less_than_equal_to, greater_than, less_than)
new()
new()
#---AND-OR----
test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) or (5 > 7)
test_not = not True
print(test_and, test_or, test_not)
new()
new()
# conditional statements
def buySoda(money):
	if money >= 1:
		return "Soda puchased"
	else:
		return "Not enough to buy"
print(buySoda(34))
print(buySoda(0.9))
new()
# conditional buy alcohol
def buyBooze(age,money):
	if (age >= 18) and (money >= 2.50):
		return "Have a qingdao"
	elif (age < 18) and (money >= 2.50):
		return "You have enough money but are too young"
	elif (age >= 18) and (money < 2.50):
		return "Get a job maaan"
	else:
		return "Young and broke"
print(buyBooze(19,3))
print(buyBooze(17,4))
print(buyBooze(20,1))
print(buyBooze(2,1))
print(buyBooze(2,10))
print(buyBooze(2,12))
print(buyBooze(2,1))
print(buyBooze(22,1))
new()
# Lists
new()
print("Lists have square brackets []")
movies = ["The pianist", "The shawshank redemption", "Daggers out", "Parasite", "The hills have eyes"]
print(movies[0]) # print the first item in list
print(movies[1:3]) # print the second and third item in the list
print(movies[0:]) # SLICING- print from start to end
print(movies[1:]) # print from shawshank to end
print(movies[:3])
print(movies[-1])
movies.append("Jaws")
print(movies)
movies.append("Hui")
movies.pop()
print(movies)
movies.pop(0)
print(movies)
new()
person = ["a","b","c","d"]
combined = zip(movies,person)
print(list(combined))
new()
#tuple are like lists but can't be modified
grades = ("A", "B", "C", "D", "F")
print(grades[3]) # will print 'D'
new()
# for loops and while loops
vegetables = ["Potato","Cabbage","Lotus root","Pepper"]
for veg in vegetables:
	print(veg)
new()
i = 0
while i <= 10:
	print(i)
	i += 1
new()
