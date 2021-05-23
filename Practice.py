# '''
# Project name : IAABank
# Programmer: Rakesh Kumar Jangid
# Date : (11-March-2021) - (11-March-2021)
# '''

#NOTE Dictionary is unordered but mutable in nature & in the form of 'Key:Value' Pair.  Strictly No duplication allowed in key (but Value can be).
#      We can access value threw 'Key'. All mixed data type allowed.








# Bank Details Dictionary of 10 users
# Here we using Users_ID 1 to 10 as a primary key to related all Nested dictionary aspects elements.
Users_Details = {
'Users_Name' : {1:"Rakesh" , 2:"Parul" , 3:"Ankit" , 4:"Monu" , 5:"Manish" , 6:"Bittu" , 7:"Jeetu" , 8:"Ajay" , 9:"Harsh" , 10:"Khali"},
'Users_ID' :   {1:1 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10},
'Users_Balance' : {1:1000 , 2:4000 , 3:11000 , 4:1020 , 5:1000 , 6:1200 , 7:1860 , 8:1600 , 9:1800 , 10:1000},
'Users_Password' : {1:"Rakesh" , 2:"Parul" , 3:"Ankit" , 4:"Monu" , 5:"Manish" , 6:"Bittu" , 7:"Jeetu" , 8:"Ajay" , 9:"Harsh" , 10:"Khali"} 
}

# --------------------------------------------------------------------------------------------------------------------------------------------


# Starting Messages and 
count = 0                                                                                                                   # Count keep 0 (It will increase after each wrong attempt)
Attempt = 3   # We can simply put value with like =   While count < 3:                                                                                                              # Attempt range keep 3 (count keep trying to make equal then attempt to make while condition false )
while count < Attempt:                                                                                                      # While condition not become false (3 Attempt)
    print("******************************************************************************************************")
    print("\t\t\t\t\t Welcome to IAA Bank")
    print("\t\t\t\\____________________________________________________/\n\n")
    input1 = int(input("Please Enter Your Account Number:  "))                                                              # input1 = Enter Users ID as a Account Number
    password = (input("Enter Your Password : "))                                                                            # Enter Password of Account Number



# Users Authentication check  
    if (password == Users_Details['Users_Password'][input1]):                                                               # Password Checking into Dictionary 'Users_Password' Key
        print("\t\t\t\t\t Welcome " + Users_Details['Users_Name'][input1] +" to IAABank !")                                 # Entry Level Welcome Message
        print("\t\t\t\t\t______________________________")                     
        print("\t\t\t\t\t 1. User Details > \n\t\t\t\t\t 2. Transaction >\n\t\t\t\t\t 3. Exit >")                           # Print 3 Options in Main Menu
        input2 = int(input( '\n\t\t\t\t\t Please choose your Option:   '))                                                  # input2 = give option to choose



# User Details OPtion
        if (input2 == 1 ):                                                                                                  # If we choose Section 1 of main menu (Users Details)
            print("Welcome " + Users_Details['Users_Name'][input1] + " Your Details are :" )                                # Welcome details Message with showing Name
            print("______________________________")
            print(". User_ID =  ", Users_Details['Users_ID'][input1])                                                       # User ID as a first User Details
            print(". User_Name =  ",Users_Details['Users_Name'][input1])                                                    # User Name as a Second Users Details
            print(". User_Balance =  ",Users_Details['Users_Balance'][input1],"\n\n\t")                                     # Users Main Balance in account Present
            print("\t\t\t\t\tYou are in User Details Section !")                                                
            print("\t\t\t\t\t______________________________")
            print("\n\t\t\t\t\t Choose Option :- \n\t\t\t\t\t 1. Main Menu \n\t\t\t\t\t 2. Exit")                           # Give Nested option inside, after showing Users Details to proceeds 
            input3 = (int(input("\t\t\t\t\t Choose Option for further process ")))                                          # Input3 = Input as choose option into main menu or exit
    
            if(input3 == 1):                                                                                                # If we choose back to main menu 1 option
                pass # return(input1) > Here I need your help "Harry Bhai" # I dont know how to return back to main menu so i use here pass statement
            elif(input3 == 2):                                                                                              # If we choose exit to trnasaction 2 option inside of Users Details Section
                print("Thank you, to using IAA BANK !")
                break                                                                                                       # Terminate the program code
            else:                                                                                                           # If you press wrong key, insted of main menu or exit 
                print("Your Transaction Suspended !")
                print("Thank you, using to IAA BANK")                                                                       # I am not using here break statement



