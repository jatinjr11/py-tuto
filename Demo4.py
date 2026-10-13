name = input("Enter your name: ")
age = int(input("Enter your age: "))

# input method always returns a string, so we use typecasting to convert it to an integer

print("Hello,", name)
print("You are", age, "years old")
print(type(age))