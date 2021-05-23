class Indian_Railway:
    total_seats = 100


    file = "main.txt"
    with open(file,"w") as open_file:
        append_file = open_file.write(str(total_seats))
        print("completed")

        def __init__(self, name, seat):
            self.name = name
            self.seat = seat

        def book_Ticket(self):
            if self.seat < self.int(file):
                print(f"seat confirmed with {self.seat}")
                self.total_seats -= self.seat

            else:
                print("We have not much seats right now.")

        def get_Status(self):
            print(f"Remaining seats are : {self.total_seats}")

        def get_fare(self):
            print(f"Your total fare charge is {self.seat * 100}\- only")

        def cancle_Ticket(self, num):
            print(f"You have cancled {num} tickets")
            self.total_seats += num










a = Indian_Railway("Rajdhani", 15)
a.book_Ticket()
# # a.get_fare()
# a.get_Status()
# a.cancle_Ticket(5)
# a.get_Status()
