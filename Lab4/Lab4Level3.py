class WorkerTypes:
    TRAINEE = "Стажер"
    WORKER = "Працівник"
    MANAGER = "Менеджер"
    DIRECTOR = "Директор"

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
        years: int = employee.Exp // 12
        # Якщо працівник працює менш як рік, то в нього звичайна зарплата без надбавок
        if years == 0:
            if employee.Position == WorkerTypes.TRAINEE:
                salary = self.TRAINEE_Salary
            elif employee.Position == WorkerTypes.WORKER:
                salary = self.WORKER_Salary
            elif employee.Position == WorkerTypes.MANAGER:
                salary = self.MANAGER_Salary
            elif employee.Position == WorkerTypes.DIRECTOR:
                salary = self.DIRECTOR_Salary
        elif years > 0:
            if employee.Position == WorkerTypes.TRAINEE:
                salary = self.TRAINEE_Salary * self.TRAINEE_YearBonusFactor * years
            elif employee.Position == WorkerTypes.WORKER:
                salary = self.WORKER_Salary * self.WORKER_YearBonusFactor * years
            elif employee.Position == WorkerTypes.MANAGER:
                salary = self.MANAGER_Salary * self.MANAGER_YearBonusFactor * years
            elif employee.Position == WorkerTypes.DIRECTOR:
                salary = self.DIRECTOR_Salary * self.DIRECTOR_YearBonusFactor * years

        return salary

    def calc_employees_expenses(self):
        all_expenses: float = 0
        if len(self.Employees) > 0:
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



    def __init__(self, name: str, exp: float, salary: float, position: str, company: Company, wallet: float):
        self.Name = name
        self.Exp = exp
        self.Salary = salary
        self.Position = position
        self.Company = company
        self.Wallet = wallet


    def obey(self):
        print(f"{self.Name}: Sorry Master!")
        pass


class Manager(Worker):
    def control_slaves(self):
        print(f"{self.Name}: Slaves are enslaved")
        pass


class Director(Manager):

    StealFactor: float = 0.1
    def steal_money(self):  # Відмивати гроші
        print("\nВиконується крадіжка грошей...")
        self.Wallet += self.Company.Budget * self.StealFactor  # Забираємо в компанії 10% грошей в карман
        self.Company.Budget = self.Company.Budget * (1 - self.StealFactor)  # Забираємо в компанії 10% грошей в карман
        print(f"В компанії забрали {self.StealFactor * 100}% бюджету в кишеню директору")
        print(f"В кишені у директора {self.Wallet} грн")

Roshen = Company("Roshen", 1000000)

Worker1 = Worker("Олексій", 13, 500, WorkerTypes.WORKER, Roshen, 0)
Manager1 = Manager("Олена", 20, 500, WorkerTypes.MANAGER, Roshen, 0)
Director1 = Director("Андрій", 60, 500, WorkerTypes.DIRECTOR, Roshen, 0)

Roshen.add(Worker1)
Roshen.add(Manager1)
Roshen.add(Director1)
Roshen.print_employees()


print(f"\nЗагальні витрати за місяць на зарплати робітників складають: {Roshen.calc_employees_expenses()} грн")

Director1.steal_money()