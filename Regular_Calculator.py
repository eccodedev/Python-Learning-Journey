# Calculator Project: 

def add(a, b):
    result = a + b
    return result 

def subtract(a , b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if a == 0 or b == 0: # I have to check first if is a valid operation.
        print('We cannot divide by zero')
        return
    
    result = a / b
    return result

def exp(a, b):
    result = a ** b
    return result

def another_calculation():
    another_calculation = int(input('Do you want to make another calculation: \n 1) Yes \n 2) No \n'))
    if another_calculation == 2:
        return False
    else:
        return True


import sys

print('    ==========================    ')
print('Welcome to my calculator project!!')
print('          📠  📟   🧮            ')
print('    ==========================    ')

def main():
    tries = 1
    flag = True
    while flag:
        flag1 = True
        while flag1:
            operation_pick = int(input('What operation do you want to make: \n   1) Addition \n   2) Subtraction \n   3) Multiplication \n   4) Division \n   5) Exponentiation \n   6) Quit \n'))
            if operation_pick == 6:
                print('    ==========================    ')
                print('            Goodbye!!')
                print('          📠  📟   🧮            ')
                print('    ==========================    ')
                sys.exit(0)
            
            elif operation_pick in (1,2,3,4,5,6):
                flag1 = False
            
            elif tries == 3:
                print('    ==========================    ')
                print('    Too many invalid options.     ')
                print('        Reset the program!'        )
                print('    ==========================    ')
                sys.exit(0)
            
            else:
                print('----->Choose a valid option:<----- ')
                tries += 1

        number_1 = int(input('Enter a number: '))
        number_2 = int(input('Enter another number: '))

        if operation_pick == 1:
            print()
            print(f'Operation = {number_1} + {number_2} = {add(number_1, number_2)}')
            print()

        elif operation_pick == 2:
            print()
            print(f'Operation = {number_1} - {number_2} = {subtract(number_1, number_2)}')
            print()

        elif operation_pick == 3:
            print()
            print(f'Operation = {number_1} * {number_2} = {multiply(number_1, number_2)}')
            print()

        elif operation_pick == 4:
            print()
            print(f'Operation = {number_1} / {number_2} = {divide(number_1, number_2)}')
            print()

        elif operation_pick == 5:
            print()
            print(f'Operation =  {number_1} ** {number_2} = {exp(number_1, number_2)}')
            print()

        flag = another_calculation()        

if __name__ == "__main__":
  main()

print('    ==========================    ')
print('            Goodbye!!')
print('          📠  📟   🧮            ')
print('    ==========================    ')

# This project was intended for practicing the functions concept. 




