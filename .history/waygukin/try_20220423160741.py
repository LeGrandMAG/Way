"""from decouple import config


username = config("ETA_ID")


print(username)"""



from async_generator import async_generator


class Student():
    def __init__(self, name):
        self.name = name
        self.age = async_generator