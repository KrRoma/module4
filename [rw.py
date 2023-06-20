# name=input('введите имя')
# salary=int(input('введите зп'))
# print(f'у{name}зп в год составляет{salary*12}')
# employee={'name':'Роман',
#         'salary': 100000,
#         'old': 23}
# print(f'у {employee["name"]} зарплата в год сост {employee["salary"]*12}')
# print(f'у {employee.get("name")} зарплата в год сост {employee.get("salary")*12}')
# print(employee)
# employee_list=[
#     {
#         'name':'Роман',
#         'salary': 300_000
#     },
#     {
#         'name': 'Дэн',
#         'salary': 200_000
#     },
#     {
#         'name':'Егор',
#         'salary': 100_000
#     }
# ]
#print(employee_list[0])
#print(employee_list[-1])
# for employee in employee_list:
#     print(f'у{employee.get("name")}зп в год составляет'
#           f'{employee.get("salary")*12}')
#print('колво сотрудников= ',len(employee_list))
class Employee:
    def __init__(self,name,salary,on_vacation,is_good_employee):
        self.name=name
        self.salary=salary
        self.on_vacation=on_vacation
        self.is_good_employee=is_good_employee
    def get_info(self):
        return f'Имя: {self.name},зп: {self.salary}руб'

employee_list=[
    Employee('Даниил',200_000,False,False),
    Employee('Роман',300_000,True,True),
    Employee('Егор',100_000,False,True),
    Employee('Дарья',250_000,False,True),
    Employee('Настя',150_000,False,True)
]
for employee in employee_list:
    print(employee.get_info())

for employee in employee_list:
    if employee.is_good_employee == False:
        employee_list.remove(employee)
print('__________________')
for employee in employee_list:
    print(employee.get_info())
