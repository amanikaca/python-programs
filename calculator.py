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

#output
#C:\Users\Dell\Desktop\-\python programs>py calculator.py
#Simple Calculator
#Enter first number: 34
#Enter second number: 12
#Choose operation: +, -, *, /
#Enter operator: +
#Result:46.0

#C:\Users\Dell\Desktop\-\python programs>py calculator.py
#Simple Calculator
#Enter first number: 3
#Enter second number: 5
#Choose operation: +, -, *, /
#Enter operator: -
#Result: -2.0

#C:\Users\Dell\Desktop\-\python programs>py calculator.py
#Simple Calculator
#Enter first number: 4
#Enter second number: 7
#Choose operation: +, -, *, /
#Enter operator: *
#Result: 28.0

#C:\Users\Dell\Desktop\-\python programs>py calculator.py
#Simple Calculator
#Enter first number: 56
#Enter second number: 4
#Choose operation: +, -, *, /
#Enter operator: /
#Result: 14.0



