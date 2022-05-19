# when custemer entry into atm misstio
print("wellcome to  sbi atm and good day")
acno =123456
name = "karthik"
mobilenumber = "8897141511"
pin = int(input("enter pin: "))
balance = 5000
if pin==8897:
 print("pin is ok")
 cash = int(input("enter cash: "))
 if cash<=40000:
    aliasname =str(input("enter yor good name"))
    detailse='yes'
    if name  == 'karthik':
     mainbalance = balance-cash
    print("you balance now in your account: ",mainbalance,"you withdraw amount",cash)
    print("thanks for visit my atm")

    if detailse == 'yes':
        print(acno,name,pin,cash)
    else:
     print("yor name is wrong")
else:
    print("yourpin is wrong or insufficent balance")
    print("plese try to again yor pin ")
    pin = int(input("enter pin: "))
    cash = int(input("enter cash: "))
    balance = 5000
    if pin == 8897 and cash <= 40000:
        name = str(input("enter yor good name"))
        detailse = 'yes'
        if name == 'karthik':
            mainbalance = balance - cash
        print("you balance now in your account: ", mainbalance, "you withdraw amount", cash)
        print("thanks for visit my atm")
        if detailse == 'yes':
            print(name, pin, cash)
        else:
            print("yor name is wrong")
    else:
        print("yourpin is wrong or insufficent balance")
        print("limit is out off ")


    #def createAccount(self):
'''selfaccNo = input('Entertheaccountno: ')
selfname = input('Enterth accountholder  name: ')
selftype = input('Entethetype ofaccount[C / S]: ')
selfdeposit = int(input('Ente The Initialamount( >= 500or Saving and >= 1000 for current'))

print('\n\n\nAccount Created')


#def showAccount(self):
print('Account Number: ', selfaccNo)

print('AccountHolder Name: ', selfname)

print('Type ofAccount', selftype)


