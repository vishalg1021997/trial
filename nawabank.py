#AAj Apun Baneyge Apna Personal Bank

class bank:
    print("WELCOME TO PYTHON BANK")

    print("Enter YOUR NAME TO START TRANSACTION")
##THIS BLOCK OF CODE WILL CHECK IF THE USER EXIST IF NOT IT WILL ASK TO REGISTER IF USER NOT EXIST
#THIS WILL ACCEPT SINGLE STR_VALUE FROM THE USER
    def enter_name(self, name):
        user = ['vishal', 'nilesh', 'kanishka', 'ananya']
        self.user_name = name
        self.balance = 1000
        if self.user_name in user:
            print("Hello", self.user_name, "What Kind Of transaction Would You Like To Do")
        else:
            print("User Not Found Error 404")
            print("Press 1 To Register Yourself OR","Any Other Number To Exist")
            ent = int(input())
            if ent == 1:
                print("Hi My Name Is Mohit Chouchan \n", "PLEASE Enter Your Name To Create a Account")
                new_user = input()
                user.append(new_user)
                print(new_user,"Your Account Is Created Sucessfully Happy Banking")
            else:
                exit()
#THIS BLOCK OF CODE WILL DISPLAY THE OPTION WHICH USER CAN PERFORM
    def menu(self):
        print("1 For Deposit/Withdraw")
        print("2 For Check Balance")
        print("3 For Add Benificary")
        print("4 For Transfer")


#IF USER SELECT OPTION 1 THE THIS BLOCK OF CODE WILL RUN IT WILL ACCEPT TWO VALUES FROM THE USER
#1 STR_VALUE AND 2 INT_VALUE SPACE SEPRATED USER CAN DEPOSIT OR WITHDRAW FROM HIS ACCOUNT
    def given_option1(self,trans_type,amount):
        self.user_trans = trans_type
        #self.user_amount = amount
        if self.user_trans == 'credit':   #USER HAS TO ENTER CREDIT TO DEPOSIT
            self.balance = self.balance + int(amount)
        elif self.user_trans == 'debit':   #USER HAS TO ENTER DEBIT TO WITHDRAW
            self.balance = self.balance - int(amount)
        else:                              #IF ANY OTHER VALUE GIVEN USER WILL GET THIS BELOW MESSAGE
            print("Enter Correct Transaction Type")

#USER CAN ADD BENIFICARY TO HIS ACCOUNT IF HE WANTS TO MAKE ANY TRANSFER OF MONEY THIS WILL ACCEPT 1 STR_VALUE
    def add_benificary(self,name):
        list_of_benificary = ['atul','shubham']
        self.benificary_name = name
        if self.benificary_name not in list_of_benificary:   #IF THE BENICIARY NOT IN LIST IT WILL ADD BENIFICARY
            list_of_benificary.append(self.benificary_name)  #AND DISPLAY SUCESSFUL MESSAGE
            print("Benificary",self.benificary_name,"Added Sucesfully\n""Benificary In Your Ac are",list_of_benificary)
        else:                      #IF BENIFICARY ALREADY EXISTS IT WILL DISBLAY BELOW MESSAGE
            print("Benificary",self.benificary_name,"Already Exist\n""Benificary In Your Ac are",list_of_benificary)
        return list_of_benificary


