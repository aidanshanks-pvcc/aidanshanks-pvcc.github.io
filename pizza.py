#Name: Aidan Shanks
#Purpose: This program finds the cost of tuition at PVCC
import datetime


yes=['Y','y','yes']
s=9.99
m=12.99
l=17.99
x=21.99
d=3.99
b=6.99
tax=.055
line='--------------------------------------'
def buyFood():
    print('Prices')
    print('Small       $'+format(s,'8,.2f'))
    print('Medium      $'+format(m,'8,.2f'))
    print('Large       $'+format(l,'8,.2f'))
    print('Extra Large $'+format(x,'8,.2f'))
    print('Drink       $'+format(d,'8,.2f'))
    print('Breadsticks $'+format(b,'8,.2f'))
    smalls=int(input("Number of Small Pizzas?"))
    meds=int(input("Number of Medium Pizzas?"))
    larges=int(input("Number of Large Pizzas?"))
    XLs=int(input("Number of XL Pizzas?"))
    drinks=int(input("Number of Drinks?"))
    bread=int(input("Number of Breadsticks?"))
    sCost=s*smalls
    mCost=m*meds
    lCost=l*larges
    xCost=x*XLs
    dCost=d*drinks
    bCost=b*bread
    pCost=sCost+mCost+lCost+xCost
    subtotal=pCost+dCost+bCost
    taxFee=subtotal*tax
    total=subtotal+taxFee
    print(line)
    print('Palermo Pizza')
    print("Expenses")
    print(line)
    print('Pizza           $'+format(pCost,'8,.2f'))
    print('Drinks          $'+format(dCost,'8,.2f'))
    print('Breadsticks     $'+format(bCost,'8,.2f'))
    print('Subtotal        $'+format(subtotal,'8,.2f'))
    print('Sales Tax       $'+format(taxFee,'8,.2f'))
    print('Total           $'+format(total,'8,.2f'))
    print(line)
    print(str(datetime.datetime.now()))


buyFood()
more=input("\nWould you like to calculate more? Y/N?")

if more in yes:
    buyFood()
else:
    print("Thank you for coming to Palermo Pizza! Enjoy your meal!")