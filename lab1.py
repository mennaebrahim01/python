#2. Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string
x = input("enter a word: ")
y= 0 
vowels = ("aeiou")
for char in x :
    if char in ("aieou"):
        y +=1
        #زودت else عشان اخرج من اللوب ويجيب توتال X
    else:
        pass
print (y)

#3. Write a program that prints the locations of "i" character in any string you added.
text = input("enter a string:")
i = 0 
for char in text:
    if char == ('i'):
        print (i)
    i+=1

# Write a program that generate a multiplication table from 1 to the number passed
x = input(("enter a number= "))
x = int (x)
for i in range (1,x+1):
    for j in range (1,x+1):
        print (f"{i}*{j}= {i*j}")

#لو عاوز يقف عند انه يضرب الرقم في نفسه       
x = input(("enter a number= "))
x = int (x)
for i in range (1,x+1):
    for j in range (1,i+1):
        print (f"{i}*{j}= {i*j}")

 #Write a program that build a Mario pyramid l
x = ("*")
y=1
z= int(input("enter row number: "))
for i in range (1,z+1):
    print (" " * (z-i) + x*y )
    y+=1 
