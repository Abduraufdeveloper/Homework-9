class Person :
    def __init__(self,name,loves,hates,a):
        self.name = name
        self.loves = loves
        self.hates = hates
        self.a = a
    def name(self):
        self.name = "Samuel"
    def loves(self):
        self.loves = "Ice cream"

    def hates(self):
        self.hates = "broccoly"

    def taste(self):
        self.a = input("Ovqat nomini kiriting  menu : Ice cream ,    broccoly , ")

if Person.taste == "Ice ceam":
    print(Person.name ,"loves" , Person.loves, "it !")
elif Person.taste == "broccoly":
    print(Person.name,"Hates",Person.hates ,"it!" )

