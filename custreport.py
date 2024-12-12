#Name: Aidan Shanks
#Purpose: Read a CSV and increase values 10% if late
#Last, First, owed, days late

infile = "customer_data_file.csv"

custInDataBlockList = []
cust = []

LATEFEERATE = .1
grandTotal = 0

def main():
    read()
    math()
    show()

def read():
    custDataFile = open(infile, "r")

    custInDataBlockList=custDataFile.readlines()
    custDataFile.close()
    for i in custInDataBlockList:
        cust.append(i.split(","))

def math():
    global grandTotal

    for i in range(len(cust)):
        owed = float(cust[i][2])
        daysLate = int(cust[i][3])

        if daysLate > 0:
            lateFee = owed * LATEFEERATE
        else:
            lateFee = 0
        owed += lateFee
        grandTotal += owed
        cust[i][2] = owed
def show():

    currency = "8,.2f"
    line = "---------------------"
    tab ="\t"

    print(line)
    print("***** Customer Balance Report *****")
    print("Name                New Amount Owed")
    print(line)

    for i in range(len(cust)):
        print(cust[i][1]+ "  " + tab + cust[i][0]+ tab + format(cust[i][2], currency))
    
    print(line)
    print("***** Grand Total:\t$" + format(grandTotal, currency))
main()