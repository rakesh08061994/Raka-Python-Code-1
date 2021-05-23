class Programmer:
    company = "Microsoft"

    def __init__(self,name,unit,work):
        print("__init__ execute, ASAP each and every xclass object instanciation")
        self.name = name
        self.unit = unit
        self.work = work

    def get_Info(self):
        print(f"My name is {self.name}")
        print(f"My branch unit is {self.unit}")
        print(f"I am working on {self.work}")
        print(f"I am a employee of {self.company}")

programmer1 = Programmer("ram", "assistent", "Bug_Resolving" )
programmer1.get_Info()

programmer2 = Programmer("david", "Head", "testing")
programmer2.get_Info()
