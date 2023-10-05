"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return f"{self.name} {self.describe_employee()}  Their total pay is {self.get_pay()}."

    def describe_employee(self):
        pass


class HourlyWorker(Employee):
    def __init__(self, name, wage, numHours, bonus, numContracts, commissionRate):
        super().__init__(name)
        self.wage = wage
        self.numHours = numHours
        self.bonus = bonus
        self.numContracts = numContracts
        self.commissionRate = commissionRate

    def get_pay(self):
        pay = self.wage * self.numHours

        if self.bonus is not None:
            pay += self.bonus
        elif self.commissionRate is not None:
            pay += self.numContracts * self.commissionRate

        return pay

    def describe_employee(self):
        desc = f"works on a contract of {self.numHours} hours at {self.wage}/hour."

        if self.bonus is not None:
            desc += f" and receives a bonus commission of {self.bonus}."
        elif self.commissionRate is not None:
            desc += f" and receives a commission for {self.numContracts} contract(s) at {self.commissionRate}/contract."

        return desc


class SalaryWorker(Employee):
    def __init__(self, name, salary, bonus, numContracts, commissionRate):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus
        self.numContracts = numContracts
        self.commissionRate = commissionRate

    def get_pay(self):
        pay = self.salary

        if self.bonus is not None:
            pay += self.bonus
        elif self.commissionRate is not None:
            pay += self.numContracts * self.commissionRate

        return pay

    def describe_employee(self):
        desc = f"works on a monthly salary of {self.salary}."

        if self.bonus is not None:
            desc += f" and receives a bonus commission of {self.bonus}."
        elif self.commissionRate is not None:
            desc += f" and receives a commission for {self.numContracts} contract(s) at {self.commissionRate}/contract."

        return desc


# class SalaryWorkers(Employee):


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryWorker('Billie', 4000, None, None, None)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyWorker('Charlie', 25, 100, None, None, None)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryWorker('Renee', 3000, None, 4, 200)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyWorker('Jan', 25, 150, None, 3, 220)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryWorker('Robbie', 2000, 1500, None, None)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyWorker('Ariel', 30, 120, 600, None, None)
