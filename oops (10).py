class Train:
    company = "Indian Railway"
    Totalseat = 100

    def __init__(self,person):
        self.person = person


    def bookTicket(self):
        if self.person > self.Totalseat:
            print(" Sorry! we dont have much seats available right now")
            print(f"We have only {self.Totalseat} seats available and your seats request is for {self.person}")
        else:
            print(f"Your Ticket Book Request for {self.person} person are submited")


    def getStatus(self):
        result = self.Totalseat - self.person
        print(f" Available seats are {result}")


    def getFare(self):
        print(f" Total Fare is {self.person * 100} of {self.person} persons for one side")

    def cancleTicket(self,seat):
         self.Totalseat = self.Totalseat + seat
         print(f"You cancle {seat} seats ")
         print(f"Your fare will be {self.person * 100} after cancleation")

user = Train(15)

user.bookTicket()

user.getStatus()

user.getFare()

user.cancleTicket(2)

user.getStatus()
