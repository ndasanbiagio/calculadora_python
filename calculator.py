#Create Calculator with Python

# 1 Part - Creating Function (Arimeticas)

def add(n1=0, n2=0):
    return n1 + n2

def subtract(n1=0, n2=0):
    return n2 - n2

def multiply(n1=0, n2=0):
    return n1 * n2

def split(n1=0, n2=0):
    return n1 / n2

def potency(n1=0, n2=0):
    return pow(n1, n2)

def square_root(n1=0):
    return n1 ** 0.5


# 2 Part MENU

def menu():  #Options
    print('Welcome to Calculator')
    print('1 - Add ')
    print('2 - Subtract')
    print('3 - Multiply')
    print('4 - Split')
    print('5 - Potency')
    print('6 - Square Root')
    print('7 - Exit')
    

# 3 Part - Inputs number
def input_numbers():
    n1 = int(input('Enter First Number: '))
    n2 = int(input('Enter Second Number: '))
    return n1, n2

def input_number():
    n1 = int(input('Enter Number: '))
    return n1
             

# 4 Part - Creating Main
def main():
    menu()
    option = 'y' #to extir of program
    while option == 'y': #as long as the option yes, keep running
        choice = input('Enter an option: ') 
        if choice == '1':
            n1, n2 =  input_numbers()       
            print('Add: ', add(n1, n2))
        elif choice == '2':
            n1, n2 =  input_numbers()       
            print('Subtract: ', subtract(n1, n2))
        elif choice == '3':
            n1, n2 =  input_numbers()       
            print('Multiply: ', multiply(n1, n2))
        elif choice == '4':
            n1, n2 =  input_numbers()       
            print('Split: ', split(n1, n2))
        elif choice == '5':
            n1, n2 =  input_numbers()       
            print('Potency: ', potency(n1, n2))
        elif choice == '6':
            n1=  input_number()       
            print('Square Root: ', square_root(n1))
        elif choice == '7':
            print('Thank you...')
            break
        else:
            print('Option Invalid!!!')
            continue
        
        option = input('Do you want continue....? (y/n)')
        if option == 'y':
            menu()
        else:
            print('Thank you.... BYE BYE')
            breakpoint
        
main()