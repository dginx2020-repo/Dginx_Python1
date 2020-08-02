print('Welcome to Dginx Bank')
cname = input('Enter your Name ')
print('Hello Mr', cname)

# variable Declaration
restart=('Y')
chances = 3
balance = 100000.86

# PIN Validation
while chances >=0:
    pin = int(input('Enter your PIN '))
    if pin == (1989) :
        print('Welcome to ATM Banking\n')
        while restart not in ('n', 'N', 'No', 'NO', 'no'):
            print('Press 1 for Balance Enq\n')
            print('Press 2 for PIN change\n')
            print('Press 3 for pay In\n')
            print('Press 4 for Billpay\n')
            print('Press 5 for Cash withdraw\n')
            option = int(input('Please Select your option '))
            if option == 1:
                print('Mr', cname, 'your Balance is $', balance)
                restart = input("Would you like to go back?")
                if restart in ('n', 'N', 'No', 'NO', 'no'):
                    print('Thank you Mr. ', cname, 'Have a great Day')
                    break
                elif option == 2:









