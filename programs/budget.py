from datetime import datetime

# creates Budget class

class Budget():
    def __init__(self, type_, balance, max_allowance_withdraw):
        self.type_ = type_
        self.balance = balance
        self.max_allowance_withdraw = max_allowance_withdraw
        # create a new file when a Budget object is instantiated
        self.file_ = self.createInfoFile()

    def __repr__(self):
        return f'Budget: {self.type_}.\nBalance: {self.balance}'

    # add money to balance 
    def addToBudget(self, amount, description ='Added: '):
        self.balance += amount
        self.modifyInfoFile(description, amount)
        return self.balance

    # withdraw from balance
    def withdrawFromBudget(self, amount, description = 'Withdrawn: '):
        self.balance -= amount
        self.modifyInfoFile(description, amount)
        return amount 

    # transfer money to another budget
    def transferToOther(self, amount, budget_to_feed):
        return budget_to_feed.addToBudget(self.withdrawFromBudget(amount))
       
    # Create a file in which I can store the type of budget and its balance
    def createInfoFile(self):
        file1 = open(f'{self.type_}_budget.txt', 'w')
        file1.write(f'Budget type: {self.type_}\n')
        file1.write(f'Balance: {self.balance}')
        file1.close()

    # modify file when balance changes
    def modifyInfoFile(self, description, amount):      #description refers to the operation applied to the balance
        file1 = open(f'{self.type_}_budget.txt', 'r')
        lines = file1.readlines()
        file1.close()
        file1 = open(f'{self.type_}_budget.txt', 'w')
        for line in lines:
            file1.write(line)
        
        now = datetime.now() # current date and time
        date = now.strftime("%m/%d/%Y, %H:%M:%S")
        file1.write(f'\n\nDate: {date};\n{description} {amount};\nNew balance: {self.balance}')
        file1.close()