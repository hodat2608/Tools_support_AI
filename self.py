class Person:
    def __init__(self, name, age , adress= None, gender=None):
        self.name = name
        self.age = age
        self.adress = adress
        self.gender = gender
    def staff(self):
        return f'tuổi của {self.name} là {self.age}' 
    
    def test(self):
        return f'địa chỉ ở  {self.adress} , {self.name} là {self.gender}' 

dat = Person('dat',23,"đà nẵng","nam")
print(dat.staff() ,"và" ,dat.test())



# def Person1():
#     dat = Person('dat',23,"đà Nẵng") 
#     return dat.adress

# print(Person1())