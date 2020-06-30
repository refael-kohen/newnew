class Employee(object):
    def __init__(self, name):
        self.name = name
        self.age = None

    def update_age(self, employees_dict):
        if self.age:
            return self.age
        for emp, age in employees_dict.items():
            if self.name == emp:
                self.age = age
                return int(age)

    def get_age(self):
        return self.age
