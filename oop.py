class Person:
    def __init__(self,name,money,mood= None,healthrate= None):
        self.name = name
        self.money = money 
        self.mood = mood
        self.healthrate = healthrate 

    def sleep(self, hours ):
        if hours < 7:
            self.mood = "tired"
            print(f"{self.name}'s mood is {self.mood}")
        elif hours == 7 :
            self.mood = "happy"
            print(f"{self.name}'s mood is {self.mood}")
        else:
            self.mood = "lazy"
    
    def eat (self, meals):
        if meals == 3:
            self.healthrate = 100
            
        elif meals ==2:
            self.healthrate = 75
        elif meals == 1:
            self.healthrate = 50
        
        print(f"{self.name}'s healthrate is {self.healthrate}")


    def buy (self, items):
        self.money -= items*10
        print(f"{self.name}'s money is {self.money}")

    
class Employee(Person):
        def __init__(self, name, money, id, car, email, salary,distancetowork):
            super().__init__(name, money)
            self.id= id
            self.car = car
            self.email= email
            self.salary = salary
            self.distancetowork = distancetowork

        def work (self,hours):
            if hours == 8:
                self.mood = "happy"
            elif hours > 8:
                self.mood ="tired"
            else:
                self.mood = "lazy"
            print(f"{self.name}'s mood is {self.mood}")


        def drive (self, distance):
            self.car.run (60 , distance)

        def refuel(self, gasamount=100):
            self.car.fuelrate +=100
            if self.car.fuelrate >100:
                self.car.fuelrate = 100

        def sendmail (self, to, subject, body):
            print ("sending mail")
            print (f"to {to}")
            print (f"subject {subject}")
            print (f"body: {body}")


class Office:
    office_employees = 0
    def __init__(self,name):
        self.name = name
        self.employees = []

    def get_all_employees (self):
        return self.employees
    
    
    def get_employee(self, empid):
        for emp in self.employees:
            if emp.id == empid:
                return emp
            
    def hire (self, employee):
        self.employees.append(employee)
        Office.office_employees +=1

    def fire (self, empid):
        for emp in self.employees:
            if emp.id == empid:
                self.employees.remove (emp)    
                Office.office_employees -=1
                break

    @staticmethod
    def calculate_lateness (distance, velocity):
        return distance / velocity
    
    def check_lateness (self,empid, movehour):
        emp = self.get_employee(empid)
        if emp:
            time= Office.calculate_lateness (emp.distancetowork,emp.car.velocity )
            reachtime = movehour + time 
            if reachtime > 9:
                emp.salary -=10
                print(f"you are late, it's been deducted from your salary")
            else:
                print(f"welcome!")

    def deduct(self, empid, deduction):
        for emp in self.employees:
            if emp.id == empid:
                emp.salary -= deduction

    def reward (self, empid, reward):
        emp= self.get_employee(empid)
        if emp:
            emp.salary +=reward
    @classmethod
    def change_emps_num(cls, num):
        cls.office_employees = num
    
        

class Car:
    def __init__(self,name,fuelrate= 100,velocity=0):
        self.name = name
        self._fuelrate = fuelrate
        self._velocity = velocity 

    @property
    def fuelrate(self):
        return self._fuelrate
    
    @fuelrate.setter
    def fuelrate (self, value):
        if value > 100:
            self._fuelrate = 100
        elif value < 0:
            self._fuelrate = 0
        else:
            self._fuelrate = value

    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity (self,value):
        if value > 200:
            self._velocity = 200
        elif value < 0:
            self._velocity = 0
        else:
            self._velocity = value 

    def run(self, velocity, distance):
        self.velocity = velocity

        if self.fuelrate >=distance:
            self.fuelrate -=distance
            remain_distance = 0
        else:
            remain_distance = distance - self.fuelrate
            self.fuelrate = 0

        self.stop(remain_distance)

    def stop (self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Car stopped, {remain_distance} km remaining")
        else:
            print("You arrived at destination")

        



        