# __add__


class Xyz:

    def __init__(self,val):
        self.val = val

    def __add__(self,obj):
        return self.val + obj.val           # obj is for 2nd object value(val)


a = Xyz(10)         # object a value 10   (will use place of val)
b = Xyz(20)         # object b value 20   (will use place of obj(val))

print(a + b)       # 30 (call the function __add__)

# NOTE: we can change operator working machinism using operator overloading but call as print( a +b )

'''
 like:  def __add__(self,obj):
            return self.val * obj.val

                    or

        def __add__(self,obj):
            return self.val ** obj.val

                    or

        def __add__(self,obj):
            return self.val / obj.val

'''

