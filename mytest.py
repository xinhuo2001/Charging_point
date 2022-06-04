class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
       print(f'count:{Employee.empCount}')
 
   def displayEmployee(self):
       print(f'name:{self.name} salary:{self.salary}')


# if __name__ == "__main__":
#     e1 = Employee("李四", 100)
#     e2 = Employee("王五", 120)

#     e1.displayEmployee()
#     e2.displayEmployee()
#     e2.displayCount()
