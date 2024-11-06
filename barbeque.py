#Name: Aidan Shanks
#Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
import datetime

adultPrice=19.95
childPrice=11.95
serviceRate=.01
taxRate=.062
yes=['Y','y','yes']

def buyFood():
    adultNum=int(input("Number of adults: "))
    childNum=int(input("Number of Children: "))
    aTotal=adultNum*adultPrice
    cTotal=childNum*childPrice
    subtotal=aTotal+cTotal
    serviceFee=subtotal*serviceRate
    taxes=taxRate*subtotal
    total=subtotal+taxes+serviceFee
    print('--------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print("--------------------------------")
    print('Adults                 $'+format(aTotal,'8,.2f'))
    print('Children               $'+format(cTotal,'8,.2f'))
    print('Subtotal               $'+format(subtotal,'8,.2f'))
    print('Service fee            $'+format(serviceFee,'8,.2f'))
    print("Sales Tax              $"+ format(taxes,'8,.2f'))
    print("Total                  $"+format(total,'8,.2f'))
    print("--------------------------------")
    print(str(datetime.datetime.now()))


buyFood()
more=input("\nWould you like to order again Y/N?")

if more in yes:
    buyFood()
else:
    print("Thank you for coming to Branch Barbeque Buffet! Enjoy your meal!")