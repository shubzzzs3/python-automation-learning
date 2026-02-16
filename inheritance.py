#inheritance
class employee:
    def __init__(self,name):
        self.name = name
        print("Employee",self.name,"is hired")

    def work(self):
        print("Employee is working")

class developer(employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language
        print("developer is woking on", self.language,"language")
    def work(self):
        print("developers is writting code")

dev1 = developer("shubham", "python")
dev1.work()
dev2 = developer("john", "Java")
#dev1.developer()
