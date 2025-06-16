import json

class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender

    def show_person(self):
        if isinstance(self,Person):
            return "{} {} age-> {}, {}".format(self.fname,self.lname,self.age,self.gender)
        
person=Person("Aniket","Kumar",18,"male")
    
with open("demo.json","w") as f:
    json.dump(person.show_person(),f)