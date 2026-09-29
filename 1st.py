name = "Sweshen"
age = 69
location = "Kabre"
print(f"My name is {name} and age is {age} and location is {location}")
print("My name is " +str(name) + " and age is " + str(age)+ " and location is " + str(location))
print("my name is %s and age is %d and location is %s "%(name, age, location))
print("My name is {0} and age is {1} and location is {2}".format(name, age, location))

name1 = input("Enter the name")
age1 = int(input("Enter the age"))
print(f"My name is {name1} and age is {age1}")

print(type(name1))
print(type(age1))
