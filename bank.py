class Bank:
    def __init__(self,name,branch,type):
        self.name=name
        self.branch=branch
        self.type=type
    def display_detail(self):
        print("name:",self.name)
        print("barnch:",self.branch)
        print("type:",self.type)

account1 = Bank("icici","kozhikode","private")
account2=Bank("idbi","kozhikode","private")
account1.display_detail()
    
    
