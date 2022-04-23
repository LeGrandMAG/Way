"""from decouple import config


username = config("ETA_ID")


print(username)"""



class Student():
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id 

        return self.name