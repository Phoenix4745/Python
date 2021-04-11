def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print('Calculator')
print('1. Addition \n2. Subtraction \n3. Multiplication \n4. Division')
print("Choose any one of these operations :-")
while True:
    choice = input('Enter choice 1/2/3/4')
    if choice in ("1", "2", "3", "4"):
        num1 = (float(input("First Number :- ")))
        num2 = (float(input("Second Number :- ")))

        if choice == '1':
            print(num1, '+', num2 , '=' , add(num1, num2))

        elif choice == '2':
            print(num1 , '-' , num2 , '=' , subtract(num1, num2))

        elif choice == '3':
            print(num1 , '*' , num2 , '=' , multiply(num1, num2))

        elif choice == '4':
            print(num1 , '/' , num2 , '=' , divide(num1, num2))
    else:
        print("Enter a valid response.")
