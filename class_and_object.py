#learning class and object
# learning class and object

class Tester:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is doing testing")

    def set_age(self, age):
        self.age = age
        print(self.name, "is", self.age, "years old")

t1 = Tester("Shubham")
t1.work()

t2 = Tester("john")
t2.work()

t3 = Tester("Shubham")
t3.set_age(4)
