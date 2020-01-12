class bankAccount:
    def __init__(self, portfolio_info):
        f=open(portfolio_info, "rw+")
        self.account_balance = float(f.readline().rstrip())
        self.portfolio_balance = float(f.readline().rstrip())
        self.goals = []
        while(f.readline()):
            id = int(f.readline().strip())
            name = f.readline().strip()
            target_amount= float(f.readline().strip())
            current_amount= float(f.readline().strip())
            contribution=float(f.readline().strip())
            inv_percentage= float(f.readline().strip())
            g = goal(id, name, target_amount,contribution,inv_percentage, current_amount)
            self.goals.append(g)
        f.close()

    def invest(self, amount):
        self.portfolio_balance = self.portfolio_balance + amount

    def update_Goals(self):
        investment = 0
        for g in self.goals:
            print g.getProgress()
            if g.getProgress() < 1:
                investment = investment + g.contrib()
                self.account_balance = self.account_balance - g.getContribution()
            else:
                print "Target amount for " + g.name + " has been achieved"
        self.invest(investment)
        print "Investment Made: ", investment, "\nCurrent Portfolio Balance: ", self.portfolio_balance
        print "Current Account  Balance: ", self.account_balance

    def save(self,filename):
        f= open(filename,"w")
        f.write(str(self.account_balance) + "\n")
        f.write(str(self.portfolio_balance)+ "\n")
        for g in self.goals:
            f.write(" "+ "\n")
            f.write(str(g.id)+ "\n")
            f.write(g.name + "\n")
            f.write(str(g.target_amount)+ "\n")
            f.write(str(g.current_amount)+ "\n")
            f.write(str(g.contribution)+ "\n")
            f.write(str(g.inv_percentage)+ "\n")
        f.close()

class goal:
    def __init__(self, id, name, target_amount, contribution, inv_percentage, current):
        self.inv_percentage = inv_percentage
        self.id = id
        self.name = name
        self.target_amount = target_amount
        self.contribution = contribution
        self.current_amount = current

    def contrib(self):
        self.current_amount = self.current_amount + (1-self.inv_percentage)*self.contribution
        return self.inv_percentage*self.contribution

    def getContribution(self):
        return self.contribution

    def getTarget(self):
        return self.target_amount

    def setTarget(self, new_target):
        self.target_amount = new_target

    def getName(self):
        return self.name

    def setName(self, new_Name):
        self.name = new_Name

    def getId(self):
        return self.id

    def get_currentamount(self):
        return self.current_amount

    def getProgress(self):
        return self.current_amount / self.target_amount

    def get_invPercentage(self):
        return self.inv_percentage

    def set_invPercentage(self, inv_percentage):
        self.inv_percentage= inv_percentage 

#-----------------------------------------------------------#

b = bankAccount("account_balance.txt")
b.update_Goals()
b.save("account_balance.txt")












