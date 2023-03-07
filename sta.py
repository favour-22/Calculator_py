from mod import *
from math import sqrt
def Calculate():
        try:
                 if True:
                   ask_input = (input('''Please type in the math operation you will like to perform:
     + for addition
     - for subtraction
     / for division 
     * for multiplication
     sqrt for square root 
     >>> '''))
        except KeyboardInterrupt:
                print("\nCalculator interupted by user")

       
                 
        try:
                         #ADDTION 
                 if ask_input == '+':
                             num_1 = int(input('''Enter the first number >>> '''))                          
                             num_2 = int(input('''Enter the second number  >>>  ''')) 
                             print('{} + {} = {}'.format(num_1, num_2,add(num_1, num_2)))                 
#SUBTRACTION         
                 elif ask_input == '-':
                        num_1 = int(input('''Enter the first number >>> '''))                          
                        num_2 = int(input('''Enter the second number  >>>  '''))
                        print('{} - {} = {}'.format(num_1, num_2,sub(num_1, num_2)))
#DIVISION             
                 elif ask_input ==  '/': 
                        num_1 = int(input('''Enter the first number >>> '''))                          
                        num_2 = int(input('''Enter the second number  >>>  '''))
                        print('{} / {} = {}'.format(num_1, num_2, div(num_1,num_2,)))
    
#Multiplication 
                 elif ask_input == '*':
                            num_1 = int(input('''Enter the first number >>> '''))                          
                            num_2 = int(input('''Enter the second number  >>>  '''))
                            print('{} * {} = {}'.format(num_1, num_2, mul(num_1,num_2,)))

                 elif ask_input == 'sqrt':
                            num_sqrt = int(input("Enter square root"))
                            print('sqrt of {} = {}'.format(num_sqrt,sqrt(num_sqrt)))                   
                 else:
                           print("try to enter correct operation")
                        
        except ValueError:
                print("Invalid input")
        except KeyboardInterrupt:
                print("\nCalculator interupted by user")
        
                
Calculate()
next_cal = input("Do you want to perform any other operation, type yes or no: ")
if next_cal == 'no':
        exit()
       
else:
        Calculate()
        
                         