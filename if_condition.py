a = ["Asia","Europe","Africa","North America","South America","Antartica","Australia"]
b = ["India","Pakistan","Bangladeh","Nepal","China","Russia"]
c = ["Delhi","Rajasthan","Gujrat","Utrakhand","South","Goa"]
d = ["Jaipur","Dausa","Udaipur","Kota","Bharatpur","Alwar","Ajmer"]
e = ["Manpur","Sikrai","Ranapada","Nikatpuri","Sikandra"]
f = [1,2,3,4,5]


input1 = input("Enter Continante Name : ")
if input1 in a:
    print(f"Welcome to {input1}")


    if input1 == "Asia":
        print("Are you want to go more deep ?")
        ask = input("Enter y/n :  ")
        if ask == "y":
            input2 = input("Enter Country Name : ")

            if input2 in b :
                print(f"Welcome to {input2}")

                if input2 == "India":
                    print("Are You want to go more deep ?")

                    ask = input("Enter y/n :  ")

                    if ask == "y":
                            
                        input3 = input("Enter state name please : ")

                        if input3 in c :
                            print(f"Welcome in {input3}")

                            if input3 == "Rajasthan":
                                print("Are you want to go more deep ? ")

                                ask = input ("Enter y/n :  ")

                                if ask == "y":
                                    input4 = input("Enter city name : ")

                                    if input4 in d:
                                        print(f"Welcome in {input4}")

                                        if input4 == "Dausa":

                                            print("Are you want to more deep ? ")

                                            ask = input("Enter y/n :  ")

                                            if ask == "y":
                                                    
                                                input5 = input("Enter Village name : ")

                                                if input5 in e:
                                                    print(f"Welcome in {input5}")

                                                    if input5 == "Manpur":
                                                        print("Are you want to go more deep ? ")

                                                        ask = input("Enter y/n : ")

                                                        if ask == "y":
                                                            input6 = int(input("Enter ward number : "))

                                                            if input6 in f:
                                                                print(f"Welcome in {input6}")

                                                                if input6 == 2:
                                                                    print("You won !")

                                                                else:
                                                                    print("ohhhhh....   You just missed this answer..")
                                                                    print("Dont worry try again.. ")

                                                            else:
                                                                print("This place is not in the list ")

                                                        else:
                                                            print("You just missed one step to win")
                                                            print(f"You were at {input6}")
                                                
                                                    else:
                                                        print("Wrong choose")                                            

                                                else:
                                                    print("This place is not in the list ")

                                            else:
                                                print(f"Thank you for this journey till {input4}")
                                        else:
                                            print("Wrong choose.")
                                    else:
                                        print("This place is not in the list ")

                                else:

                                    print(f"Thank you for this journey till {input3}")
                            else:
                                print("Wrong choose !")
                        else:
                            print("This place is not in the list ")

                    else:
                        print(f"Thank You for this journey till {input2}")
                else:
                    print("Wrong choose !")    
            else:
                print("This place is not in the list ")
            
        else:
            print(f"Thank you for this journey till {input1}")
    else:
        print("Wrong choose from starting !")
else:
    print("This place is not in the list ")            