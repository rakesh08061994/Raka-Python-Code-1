class DataJi:
    """Define class for dadaji"""
    village = "Manpur"
    cast = "Jangid"
    gotr = "Sehvaliya"

    def __init__(self, name, age, color, health, behave, job):
        self.name = name
        self.age = age
        self.color = color
        self.health = health
        self.behave = behave
        self.job = job

    def show_Behave(self, who_is):
        if who_is == "relative":
            print("Please have a seat !")
            print("son, take a good tea for us")
            print("Ha ha ha ha ......")
        elif who_is == "family":
            print("@#@#@#@# chhora.... o chhoori....")
            print("Give me some water, and make a tea for me")
            print("start the tv and set it on news channel")
            print("just look, where is my glasses")
            print("Ok... Do what you want to. bytheway who is listening me")

    def get_Info(self):
        print(f"My name is {self.name}, & I am {self.age} year old.")
        print(f"I am a retired {self.job}. & now i am sitting at home")
        print(f"I belive in god, not so much")
        print("Because i am supreme, I have a smart mind, i can't be wrong ever. ")

    def at_Morning(self):
        print("I awake early in the morning")
        print("I am not going getting fresh for last three days.")
        print("give me some warm water, and take some tea")
        print("start the tv")


class PapaJi(DataJi):
    """Define class for PapaJi, That also inherit all method and attributes of there parents class"""

    def __init__(self, name, age, color, health, behave, job):
        self.name = name
        self.age = age
        self.color = color
        self.health = health
        self.behave = behave
        self.job = job

    # def show_Behave(self,who_is):
    #     if who_is == "family":
    #         print("Hmm..   ok.. ok..")
    #         print("I am best, You are wrong")
    #         print("You dont know nothing, I am supreme")
    #         print("No one is smarter then me, I cant never be wrong")
    #         print("You are useless !")

    #     elif who_is == "relative":
    #         print("please have a seat.\n Dear son say to mom, to make a good tea")
    #         print("What is Truth, \n what is Supreme lord, what is regression")
    #         print("we are so small, infront of supreme god")
    #         print("we are nothing in front of god.")
    #         print("But my defination and my word is correct.\n and your word is just ok.. ok ")

    def get_Info(self):
        print(f"My name is {self.name}, & I am {self.age} year old.")
        print(f"I am a {self.job}")
        print(f"I belive in god, so much")
        print("I am a perfect person, I have a smart mind, i can't be wrong never. ")
        print("My father, and my children is ass hole, but I am the perfect.")


shiv_prashad = DataJi("Shiv", 70, "Red_Black", "Vary", "Rude", "Teacher")

# print(shiv_prashad.name)
# print(shiv_prashad.age)
# shiv_prashad.get_Info()
# shiv_prashad.show_Behave("family")
# shiv_prashad.at_Morning()

nawal = PapaJi("Nawal", 57, "Fair", "good", "Rude", "Teacher")

# nawal.get_Info()
# print(shiv_prashad.cast)
# print(nawal.cast)

# print(shiv_prashad.gotr)
# print(nawal.gotr)

# print(shiv_prashad.village)
# print(nawal.village)


nawal.show_Behave("family")
