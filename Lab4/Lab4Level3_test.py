import unittest
from Lab4Level3 import Company
from Lab4Level3 import Worker
from Lab4Level3 import Manager
from Lab4Level3 import Director
from Lab4Level3 import WorkerTypes


class TestCompany(unittest.TestCase):

    def setUp(self):
        self.Company = Company("Roshen", 1000000)
        self.Worker = Worker("Andrii", 13, 500, WorkerTypes.WORKER, self.Company, 0)


    def test_calc_salary(self):
        self.assertEqual(self.Company.calc_salary(self.Worker), 2000 * 1.2)


if __name__ == '__main__':
    unittest.main()
