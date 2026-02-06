#Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
#enter numbers
numbers = []
for i in range (5):
    x = int(input("enter number:"))
    numbers.append(x)
print (numbers)
asc_numbers = sorted(numbers)
dsc_numbers = sorted (numbers, reverse="true")
print (asc_numbers)
print(dsc_numbers)
# in case you want it sorted in original list 
numbers.sorted()
numbers.reverse()


#Write a program that generate a multiplication table from 1 to the number passed.
x = int (input("enter a number: "))
y =[]

for i in range (1,x+1):
    z=[]
    for j in range (1,i+1):
        z.append(i*j)
    y.append(z)
print (y)

#Ask the user for his name then confirm that he has entered his name(not an empty
#string/integers). then proceed to ask him for his email and print all this data(Bonus) check if it is
a# valid email or not
name = input("enter a valid name: ")
if name.isdigit():
    print ("please enter a valid name")
elif name.isspace():
     print ("please enter a valid name")
else :
     email = input("enter your email: ")
     if email.isspace():
          print ("please enter a valid mail")
     if email.isdigit():
          print ("please enter a valid mail")
     else:
        if '@' in email and '.' in email:
            user, domain = email.split('@')
            if '.' in domain:
                domain.split('.') = x,y
                if x.y:
                    print ("valid")


######another solution by function
def emailvalidation(email):
     if '@' in email and '.' in email:
            user, domain = email.split('@')
            if user and domain and '.' in domain:
                x,y = domain.split('.',1)
                if x.strip() and y.strip():
                    return True
            return False
     else:
         return False
     

name = input("enter a valid name: ")
if name.isdigit():
    print ("please enter a valid name")
elif name.isspace():
     print ("please enter a valid name")
else :
     email = input("enter your email: ")
     if email.isspace():
          print ("please enter a valid mail")
     if email.isdigit():
          print ("please enter a valid mail")
     else:
          if emailvalidation(email):
               print ("email is valid")
          else:
               print ("not valid")

            
                   
                    

######problem 4
users = [{"name":"omar","pass":"123"},{"name":"ahmed","pass":"456"}]
name = input("name:")
password = input ("pasword:")
for i in users:
    if i["name"] == name and i["pass"]== password:
        print ("welcome")
        break
else:
    print ("enter coreect ")