
from budget import Budget

food_budget = Budget('Food', 400, 50)
print(food_budget)

clothing_budget = Budget('Clothes', 200, 100)
print(clothing_budget)

entertainment_budget = Budget('Entertainment', 100, 20)
print(entertainment_budget)

clothing_budget.addToBudget(30)

clothing_budget.addToBudget(30)

clothing_budget.withdrawFromBudget(20)

clothing_budget.withdrawFromBudget(150)

clothing_budget.transferToOther(20, food_budget)

food_budget.transferToOther(10, entertainment_budget)

food_budget.withdrawFromBudget(50)

food_budget.addToBudget(500)

entertainment_budget.transferToOther(20, clothing_budget)

entertainment_budget.withdrawFromBudget(70)

entertainment_budget.withdrawFromBudget(25)

entertainment_budget.addToBudget(35)
