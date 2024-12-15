# Name: your-name-here
# Prog Purpose: This program finds the cost of movie tickets, popcorn, & drinks
#   The output is sent to an .html file

import datetime

##############  define global variables ############
# Forms of Yes
yes=['Y','y','yes']
# define tax rate and prices
INSTFEE=1.75
SAF=2.9

# define global variables

numCredits = 0

tuitionFee = 0
capitalFee = 0
scholarship = 0

tPrice=0
cPrice=0
sPrice=0
iPrice=0

subtotal = 0
total = 0

# create output file
outfile = 'pvccweb.html'


##############  define program functions ################
def main():
    
    open_outfile()
    moreCredits = True
    
    while moreCredits:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        askAgain = input('\nWould you like to order again (Y or N)?: ' )
        if askAgain.upper() == 'N':
            moreCredits = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Piedmont Virginia Community College </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #dadada; background-image: url(wp-pvcc.png); color: #eb2536;">\n')
    
def get_user_data():
    global numCredits,tuitionFee,capitalFee, scholarship
    locale=input("In State?")
    if locale in yes:
        tuitionFee=164.4
        capitalFee=0
    else:
        tuitionFee=353
        capitalFee=26
    numCredits = int(input('Number of Credits: '))
    scholarship = int(input("Amount of Scholarship: "))

def perform_calculations():
    global tPrice, cPrice, sPrice, iPrice, tuitionFee, capitalFee, subtotal, total
    tPrice=numCredits*tuitionFee
    cPrice=numCredits*capitalFee
    sPrice=numCredits*SAF
    iPrice=numCredits*INSTFEE
    subtotal=tPrice+cPrice+sPrice+iPrice
    total=subtotal-scholarship

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:19]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #dadada  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>PVCC Tuition</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Your Piedmont Virigina Community college Price ***\n')
    
    f.write(tr + 'Credits' + endtd + str(numCredits) + endtr)
    f.write(tr + 'Tuition' + endtd + str(tuitionFee) + endtd + format(tPrice,currency) + endtr)
    f.write(tr + 'Capital Fees' + endtd + str(capitalFee) + endtd + format(cPrice,currency) + endtr)
    f.write(tr + 'Student Activity Fees ' + endtd + str(SAF) + endtd +  format(sPrice,currency)  + endtr)
    f.write(tr + 'Institutional Fees ' + endtd + str(INSTFEE) + endtd +  format(iPrice,currency)  + endtr)

    f.write(tr + 'Price Before Scholarships' +  endtd + sp + endtd + format(subtotal,currency)  + endtr)     
    f.write(tr + 'Scholarships' + endtd + sp + endtd + format(scholarship,currency) + endtr)
    f.write(tr + 'TOTAL' +     endtd + sp + endtd + format(total,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


##########  call on main program to execute ############
main()              


