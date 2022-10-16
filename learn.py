print('   /|')
print('  / |')
print(' /  |')
print('/___|')
character_name="john"
character_age= 50

print("there was one a man named " +character_name)
print("he was " +str(character_age)+ " years old ")
character_name="mike"
character_age= 34
print("he liked his name "+character_name+" but didnt his age "+str(character_age))
print("giraffe\n academy")
my_num = -5

print(abs(my_num))
print(pow(3,2))
print(max(4,8))
print(min(4,3))
print(round(3.49))
print(round(3.6))
print("some more maths function")
from math import*

print(floor(3.8))
print(ceil(3.1))
print(sqrt(100))

print("input from the user")
#name=input("enter your name:")
#print("hello "+ name+"!")
'''
print("Buildin a basic calculator")
num1=input("Enter a number")
num2=input("Enter another number")
result=int(num1)+float(num2)
print (result)
'''
print("making lists")
friends=["kevin","mike","karan","timmy","jimmy"]

print(friends)
print(friends[0])
print(friends[1:])
print(friends[1:3])

print("lists functions")
lucky_numbers=[1,2,3,4,5,6]
people=["jon","min","tin","com","lesss","maxi"]

print("fuctions")
def say_hi(name,age):
    print("Hello "+name+" you are "+ str(age))
say_hi("mike",21)

def cube(num):
    return(num*num*num)
print(cube(4))

print("if statements")
is_male=True
is_tall=True

if is_male or is_tall:
    print("you are a male or you are tall or both")
else:
    print("you are neithe male nor tall")

is_male=True
is_tall=False
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male)and is_tall:
    print("you are not a male but are tall")
else:
    print("you are either not male or not tall or both")

print("if statements and comparisons")
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(1,2,3,))

print("key value pairs")
month_conversions={
    "jan" : "january",
    "feb" : "febuary",
     "mar" : "march",
}

print(month_conversions.get("jan","not valid"))

print("WHILE LOOP")

i = 1
while i<=10:
     print(i)
     i=i+1

print("done with loop")

print("For loops")

for letter in "giraffe academy":
    print (letter)

for friend in friends:
    print (friend +"from the list")

for count in range(3,10):
    print (count)

for index in range(len(friends)):
    print (friends[index])

for num in "123":
    print (num)


print("exponent function")
def raise_to_the_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result

print(raise_to_the_power(4,7))

print("2d lists and nested looops")
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[3][0])
for row in number_grid:
    print(row)
    for col in row:
        print(col)

print("comments")
'''
this will not be executed
'''
# this will also not be executed

print("try/execpt errors input validation")
try:
    number=int(input("enter a number: "))
    print (number)
except ValueError:
       print("invalid input")

# python2.0 Data structures and algorithms


