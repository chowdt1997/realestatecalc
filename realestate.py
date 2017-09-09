#Purchase price of the property

purchaseprice = input ("What is the purchase price of the property? ")
floatpurchase = float (purchaseprice)
print ("The bidding price is " + "$" + purchaseprice)
print ("Good Luck at the auction!")

#Calculate Eastside Funding downpayment
efdown = floatpurchase * 0.10
print ("Eastside funding downpayment is 10% of the purchase price \n")
print ("Which is $" + str (efdown))

#Calculate Monthly Interest if financing with Eastside Funding
numofmonths = input ("What is the number of months you are financing? ")
floatnumofmonths = float (numofmonths)
amountfinanced = floatpurchase - efdown
print (("This is the amount you are financing $")+(str (amountfinanced)))

#County taxed assessed value
assessedvalue = float (input ("What is the County Assessed Value? "))
excisetaxpercent = float(0.0178)
excisefee = float (excisetaxpercent * assessedvalue)
print ("\n The County excise fee is " + "$" + str (excisefee))

#Calculate Vestus commission
vestuscommtaxpercent = float (0.03)
vestuscommission = float (vestuscommtaxpercent * assessedvalue)
print ("\n Vestus Agent Commission is $" + str (vestuscommission))

#Other fixed fees including loan processing fee, recording, reconveyence, docprep
totalfixedfees = float (780.00)

#Calculate and display total cash to bring to auction
print ('''This is the amount of cash that you need to fund this deal,
see the following breakdown: \n''')

print ("Line Item    \t\t\t$Amount of Cash \n")
print ("Fixed Fees   \t\t\t$" + str (totalfixedfees))
