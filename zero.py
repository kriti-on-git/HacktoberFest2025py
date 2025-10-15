# calculator.py

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(divide(a, b))

