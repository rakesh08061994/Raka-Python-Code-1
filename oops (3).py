class C2dVector:
    name = "C2DVector"

    def __init__(self, X_axes, Y_axes):
        self.X_axes = X_axes
        self.Y_axes = Y_axes

    def __str__(self):
        return (f"{self.X_axes}i + {self.Y_axes}j ")


class C3dVector(C2dVector):
    name = "C3dVector"

    def __init__(self, X_axes, Y_axes, Z_axes):
        super().__init__(X_axes, Y_axes)
        self.Z_axes = Z_axes

    def __str__(self):
        return (f"{self.X_axes}i + {self.Y_axes}j + {self.Z_axes}k")


a = C2dVector(5, 10)
b = C3dVector(10, 30, 50)

print(a)  # <__main__.C2dVector object at 0x0000020D8F09CFD0> (if __str__ is not defned)
print(b)  # <__main__.C3dVector object at 0x0000020D8F09CC70> (if __str__ is not defned)

# print(len(a))
# print(len(b))

