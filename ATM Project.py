print('Welcome to Dginx Bank')
cname = input('Enter your Name ')
print('Hello Mr', cname)

# variable Declaration
restart=('y')
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
# Balance enquiry
            if option == 1:
                print('Mr', cname, 'your Balance is $', balance)
                restart = input("Would you like to go back?")
                if restart in ('n', 'N', 'No', 'NO', 'no'):
                    print('Thank you Mr. ', cname, 'Have a great Day')
                    break
# PIN Change
            elif option == 2:
                    newpin = int(input('Please enter your new PIN '))
                    confpin = int(input('Please conform your new PIN '))
                    if newpin == confpin:
                        pin = newpin

                    else:
                        print('Pin did not matched Try later')
                        break
# Pay In
            elif option == 3:
                balanceadd = float(input('Enter the value you want to add: '))
                balance = balance + balanceadd
                print('your new balance is $', float(balance))
                restart = input("Would you like to go back ?")
                if restart in ('n', 'N', 'No', 'NO', 'no'):
                    print('Thank you Mr. ', cname, 'Have a great Day')
                    break
# Bill Pay
            elif option == 4:
                vendor = input("Enter vendor's name ")
                billpay = float(input('Enter the Bill Amount '))
                billconform = input('press Y to conform and N to reject the payment ')
                if billconform in ('Y', 'y',):
                    balance = balance-billpay
                    print('Transaction of $', float(billpay), 'is successful\n')
                    print('Your available balance is $ ', balance)
                    restart = input("Would you like to go back ? ")
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        print('Thank you Mr. ', cname, 'Have a great Day')
                        break
# withdraw
            elif option == 5:
                option5 = ('y')
                withdraw = int(input("Enter the amount you want to withdraw: \n", '$10', '$20', '$50', '$100'))
                if withdraw in (10, 20, 50, 100):
                    balance = balance - withdraw
                    print('\n Your new Balance is $', balance)
                    restart = input("Would you like to go back ? ")
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        print('Thank you Mr. ', cname, 'Have a great Day')
                        break
                elif withdraw not in (10, 20, 50, 100):
                    print('Invalid Entry Try again')
                    restart = ('y')
                elif withdraw ==1:
                    withdraw = int(input("Enter the amount you want to withdraw: \n", '$10', '$20', '$50', '$100'))























