from oop import Person, Office, Employee, Car

car1 = Car("fiat128",100,80)
car2 = Car("cubra")

emp1 = Employee ("samy",1500,5,car1, "samy011@gmail.com", 5000,10)
emp2 = Employee ("ahmed", 2500, 10, car2, "ahmed@gmail.com", 4500, 50)

emp1.sleep(5)
emp2.eat(2)
emp1.buy(5)
emp2.sendmail(emp1.name,"greeting","Nice to meet you ")

office1 = Office("iti PortSaid")

office1.hire(emp1)
office1.hire(emp2)

office1.fire(10)

print(Office.office_employees)

emp1.work(10)
emp2.drive(1)

##deduction for empid = 5 and print its salary 
office1.deduct(5, 400)
x = office1.get_employee(5)
print (x.salary)


##hire emp2 again and reward it with 500 then print its new salary 
office1.hire(emp2)
office1.reward(10,500)
y = office1.get_employee(10)
print(y.salary)


office1.check_lateness(5, 9)



