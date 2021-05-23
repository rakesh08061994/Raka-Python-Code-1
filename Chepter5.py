# # **************************************Dictionary**************************************
# # **************************************************************************************

# # Create Simple Empty Dictionary

Dict = {}
print("Print Empty Dictionary \n", Dict)

# # ------------------------------------------------------------

# # Adding element one at aa time in Dictionary

# Dict[0] = 'Value'
# Dict[1] = 'Added'
# Dict[2] = 'in'
# Dict['Book'] = 'Dictionary'
# print("Dictionary Before Adding 3 Elements\n", Dict)

# # --------------------------------------------------------------

# # Adding Set of values in single key

# Dict[4] = 1,2,3,4,5
# print("Dictionary Before Adding Multiple Values In Single Key \n", Dict)

# # ---------------------------------------------------------------

# # Update Old Values to New Value in Dictionary

# Dict[2] = 'Updated'
# print("Before update New Value on 2nd indexing \n", Dict)

# # ------------------------------------------------------------------

# # Added Nested value to a Dictionary

# Dict[5] = {'Number':9887211207, 'Place':'Jaipur', 'Nationality':'Indian'}       #Add Nested Value in Dict
# print("Added Nasted Value In 5th Indexing of Dictionary \n", Dict)

# # -----------------------------------------------------------------------------------

# print("\n\n\n\n At The End Of Practises\n Dictionary Changed From \n Empty To Big Dictionary \n", Dict)
# print(type(Dict))

# # -------------------------------------------------------------------------------------

# # Access The Elements From Dictionary Using Key with Python Buil-In Function

# print(Dict)     # This is Dictionary With Key & Values

# print(Dict[1])    # Access Dictionary Using ['Key_Name'] not Indexing
# print(Dict['Book'])     # Key may be Integer or str type

# # ---------------------------------------------------------------------------------------

# # Use get() Method to access Dictionary
# print(Dict.get(1))      # Key Name is 1
# print(Dict.get('Book')) # Key Name is 'Book'

# # ------------------------------------------------------------------------------
# # Printing Dictionary, Nested Dictionary and Then Check Data Type of Ditionary,
# #  Nested dictionary & her Key's Value

# print(Dict)
# print(type(Dict))   # Printing Dictionary Data Type
# print(Dict['Book']) # Printing Value of Dictionary Key's 
# print(type(Dict['Book']))   #Printing Values Data Type of Dictiionary Keys
# print(Dict[5])
# print(type(Dict[5]))                #Printing Nested Dictionary
# print(Dict[5]['Number'])            #Printing Nested Dictionary key's value
# print(type(Dict[5]['Number']))      #Printing Nested Dictionary key's value Data Type
# # -----------------------------------------------------------------------------
# print("\n\nDelete the (Key & value in Dictionary), AND (Nested Dictionary and there key & Value) from del() Method \n\n")
# print("\n\nPrinting Dictionary Before Deleting\n\n")
# print(Dict)         
# print("\n\nDeleting Value of Keys 1\n\n")
# del(Dict[1])       
# print(Dict)         # See Changes
# print(" \n\nDeleted Nested Dictionary Keys 5 Values\n\n")
# del(Dict[5]['Number'])         
# print(Dict)
# print(" \n\nDeleting Whole Nested Dictionary\n\n")
# del(Dict[5])
# print("\n\nNow This is Remaining Dictionary")               
# print(Dict)

































# # **************************************Thank You*********************************************************

