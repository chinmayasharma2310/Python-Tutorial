# using input()

val = input("Enter the name:")
print(val)
print(type(val))

#input() always returns string value. 

age = input("Enter your age:")
print(age)
print(type(age))  # still the return type is String. 

# type cast the input

age_int = int(input("Enter your age:"))
print(age_int)
print(type(age_int))

# taking Multiple inputs using split()

x, y = input("Enter the names:").split(",")
print("First name :", x)
print("First name :", y)

a, b = input("Enter the ages: ").split()
print("First age {} and Second age {}".format(a,b))

# type casting using list()

x = list(map(int, input("Enter numbers:").split()))
print(x)

# using List comprehension 

x, y = [int(i) for i in input("Enter roll no:").split()]
print("First Roll no:", x)
print("First Roll no:", y)

x = [int(i) for i in input("Enter all roll no: ").split()]
print(x)