openbank = bank()
openbank.enter_name(input())
openbank.menu()
while(True):    #THE LOOP WILL RUN UNTIL THE USER WANTS TO STOP THE LOOP SO USER CAN DO CONTINUES TRANSACTION
    choice = int(input()) #ASK THE USER TO ENTER THE TRANSACTION NUMBER 1,2,3,4
    if choice == 1: #IF 1 USER WILL BE ALLOWED TO DO CREDIT AND DEBIT IN HIS ACCOUNT
        print("For Deposit Enter credit and amount --- For Withdraw Enter debit and amount")
        len_den , paisa = input().split()
        openbank.given_option1(len_den,paisa) #HERE ATTRIBUTE IS CALL WHICH IS IN CLASS BANK TO MAKE CREDIT DEBIT
        print("Your Acount Balance After Current Transaction is",openbank.balance) #DISPLAY THE BALANCE OF THE AC
        print("Will You Like To Do Another Transaction Y/N")
        more = input() #IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
        if more == 'Y':
            openbank.menu()
            continue
        else:
            exit()

    elif choice == 2:#IF 2 USER CAN CHECK HIS ACCOUNT BALANCE
        print("Your Acount Balance After is", openbank.balance)
        print("Will You Like To Do Another Transaction Y/N")
        more = input()#IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
        if more == 'Y':
            openbank.menu()
            continue
        else:
            exit()

    elif choice == 3:#IF 3 USER CAN ADD BENIFICARY TO HIS ACCOUNT TO MAKE TRANSACTION
        print("Enter The Name Of The Benificary You Want To Add")
        openbank.add_benificary(input())#ATTRIBUTE TO ADD_BENIFICARY IS CALL IN CLASS BANK
        print("Will You Like To Do Another Transaction Y/N")
        more = input()#IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
        if more == 'Y':
            openbank.menu()
            continue
        else:
            exit()

    elif choice == 4: #IF 4 USER CAN TRANSFER AMOUNT TO THE BENIFICARY IN LIST
        print("Enter The Benificary Name and Amount To Transfer ")
        ben_name, trans_amount = input().split() #THIS WILL ACCEPT 2 VALUE FROM USER STR AND INT SPACE SEPRATED
        return_value = openbank.add_benificary(ben_name).copy()#THIS WILL GET THE COPY OF BENIFIFCIARY LIST
                                                              # AND CHECK IF THE BENFICIARY IS AVILABLE OR NOT
                                                              # IF NOT IT WILL ADD THE BENIFIFCIARY IN THE LIST
#THIS BELOW CODE WILL CHECK IF THE SUFFICENT BALANCE IS AVIALBLE
# IN THE USER ACCOUNT OR NOT AND ACCORDINGLY GIVE THE MESSAGE
        if openbank.balance < int(trans_amount):#LESS BALANCE
            print("No Sufficent Balance Please Deposit Some Money","\n Click On Y TO Proceed")
            more = input()#IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
            if more == 'Y':
                openbank.menu()
                continue
            else:
                exit()
        if openbank.balance > int(trans_amount):#HAVE BALANCE DO SUCESSFUL TRANSACTION
            openbank.balance = openbank.balance - int(trans_amount)
            print(int(trans_amount),"Got Transfered Sucessfully To",ben_name,"\n Your Current Balance is",openbank.balance)
            print("Will You Like To Do Another Transaction Y/N")
            more = input()
            if more == 'Y':#IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
                openbank.menu()
                continue
            else:
                exit()
        if openbank.balance == int(trans_amount):#GIVES WARRNING AFTER THIS TRANSACTION USER AC_BAL WILL BE ZERO
                                                # SO ASK FOR THE CONFIRMATION STILL WOULD HE LIKE TO DO OR NOT
                                                #IF CUSTOMER DECLINES THE TRANSFER IS CNCELLED
            print("WARNING After This Transaction Your Account Balance Will Be Zero Press Y to Continue")
            confirmation = input()
            if confirmation == 'Y':
                openbank.balance = openbank.balance - int(trans_amount)
                print(int(trans_amount), "Got Transfered Sucessfully To", ben_name, "\n Your Current Balance is",
                      openbank.balance)
                print("Will You Like To Do Another Transaction Y/N")
                more = input()
                if more == 'Y':#IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
                    openbank.menu()
                    continue
                else:
                    exit()
            else:
                print("Transfer Cancelled")
                print("Will You Like To Do Another Transaction Y/N")
                more = input()
                if more == 'Y':#IF USER WANTS TO DO MORE TRANSACTION HE HAS TO ENTER Y OR TO STOP ENTER N
                    openbank.menu()
                    continue
                else:
                    exit()