
from budget import Budget

# List that will store the budgets created
listBudgets = []

# append an initial budget if you want to try the transfer method with the first budget you create
listBudgets.append(Budget('temp',400,50))

condition = 'y'

while condition == 'y':
    print('Type in the name of your new budget(i.e.: food, entertainment,... ):')
    budgetType = input()
    print('What\'s your initial balance?')
    budgetBalance = int(input())
    print('Set your maximum withdraw allowance:')
    maxWithdraw = int(input())

    newBudg = Budget(budgetType,budgetBalance,maxWithdraw)
    listBudgets.append(newBudg)

    print('Do you want to add more money to your balance? y/n')
    answer=input()
    if answer == 'y':
        print('How much do you want do add?')
        amount=int(input())
        newBudg.addToBudget(amount)

    print('Do you want to withdraw money? y/n')
    answer=input()
    if answer == 'y':
        print(f'How much do you want do withdraw? \nMax allowance: {newBudg.max_allowance_withdraw}\nCurrent Balance: {newBudg.balance}')
        amount=int(input())
        if amount > newBudg.max_allowance_withdraw or newBudg.balance < amount:
            print('Not allowed')
        else:
            newBudg.withdrawFromBudget(amount)

    print('Would you like to transfer money to another budget? y/n')
    answer=input()
    if answer == 'y':
        print('Type in the budget to feed:')
        budgetToFeed = input()
        # check if the file and therefore the budget to feed exist. If yes transfer money
        found = False
        for budget in listBudgets:
            if budget.type_ == budgetToFeed:
                print(f'How much do you want to transfer? \nMax allowance: {newBudg.max_allowance_withdraw}\nCurrent Balance: {newBudg.balance}')
                amount=int(input())
                if amount > budget.max_allowance_withdraw or budget.balance < amount:
                    print('Not allowed')
                else:
                    newBudg.transferToOther(amount, budget)
                found = True
        if found:
            found = False
        else:
            print('Sorry, budget not found. Money cannot be transferred.')

    print('Would you like to create another budget? y/n')
    condition = input()
    