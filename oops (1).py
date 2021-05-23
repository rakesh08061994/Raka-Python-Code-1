class Employee:

    company = "Google"

    def __init__(self, name, salary, subunit):

        self.name = name

        self.salary = salary

        self.subunit = subunit

        # First it will print(as soon as object is created)
        print("Employee is created !")

    def getDetails(self):

        print(f"Employee Name is {self.name}")

        print(f" salary is {self.salary}")

        print(f"subunit is {self.subunit}")


rakesh = Employee("rakesh", 100, "Youtube")

harry = Employee("harry", 200, "Dropbox")

ajay = Employee("ajay", 300, "GMap")


# That shown DRY principle (Do Not Repeat Yourself)

rakesh.getDetails()

harry.getDetails()

ajay.getDetails()
