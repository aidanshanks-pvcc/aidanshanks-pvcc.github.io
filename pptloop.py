#Name: Aidan Shanks
#Purpose: This program finds the cost of property tax
import datetime
yes=("y","Y","Yes","yes","YES")
pptRate=.042
reliefRate=.33
def main():
    value=int(input("What is the assessed value of your vehicle(in dollars)?:"))
    relief=input("Does this vehicle qualify for relief(Y/N?")
    taxDue=0
    total=0
    reliefA=0
    taxDue=(value*pptRate)/2
    if relief in yes:
        reliefA=reliefRate*taxDue
        taxDue=taxDue*(1-reliefRate)
    total=taxDue
    annual=2*total    

    date=str(datetime.datetime.now())
    moneyf='8,.2f'
    line="------------------------------------------------------"
    tab="\t"
    print(line)
    print("*************Personal Property Tax Report*************")
    print("              Charlottesville, Virginia")
    print("\n\tdate:"+date)
    print(line)
    print("\tAssessed Value      $"+format(value,'8,.2f'))
    print("\tRelief Amount       $"+format(reliefA,'8,.2f'))
    print("\tFull Annual Amount  $"+format(annual,'8,.2f'))
    print(line)
    print("\tTax Due: "+ tab + format(total,moneyf))
again=True
while again==True:
    main()
    a=input("Would you like to calculate another vehicle(Y/N)?")
    if a in yes:
        again=False