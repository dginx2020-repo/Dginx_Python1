print('Welcome to Dginx Bank')
cname = input('Enter your Name ')
print('Hello ', cname)

# variable Declaration
restart=('Y')
chances = 3
balance = 100000.86
wdchance = 2

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
                    chances = -1
                    print('Thank you Mr. ', cname, 'Have a great Day')
                    break
# PIN Change
            elif option == 2:
                    newpin = int(input('Please enter your new PIN '))
                    confpin = int(input('Please conform your new PIN '))
                    if newpin == confpin:
                        pin = newpin
                        print('PIN has been changed successfully\n')
                        restart = input("Would you like to go back?")
                        if restart in ('n', 'N', 'No', 'NO', 'no'):
                            chances = -1
                            print('Thank you Mr. ', cname, 'Have a great Day')
                            break

                    else:
                        print('Pin did not matched Try later')
                        chances = -1
                        print('Thank you Mr. ', cname, 'Have a great Day')
                        break
# Pay In
            elif option == 3:
                balanceadd = float(input('Enter the value you want to add: '))
                balance = balance + balanceadd
                print('your new balance is $', float(balance))
                restart = input("Would you like to go back ?")
                if restart in ('n', 'N', 'No', 'NO', 'no'):
                    chances = -1
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
                elif billconform in ('N', 'n'):
                    print('Transaction has been cancelled\n')
                    restart = input("Would you like to go back ? ")
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        chances = -1
                        print('Thank you Mr. ', cname, 'Have a great Day')
                        break
# withdraw
            elif option == 5:
                withdraw = int(input('Enter the amount you want to withdraw: \n' '$10 $20 $50 $100 \n'))
                if withdraw in [10, 20, 50, 100]:
                   balance = balance - withdraw
                   print('\n Your new Balance is $', balance)
                   restart = input("Would you like to go back ? ")
                   if restart in ('n', 'N', 'No', 'NO', 'no'):
                    chances = -1
                    print('Thank you Mr. ', cname, 'Have a great Day')
                    break

                elif withdraw != [10, 20, 50, 100]:
                    print('Invalid Entry Try again')
                    withdraw = int(input('Enter the amount you want to withdraw: \n' '$10 $20 $50 $100 \n '))
                    if withdraw in [10, 20, 50, 100]:
                        balance = balance - withdraw
                        print('\n Your new Balance is $', balance)
                        restart = input("Would you like to go back ? ")
                        if restart in ('n', 'N', 'No', 'NO', 'no'):
                            print('Thank you Mr. ', cname, 'Have a great Day')
                    elif withdraw not in [10, 20, 50, 100]:
                        print('Transaction Timeout \n' 'Thank you for Banking with us\n')
                        chances = -1
                        break


    elif pin != (1989):
        print('Incorrect PIN')
        chances = chances-1
        if chances ==0:
            print('\n No more attempt left \n' 'Card had been Blocked Please visit your nearest branch \n' 'Thank you!!!')
            break

























