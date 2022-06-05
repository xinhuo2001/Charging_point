ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }


def ancestors(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for parent in parents:
            result += ancestors(genealogy, parent)
        return result
    return []
print(ancestors(ada_family, 'Judith Blunt-Lytton'))
print(ada_family)













# def add1(num_list):
#     for i in range(len(num_list)):
#         # num_list[i] = 1 + num_list[i]
#         # num_list = num_list + [1]
#         num_list += [1]
#     print(num_list)

# num_list = [1, 2, 3]
# print(num_list)
# add1(num_list)
# print(num_list)










# import json

# data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }

# data2 = json.dumps(data)
# print(data2)
# print(type(data2))

# data3 = json.loads(data2)
# print(data3)
# print(type(data3))

# with open(position, "r", encoding='utf-8') as f:

# class Employee:
#    '所有员工的基类'
#    empCount = 0
 
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#        print(f'count:{Employee.empCount}')
 
#    def displayEmployee(self):
#        print(f'name:{self.name} salary:{self.salary}')


# if __name__ == "__main__":
#     e1 = Employee("李四", 100)
#     e2 = Employee("王五", 120)

#     e1.displayEmployee()
#     e2.displayEmployee()
#     e2.displayCount()
