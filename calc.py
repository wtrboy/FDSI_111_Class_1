
def print_separator():
    print('---------------')
    
def print_menu():
    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

# instructions

opc = ''
while(opc !='x'):
    # find out how to print empty lines (google it)
    # print('n\n\n\n')
    print_menu()

    opc = input('Please choose an option: ')
   
    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))
   
    if(opc == '1'):
        res = num1 + num2
        print('Res: ' + str(res))

    elif(opc == '2'):
        res = num1 - num2
        print('Res: ' + str(res))
    
    elif(opc == '3'):
        res = num1 * num2
        print('Res: ' + str(res))

    elif(opc == '4'):
        res = num1 / num2
        print('Res: ' + str(res))

    input('Press Enter to continue...')
    
