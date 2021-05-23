# (a+bi) + (c+di) = (a+c) + (b+d)i  ------------> Addition of Complex Number
# multiply: # (a+bi)(c+di) = (ac−bd) + (ad+bc)i
''' Each part of the first complex number gets multiplied by
    each part of the second complex number '''


class Complex:
    
    def __init__(self, r, i):
        self.real_part = r
        self.img_part = i

    def __add__(self, num2):
        print("Lets add")
        if self.img_part < 0:
            return Complex(self.real_part + num2.real_part, -self.img_part - num2.img_part)
        else:
            return Complex(self.real_part + num2.real_part, self.img_part + num2.img_part)


    def __mul__(self,num2):
        mulReal = self.real_part * num2.real_part - self.img_part * num2.img_part
        mulImg = self.real_part * num2.img_part + self.img_part * num2.real_part
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.img_part < 0:
            return f"{self.real_part} - {-self.img_part}i"
        else:
            return f"{self.real_part} + {self.img_part}i"

val1 = Complex(3, 2)
val2 = Complex(1, -7)

print(val1 + val2)
print(val1 * val2)


# print(val)

