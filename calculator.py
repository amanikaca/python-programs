# calculator.py

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Undefined"

print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operator: ")

if op == '+':
    print(f"Result: {add(a, b)}")
elif op == '-':
    print(f"Result: {sub(a, b)}")
elif op == '*':
    print(f"Result: {mul(a, b)}")
elif op == '/':
    print(f"Result: {div(a, b)}")
else:
    print("Invalid operator.")
