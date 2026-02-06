###2. Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string
def countvowels (string):
    x= 0
    vowels = ("aeiou")
    for char in string:
        if char in vowels:
            x+=1
    print (x) 

countvowels("meow")

#3. Write a program that prints the locations of "i" character in any string you added.
def geti (string):
    x = 0
    for i in string:
        if i == ('i'):
            print (x)
        x+=1
            

geti("miniyuio")

##Write a program that generate a multiplication table from 1 to the number passed
def small_multi_table(x):
    for i in range (1, x+1):
        for j in range (1, i+1):
            print (f"{i}*{j} = {i*j}")

small_multi_table(5)

def multitable(x):
    for i in range (1,13):
        print (f"{i}*{x}= {i*x}")

multitable(3)

## #Write a program that build a Mario pyramid l
def pyramid(x):
    y= '*'
    z= " "
    for i in range (1, x+1):
        print (f"{z*(x-i)} {i*y}")

pyramid(5)

###Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
#enter numbers
def getelement ():
    user = []
    for i in range (1, 6):
        x = input("insert {i} element: ")
        user.append(x)
    print (user)
    asc = sorted (user)
    des = sorted(user, reverse="true")
    print(asc)
    print(des)

getelement()

##check if given inputs in this dic
def varify (name, password):
    users = [{"name":"omar","pass":"123"},{"name":"ahmed","pass":"456"}]
    for i in users:
        if name == i["name"] and password == i["pass"]:
            print ("welcome")
            break
    else:
        print ("enter valid one")

varify ("ahmed", "456")