income = int(input("How much money can you rent the propety for? "))
expenses = int(input("What is the total monthly expenses for the property? "))
cashFlow = income - expenses
CashonCash = int(cashFlow * 12) / int(input("What is your total investment? "))


def Finances():
    
    print("Monthly income: ", income)
    print("Monthly Expenses: ", expenses)   
    print(cashFlow)
    print("ROI", CashonCash * 100, "%")
    if CashonCash * 100 < 9:
        print("This one is a loser")
    else:
        print("Hurry up and buy this one")

Finances()