# nested if - elif - else statement
# Note: 
#  Python allow conditional statements to contain another conditional statement.
#  This structure is found in nested if - elif - else statement
#  Nesting can go as deep as you would want it to go
# if statement can also be checked inside other if statement. This conditional statement is called nested if statement. 
# This means that inner if condition will be checked. only if outer if condition is true and by this.
#  we can see multiple conditions to be satisfied

a = '''
Syntax:  

        if(Contion 1 )  --------------------------------|       # If Condition Start                
            if(Condition 1.1):----------------------|   | # Nesting If                              
                Statement 1.1                       |   |                                           
            elif(Condition 1.2):                    |   | # Nesting elif                            
                Statement 1.2                       |   |                                           
            else:                                   |   | # Nesting Else                                      
                Statement 1.3-----------------------|   |                                           
        elif( Condition 2):                             |       # elif Condition Start             
            Statement 2                                 |                                           
        else:                                           |       # else Condition Start              
            Statement 3 --------------------------------|                                           

'''

print(a)

# **************************************************************************************************************************

num = int(input("Enter Your Age:  "))
if (num >= 20):
    if(num >= 60):
        print("Please Register with the senior club !")
    elif(num >= 36):
        print("You belong to middle ager club !")
    else:
        print("Please Register with young adult club !")
elif(num > 12):
    print("You Belong to adult club !")
else:
    print("Sorry! You are too young to be a member !")
    
