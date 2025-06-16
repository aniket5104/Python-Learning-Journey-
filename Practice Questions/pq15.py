class Student:
    def __init__(self):
        self.name=input("ENter The name of the student")
        self.m1, self.m2, self.m3=map(int,input("Enter the mark in the 3 subjects").split())
    def show_average(self,m1,m2,m3):
        print("The average marks of",self.name,"is",(m1+m2+m3)/3)


s1=Student()
s1.show_average(s1.m1,s1.m2,s1.m3)
