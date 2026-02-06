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
     
emails = [
     "men@gmail.com",
    "menna@example.co",
    "menna@gmail.com",
    "johndoe@yahoo.co.uk",   
    "user@domain",            
    "@gmail.com",             
    "ahmed@.com",             
    "sara123@outlook.com",
    "noatsign.com"
]
valid = list (map(emailvalidation, emails))
print (valid)

filtered = list(filter(emailvalidation, emails))
print (filtered)

#####problem 2
height =[" ", " ", " ", " ", " "]
for i in range (1,len(height)+1):
          height[len(height)- (len(height)+i)] = "*"
          print (height)
print("========================================")
print (height)
     
     