# Transaction option Choosen by the user
        elif(input2 == 2):                                                                                                  # Choose Section 2 (Transaction)
            print("Welcome in Transaction Option")
            print("______________________________")
            input4 = int(input("Choose Option : \n 1. Debit :\n 2. Credit : \n 3. Transfer Money :  "))                     # Give 3 Options to user in transaction section 
            
            if(input4 == 1):                                                                                                # Choose Option of Debit amount
                print("\t\t\t\t\t Debit Amount !")                                                                                 
                print("\t\t\t\t______________________________")
                print(f"\t\t\t\t > You have {Users_Details['Users_Balance'][input1]}, balance left !")                      # Using f string inside print section
                input5 = int(input("\t\t\t\t > Enter Debited Amount:  "))                                                   # input5 as debit amount input
                if(input5 < Users_Details['Users_Balance'][input1]):                                                        # Check wether user have sufficient balance to make debit transaction
                    Users_Details['Users_Balance'][input1] = (Users_Details['Users_Balance'][input1]) - input5              # Debit from user account and update to new value in dictionary users balance 
                    print("\n\n\t\t\t\t< You have left ", Users_Details['Users_Balance'][input1] , "in your account >")     # Balance left in account
                    break                                                                                                   # Transaction Complete(Terminate the program)
                else:                                                                                                       # If user have not sufficient balance to make debit transaction
                    print("\n\n\t\t < You have unsufficient balance in your account to make a debit transaction >")          
                    break                                                                                                   # break transaction 
            elif(input4 == 2):                                                                                              # Choose Option credit amount
                input6 = int(input("\n\n\t\t\t\t\tCredit Amount: "))                                                        # input6 = as a Credit amount input from user
                print("\t\t\t\t______________________________")
                Users_Details['Users_Balance'][input1] = Users_Details['Users_Balance'][input1] + input6                    # Credit amount in self account
                print("\n\t\t\t < Your current account balance is ", Users_Details['Users_Balance'][input1], ">")           # Balance increse after make credit transaction
                break                                                                                                       # Terminate program after completion process

            elif(input4 == 3):                                                                                              # If user choose Transfer money option
                print("\n\n\t\t\t Which account Id, you want to transfer money !")                                          # In Which id do yu want to transfer money
                input7 = int(input("\t\t\t\t Enter Users_ID : "))                                                           # input7 = as receiver user id(Account Number) 
                print("\nYou are crediting amount to", Users_Details['Users_Name'][input7])                                 # Show which account you transfering money
                                       
                if(input7 == (Users_Details['Users_ID'][input7])):                                                          # check Users or user ID exist in bank or not
                    input8 = int(input("Transfer Credit Amount:  "))                                                        # If condition true, then enter transfer money amount
                    if(input8 < Users_Details['Users_Balance'][input1]):                                                    # Is user have able to transfer money or not
                        Users_Details['Users_Balance'][input7] + input8                                                     # If Conndition true, Make transfer
                        print("\nThank you !\n You have", Users_Details['Users_Balance'][input1] - (input8), "Balance Left !")          # Balance left in your account 
                        break                                                                                                           # Terminate program after completition transaction
                    else:                                                                                                               # If user have not sufficient balance to transfer money
                        print("You have unsufficient balance in your account to transfer money !")
                else:                                                                                                 
                    print("Wrong Account Number")                                                                                       # If users id does not exiatance in bank dictionary
                        
            else:                                                                                                                       # If both option does not press by the user
                print("Wrong Input !")
                break                                                                                                                   # Terminate the program




# Exit Option Choosen by the user 
        elif(input2 == 3):                                                                                                              # User press exit key insted of users details and transaction option
            print("Thank you, to using IAA BANK")
            break
        else:
            print("You have press wrong option key !")
            break
    else:
        print("Wrong Password")                                                                                                         # When user press wrong password for user Account
        count = count + 1                                                                                                               # Count is increasing by itself by 1 each time of loop




        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        # Regards to "CodeWithHarry" Youtube Channel
        # Thanks !