from unittest import TestCase
import os

from my_package.store.employee import Employee

class TestEmployee(TestCase):

    # The steps:

    # Run test_update_age:

    # t = TestEmployee()
    # TestEmployee.setUpClass()
    # t.setUp()
    # t.test_update_age()

    #Don't call to tearDownClass, it is object method,
    # we call it only after end of the run of all instances
    # of TestEmployee

    ######################
    # Run test_get_age:

    # Don't call again to setUpClass,
    # but the cls.employees_dict is object attribute,
    # so you can use it also in the new instance of TestEmployee

    # t = TestEmployee()
    # t.setUp()
    # t.test_get_age()
    # TestEmployee.tearDownClass() #


    @classmethod
    def setUpClass(cls):
        # We are not going to change the values of the file, so we can read it one time for all tests
        cls.employees_dict = {}
        file_name = os.path.join(os.path.join(os.path.dirname(__file__), 'data', 'employees.csv'))
        with open(file_name) as employees_fh:
            for line in employees_fh.readlines():
                emp, age = line.split(',')
                cls.employees_dict[emp] = age

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # We change the employee age in an update_age call, so we want to redefine it for each method.
        self.emp = Employee('Moshe')

    def test_update_age(self):
        self.assertEqual(self.emp.update_age(self.employees_dict), 50)

    def test_get_age(self):
        self.assertEqual(self.emp.get_age(), None)
