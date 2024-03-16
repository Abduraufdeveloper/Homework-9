class Composer:
    def __init__(self,dob,name,country):
        self.dob = dob
        self.name = name
        self.country = country
    def ism(self):
        self.name = input("Ismingizni kirting :")
    def dob(self):
        self.dob = input("Tug`ilgan yilingizni kirting :")
    def strana(self):
        self.country = input("Yoshayodgan country kiriting :")
while True:
    print(Composer.ism)
    print(Composer.dob)
    print(Composer.strana)
    if Composer == True:
        a = 1
        a += 1
        print(a)
    break

