from programs.budget import Budget

def test_budg1():
    test = Budget('Test', 200, 50)
    assert str(test) == 'Budget: Test.\nBalance: 200'

def test_budg2():
    test = Budget('Test', 200, 50)
    assert test.addToBudget(20) == 220

def test_budg3():
    test = Budget('Test', 200, 50)
    assert test.withdrawFromBudget(40) == 40
    assert test.withdrawFromBudget(250) == 'Oooops! Seems like you do not have enough money to withdraw. Please add some to your budget'
    assert test.withdrawFromBudget(70) == 'Sorry, you are not allow to withdraw this amount of money. Your limit is 50'

def test_budg4():
    test = Budget('Test', 200, 50)
    test2 = Budget('Test2', 500, 150)
    assert test.transferToOther(25, test2) == 525
    assert test.transferToOther(75, test2) == 'Sorry, you are not allow to withdraw this amount of money. Your limit is 50'