from symtable import Class

from Lab4.WorkersTypes import WorkerTypes


class Company:
    Name: str
    Budget: float

    Employees: list['Worker'] = []

    TRAINEE_YearBonusFactor = 1
    WORKER_YearBonusFactor = 1.2
    MANAGER_YearBonusFactor = 1.5
    DIRECTOR_YearBonusFactor = 2

    TRAINEE_Salary = 1000
    WORKER_Salary = 2000
    MANAGER_Salary = 3000
    DIRECTOR_Salary = 5000

    def __init__(self, Name: str, Budget: float):
        self.Name = Name
        self.Budget = Budget

    def calc_salary(self, employee: 'Worker'):
        salary: float = employee.Salary
        if employee.Exp / 12 >= 1 or employee.Exp == 0:
            exp_year: int = employee.Exp / 12  # 1, 2, 3, 4 yars working...

            if employee.Position == WorkerTypes.TRAINEE:
                for i in range(1, int(exp_year)):
                    salary = salary * self.TRAINEE_YearBonusFactor

            elif employee.Position == WorkerTypes.WORKER:
                for i in range(1, int(exp_year)):
                    salary = salary * self.WORKER_YearBonusFactor

            elif employee.Position == WorkerTypes.MANAGER:
                for i in range(1, int(exp_year)):
                    salary = salary * self.MANAGER_YearBonusFactor

            elif employee.Position == WorkerTypes.DIRECTOR:
                for i in range(1, int(exp_year)):
                    salary = salary * self.DIRECTOR_YearBonusFactor
        return salary

    def calc_employees_expenses(self):
        all_expenses: float
        for i in self.Employees:
            all_expenses += i.Salary
        return all_expenses

    def print_employees(self):
        for employee in self.Employees:
            print(f"{employee.Position} {employee.Name} працює вже {employee.Exp} місяці з зарплатою {employee.Salary}")

    def add(self, employee: 'Worker'):
        if self.Employees.count(employee) == 0:
            self.Employees.append(employee)
            if employee.Position == WorkerTypes.WORKER:
                self.Employees[-1].Salary = self.WORKER_Salary
                self.Employees[-1].Salary = self.calc_salary(self.Employees[-1])

            elif employee.Position == WorkerTypes.TRAINEE:
                self.Employees[-1].Salary = self.TRAINEE_Salary
                self.Employees[-1].Salary = self.calc_salary(self.Employees[-1])

            elif employee.Position == WorkerTypes.MANAGER:
                self.Employees[-1].Salary = self.MANAGER_Salary
                self.Employees[-1].Salary = self.calc_salary(self.Employees[-1])

            elif employee.Position == WorkerTypes.DIRECTOR:
                self.Employees[-1].Salary = self.DIRECTOR_Salary
                self.Employees[-1].Salary = self.calc_salary(self.Employees[-1])




class Worker:
    Name: str
    Exp: float
    Salary: float
    Position: str
    Company: Company

    Wallet: float

    YEAR_BONUS_FACTOR = 1.2

    def __init__(self, name: str, exp: float, salary: float, position: str, company: Company, wallet: float):
        self.Name = name
        self.Exp = exp
        self.Salary = salary
        self.Position = position
        self.Company = company
        self.Wallet = wallet

    def calc_salary(self):
        if self.Exp % 12 == 0:
            exp_year = self.Exp / 12  # 1, 2, 3, 4 yars working...
            self.Exp = self.Salary * self.YEAR_BONUS_FACTOR * exp_year

    def obey(self):
        print(f"{self.Name}: Sorry Master!")
        pass


class Manager(Worker):
    def control_slaves(self):
        print(f"{self.Name}: Slaves are enslaved")
        pass


class Director(Manager):

    def launder_money(self):  # Відмивати гроші
        self.Wallet += self.Company.Budget * 0.1  # Забираємо в компанії 10% грошей в карман
        self.Company.Budget = self.Company.Budget * 0.9  # Забираємо в компанії 10% грошей в карман


Roshen = Company("Roshen", 1000000)

Worker1 = Worker("Олексій", 13, 500, WorkerTypes.WORKER, Roshen, 0)
Manager1 = Manager("Олена", 20, 500, WorkerTypes.MANAGER, Roshen, 0)
Director1 = Director("Андрій", 60, 500, WorkerTypes.DIRECTOR, Roshen, 0)

Roshen.add(Worker1)
Roshen.add(Manager1)
Roshen.add(Director1)
Roshen.print_employees()