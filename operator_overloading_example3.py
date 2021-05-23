# __mul__


class Xyz:

    def __init__(self,val):
        self.val = val

    def __mul__(self,obj):
        return self.val * obj.val           # obj is for 2nd object value(val)
        # return self.val - obj.val
        # return self.val + obj.val
        # return self.val ** obj.val
        # return self.val / obj.val
        # return self.val // obj.val        (all above possibility is possible because we changed internal operator working on a - b)

a = Xyz(10)         # object a value 10   (will use place of val)
b = Xyz(20)         # object b value 20   (will use place of obj(val))

print(a * b)       # 200 (call the function __add__)