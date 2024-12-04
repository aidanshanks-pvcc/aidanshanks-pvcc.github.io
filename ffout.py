#Name: Aidan Shanks
# Prog Purpose: This program creates a payroll report
import datetime
############## LISTS of data ############
emp = [
"Smith, James ",
"Johnson, Patricia",
"Williams, John ",
"Brown, Michael ",
"Jones, Elizabeth ",
"Garcia, Brian ",
"Miller, Deborah ",
"Davis, Timothy ",
"Rodriguez, Ronald",
"Martinez, Karen ",
"Hernandez, Lisa ",
"Lopez, Nancy ",
"Gonzales, Betty ",
"Wilson, Sandra ",
"Anderson, Margie ",
"Thomas, Daniel ",
"Taylor, Steven ",
"Moore, Andrew ",
"Jackson, Donna ",
"Martin, Yolanda ",
"Lee, Carolina ",
"Perez, Kevin ",
"Thompson, Brian ",
"White, Deborah ",]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
"C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]
hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
28, 31, 37, 32, 36, 22, 28, 29, 21, 31]
num_emps = len(emp)

grossPay=[]
fedTax=[]
stateTax=[]
socSec=[]
medicare=[]
ret401K=[]
netPay=[]

totalGross=0
totalNet=0

PAYRATE=(16.5,15.75,15.75,19.5)
DEDRATE=(.12,.03,.062,.0145,.04)

def main():
    perform()
    outputFile()

def perform():
    global totalGross, totalNet

    for i in range(num_emps):
        if job[i]=="C":
            pay = hours[i]*PAYRATE[0]
        elif job[i]=="S":
            pay = hours[i]*PAYRATE[1]
        elif job[i]=="J":
            pay = hours[i]*PAYRATE[2]
        else:
            pay = hours[i]*PAYRATE[3]

        fed=pay*DEDRATE[0]
        state=pay*DEDRATE[1]
        social=pay*DEDRATE[2]
        med=pay*DEDRATE[3]
        ret=pay*DEDRATE[4]

        net=pay-fed-state-social-med-ret

        totalGross+=pay
        totalNet+=net

        grossPay.append(pay)
        fedTax.append(fed)
        stateTax.append(state)
        socSec.append(social)
        medicare.append(med)
        ret401K.append(ret)
        netPay.append(net)
def outputFile():
    currency='8,.2f'
    line="\n-----------------------------"
    tab="\t"
    outFile="payroll.txt"
    f=open(outFile,"w")
    f.write(line)
    f.write("\n*********** FRESH FOODS MARKET **********")
    f.write("\n--------- WEEKLY PAYROLL REPORT ---------")
    f.write("\n"+tab+str(datetime.datetime.now()))
    f.write(line)
    titles1="\nEmp Name"+tab+"Code"+tab+"Gross"+tab
    titles2="Fed Inc Tax"+tab+"State Inc Tax"+tab+"Social Sec."+tab+"Medicare"+tab+"Net"
    f.write(titles1+titles2)
    for i in range(num_emps):
        data="\n"+emp[i]+"  "+job[i]+format(grossPay[i],currency)
        data1=format(fedTax[i],currency)+format(stateTax[i],currency)+format(socSec[i],currency)+format(medicare[i],currency)+format(ret401K[i],currency)+format(netPay[i],currency)
        f.write(data+data1)
    f.write(line)
    f.write("\n**************** TOTAL GROSS: $"+format(totalGross,currency))
    f.write("\n**************** TOTAL NET  : $"+format(totalNet,currency))
    f.write(line)
    f.close()
    print(f"Open {outFile} to view your report")
main()