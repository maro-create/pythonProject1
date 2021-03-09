class Employee:
  def get_net_salary(self):
    tax = self.salary * 0.15 - self.children * 1500
    netSalary = self.salary - tax
    return f"Výše čisté mzdy je {netSalary} Kč."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.salary = 100000
    self.children = 2



class Employee:
  def get_tax(self):
    tax = self.salary * 0.15 - self.children * 1500
    return (tax)
  def get_net_salary(self):
    net_salary = self.salary - self.get_tax()
    return (f"Výše čisté mzdy je {net_salary} Kč.")
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.salary = 100000
    self.children = 2









