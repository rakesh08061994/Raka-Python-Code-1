# class Basic:

#     def __init__(self,a):
#         self.a = a
#         # self.b = b
#         # self.c = c
#         # self.d = d
#         # self.e = e
#         # self.f = f

#     def __add__(self,o):            # here 'o' is defined for second objects value
#         return self.a + self.a

# # obj1 = Basic(5, 10, 30, 10, 8, 3)
# # obj2 = Basic(15, 20, 40, 26, 84, 13)

# # print(obj1.a)
# # print(obj1.b)
# # print(obj1.c)
# # print(obj1.d)
# # print(obj1.e)
# # print(obj1.f)

# # print(obj1.a + obj1.b + obj1.c + obj1.d + obj1.e + obj1.f)  #66
# # print(obj2.a + obj2.b + obj2.c + obj2.d + obj2.e + obj2.f)  #198

# # print(obj1.a + obj2.f)  #18
# # print(obj1.a + obj2.b)  #25
# # print(obj1.a + obj2.c)  #45
# # print(obj1.c + obj2.d)  #56
# # print(obj1.b + obj2.e)  #94
# # print(obj1.d + obj2.f)  #23


# # print((obj1.a + obj1.b + obj1.c + obj1.d + obj1.e + obj1.f) + (obj2.a + obj2.b + obj2.c + obj2.d + obj2.e + obj2.f) ) #264


# obj1 = Basic(5)
# obj2 = Basic(40)

# # print(obj1.a + obj2.a) #45
# print(obj1 + obj2)      # without __add__ (throw an error : TypeError: unsupported operand type(s) for +: 'Basic' and 'Basic')
# print(obj1 + obj2)      # with __add__ # 45







# *****************************************************************************************************************


# class A:
#     def __init__(self, a):
#         self.a = a
#     def __lt__(self, other):
#         if(self.a<other.a):
#             return "ob1 is lessthan ob2"
#         else:
#             return "ob2 is less than ob1"
#     def __eq__(self, other):
#         if(self.a == other.a):
#             return "Both are equal"
#         else:
#             return "Not equal"
                  
# ob1 = A(2)
# ob2 = A(3)
# print(ob1 < ob2)
  
# ob3 = A(4)
# ob4 = A(4)
# print(ob1 == ob2)


# -----------------------------------------------------------------------------------------------------------------



# Python program to overload
# a comparison operators 
  
# class A:
#     def __init__(self, a):
#         self.a = a
#     def __gt__(self, other):
#         if(self.a>other.a):
#             return True
#         else:
#             return False
# ob1 = A(2)
# ob2 = A(3)
# if(ob1>ob2):
#     print("ob1 is greater than ob2")
# else:
#     print("ob2 is greater than ob1")




# -------------------------------------------------------------------------------------

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
     # adding two objects 
    def __add__(self, other):
        return self.a ** other.a, self.b ** other.b   # it should additing two object variables value(but we can operator overloading work)
  
  
Ob1 = complex(5, 2)
Ob2 = complex(5, 3)
Ob3 = Ob1 + Ob2
print(Ob3)







