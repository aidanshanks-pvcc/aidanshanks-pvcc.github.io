#Name: Aidan Shanks
#Purpose: This program finds the cost of movie tickets
import datetime

tickPrice=10.99
taxRate=.055
yes=['Y','y','yes']

def buyTickets():
    num=int(input("Number of movie tickets: "))
    subtotal=num*tickPrice
    taxes=taxRate*subtotal
    total=subtotal+taxes
    print('---------------------------')
    print('****Cinema House Movies****')
    print("Your neighborhood movie house")
    print("---------------------------")
    print('Tickets        $'+format(subtotal,'8,.2f'))
    print("Sales Tax      $"+ format(taxes,'8,.2f'))
    print("Total          $"+format(total,'8,.2f'))
    print("---------------------------")
    print(str(datetime.datetime.now()))
    more=input("\nWould you like to order again Y/N?")

    if more in yes:
        buyTickets()
    else:
        print("Thank you for your order. Enjoy your movie!")

buyTickets()
