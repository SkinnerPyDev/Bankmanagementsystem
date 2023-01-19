
import csv

class Bank:
    def __init__(self):
        self.details = []
        self.logged_in = False
        self.balance = 0
    
    #Create an account

    def resgister(self, name, pn, pin,balance=0):
        
        condtion = True
        
        if len(str(pn)) >10 or len(str(pn))<10:
            print("-------------------------------------")
            print("Invalid phone number!")
            print("-------------------------------------")
            condtion  = False
            
        if len(str(pin)) <4 or len(str(pin))>6:
            print("-------------------------------------")
            print("Pin should be between 4 to 6 digit")
            print("-------------------------------------")
            condtion = False
        
        if condtion:
            print("-------------------------------------")
            print("Account created succesfully")
            print("-------------------------------------")

            with open("data.csv","a") as file:
                data = csv.DictWriter(file,fieldnames = ["name","pn","pin","balance"])
                data.writerow({"name":"name","pn":"pn","pin":"pin","balance":"balance"})
                data.writerow({"name":name,"pn":pn,"pin":pin,"balance": balance})

    #Custmor Login:

    def login(self, name,pin):
        details = []
        with open("data.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                details.append({"name":row["name"],"pin":row["pin"]}) 
        if not any(key["name"]==name and key["pin"] == str(pin) for key in details):
            print("-------------------------------------")
            print("wrong details")
            print("-------------------------------------")
            self.logged_in = False
        else:
            print("-------------------------------------")
            print(f'{name.capitalize()} logged in...')
            print("-------------------------------------")
            self.logged_in = True

    #deposite money

    def deposite(self,pin,name):
        ammount = 0
        with open("data.csv", "r") as f_in:
            reader = csv.DictReader(f_in)
            data = list(reader)
        for row in data:
            if row["pin"] == str(pin) and row["name"] == name:
                while True:
                    try:
                        ammount = int(input("Enter the ammount: "))
                        if ammount > 0:
                            self.balance = int(row["balance"])
                            self.balance+=ammount
                            row["balance"] = str(self.balance)
                            print("Ammount has been deposited")
                            break
                    except ValueError:
                        print("--------------------------------------")
                        print("Invalid input")
                        print("--------------------------------------")
                        continue
        with open("data.csv", "w") as f_out:
            writer = csv.DictWriter(f_out, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    #cheack balance

    def check_balance(self,pin,name):
        with open("data.csv", "r") as f_in:
            reader = csv.DictReader(f_in)
            data = list(reader)
        for row in data:
            if row["pin"] == str(pin) and row["name"] == name:
                self.balance = int(row["balance"])
        return self.balance

    #withdraw money

    def withdraw(self):
        ammount = 0
        with open("data.csv", "r") as f_in:
            reader = csv.DictReader(f_in)
            data = list(reader)
        for row in data:
            if row["pin"] == str(pin) and row["name"] == name:
                while True:
                    try:
                        ammount = int(input("Enter the ammount: "))
                    except ValueError:
                        print("----------------------------")   
                        print("Invalid input")
                        print("----------------------------")   
                        continue
                    if ammount <= 0: 
                        print("----------------------------")   
                        print("Please enter a valid ammount")
                        print("----------------------------")   
                    elif ammount < int(row["balance"]):
                        self.balance = int(row["balance"])
                        self.balance-=ammount
                        row["balance"] = str(self.balance)
                        print("Ammount has been withdraw")
                        break
                    else:  
                        print("-----------------------------------------")  
                        print("Sorry! Not enough money")
                        break


        with open("data.csv", "w") as f_out:
            writer = csv.DictWriter(f_out, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)  

    def transferMoney(self,name,pin,tname,tpn,Transfer_amt):
        current_bal = 0
        with open("data.csv", "r") as f_in:
            reader = csv.DictReader(f_in)
            data = list(reader)
        for row in data:
            if row["pin"] == str(pin) and row["name"] == name:
                if Transfer_amt> int(row["balance"]):
                    print("---------------------------------------------------")
                    print("You dont have enough balance")
                    print(f'Your current balance is {bank.check_balance(name,pin)} RS') 
                    print("---------------------------------------------------")
                else:
                    self.balance = int(row["balance"]) - Transfer_amt
                    row["balance"] = str(self.balance)
                    current_bal = row["balance"]
                    for row in data:
                        if row["name"] == tname and row["pn"] == str(tpn):
                            self.balance = int(row["balance"]) + Transfer_amt
                            row["balance"] = str(self.balance)
                            print("---------------------------------------------------")
                            print("Money has been tranfered succesfully")
                            print(f'Your current balance is {current_bal} RS') 
                            print("---------------------------------------------------")
                            break
                    else:
                        print("----------------------------")
                        print("Wonrg details")
                        print("----------------------------")

        with open("data.csv", "w") as f_out:
            writer = csv.DictWriter(f_out, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
bank = Bank()
print("**************************************")
print("\tWelcome to Nitesh's Bank\n")
print("**************************************")
while True:
    ch = input("1.Resister a new user\n2.login\n3.Quit\n")
    if ch == "1":
        while True:
            try:
                name = input("Please enter your full name: ")
                pn = int(input("Enter your phone number: "))
                pin = int(input("Create your pin: "))
                bank.resgister(name,pn,pin)
                break
            except ValueError:
                print("--------------------")
                print("Invalid input")
                print("--------------------")
                continue
    elif ch ==  "2":
        while True:
            try:
                name = input("Enter your name: ")
                pin = int(input("Enter your pin: "))
                bank.login(name,pin)
                break
            except ValueError:
                print("---------------------------------------------------")
                print("Invalid details please enter again")
                print("---------------------------------------------------")
                continue
        #bank.login(name,pin)
        if bank.logged_in == True:
            while True:
                choice = input("1.Check your balance\n2.Deposite money\n3.Withdraw money\n4.Transfer Money\n5.Log out\n")
                if choice == "1":
                    current_bal = bank.check_balance(pin,name)
                    print("---------------------------------------------------")
                    print(f'Your current balance is {current_bal} RS')
                    print("---------------------------------------------------")
                elif choice == "2":
                    print("---------------------------------------------------")
                    bank.deposite(pin,name)
                    print("---------------------------------------------------")
                    print(f'Your current balance is {bank.check_balance(pin,name)} RS')
                    print("---------------------------------------------------")
                elif choice == "3":
                    bank.withdraw()
                    print("-----------------------------------------")  
                    print(f'Your current balance is {bank.check_balance(pin,name)} RS') 
                    print("-----------------------------------------")   

                elif choice == "4":
                    #
                    while True:
                        try:
                            Transfer_amt = int(input("Enter the ammount: "))
                            break
                        except ValueError:
                            print("Invalid input")
                            continue
                    tname = input("Enter the name: ")
                    while True:
                        try:
                            tpn = int(input("Enter phone number: "))
                            break
                        except ValueError:
                            print("Invalid input")
                            continue

                    bank.transferMoney(name,pin,tname,tpn,Transfer_amt)
                elif choice == "5":
                    break
    else:
        quit()
