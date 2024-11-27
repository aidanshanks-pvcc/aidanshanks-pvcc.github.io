#Name: Aidan Shanks
#Purpose: This program finds the cost of property tax
import datetime

pptRate=.042
reliefRate=.33
vehicle=["2019 Volvo",
         "2018 Toyota",
         "2022 Kia",
         "2020 Ford",
         "2023 Honda",
         "2019 Lexus"]
vehicleValue=[13000,10200,17000,21000,28000,16700]
pptrE=["Y","Y","N","Y","N","Y"]
owner=["Brand,Debra",
       "Smith,Carter",
       "Johnson,Bradley",
       "Garcia,Jennifer",
       "Henderson,Leticia",
       "White,Danielle"]
pptOwed=[]
numVehicles=len(vehicle)
taxDue=0
total=0
for i in range(numVehicles):
    taxDue=(vehicleValue[i]*pptRate)/2
    if pptrE[i].upper() == "Y":
        taxDue=taxDue*(1-reliefRate)
    pptOwed.append(taxDue)
    total=total+taxDue
date=str(datetime.datetime.now())
moneyf='8,.2f'
line="------------------------------------------------------"
tab="\t"
print(line)
print("*************Personal Property Tax Report*************")
print("              Charlottesville, Virginia")
print("\n\tdate:"+date)
print("\nName"+tab+tab+tab+"Vehicle"+tab+tab+"Relief"+tab+"Tax Due")
print(line)
for i in range(numVehicles):
    dataline1=owner[i]+tab+vehicle[i]+tab+format(vehicleValue[i],moneyf)+tab
    dataline2=pptrE[i]+tab+format(pptOwed[i],moneyf)
    print(dataline1+dataline2)
print(line)
print("****************************Tax Due: "+ tab + format(total,moneyf))