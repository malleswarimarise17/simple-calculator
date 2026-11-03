def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("--- Simple Calculator ---")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# For now, you can test specific numbers here:
num1 = 10
num2 = 5

print(f"\nUsing numbers: {num1} and {num2}")
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
