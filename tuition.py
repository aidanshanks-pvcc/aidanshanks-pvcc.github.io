#Name: Aidan Shanks
#Purpose: This program finds the cost of tuition at PVCC
import datetime


yes=['Y','y','yes']
instFee=1.75
SAF=2.9
locale=input("In State?")
if locale in yes:
    tuition=164.4
    capitalFee=0
else:
    tuition=353
    capitalFee=26


def buyFood():
    credits=int(input("Number of Credits?"))
    scholarship=int(input("Amount of Scholarship?"))
    tPrice=credits*tuition
    cPrice=credits*capitalFee
    sPrice=credits*SAF
    iPrice=credits*instFee
    subtotal=tPrice+cPrice+sPrice+iPrice
    total=subtotal-scholarship
    line='--------------------------------------'
    print(line)
    print('Piedmont Virginia Community College')
    print("Tuition and Fees Report")
    print(line)
    print('Tuition                    $'+format(tPrice,'8,.2f'))
    print('Capital Fees               $'+format(cPrice,'8,.2f'))
    print('Student Activity Fees      $'+format(sPrice,'8,.2f'))
    print('Institutional Fees         $'+format(iPrice,'8,.2f'))
    print('Price pre Scholarships     $'+format(subtotal,'8,.2f'))
    print('Scholarships               $'+format(scholarship,'8,.2f'))
    print('Final Price                $'+format(total,'8,.2f'))
    print(line)
    print(str(datetime.datetime.now()))


buyFood()
more=input("\nWould you like to calculate more? Y/N?")

if more in yes:
    buyFood()
else:
    print("Thank you for coming to Branch Barbeque Buffet! Enjoy your meal!")