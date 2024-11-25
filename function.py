# custom function with default argument
def greet(name="MohammadAli"):
    print("Hello " + name)

greet()
greet("anne")


def hello_world():
    print("Hello world!")

hello_world()


def operations(x, y):
    return (x + y, x - y, x * y, x / y)

a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))

add, subtraction, multiply, divide = operations(a, b)
print(
    " ----- Result ----- \n"
    + "Add: "
    + str(add)
    + "\n"
    + "Subtraction: "
    + str(subtraction)
    + "\n"
    + "Multiply: "
    + str(multiply)
    + "\n"
    + "Divide: "
    + str(divide)
    + "\n"
)
