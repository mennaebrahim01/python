def emailvalidation(email):
    try:
        email = input ("enter email: ")
        if '@' in email and '.' in email:
                user, domain = email.split('@')
                if user and domain:
                    x,y = domain.split('.')
                    if x.strip() and y.strip():
                         print ("valid email")
                else: print("not valid ")

        else:
             print ("please enter a valid email")     
    except ValueError:
         print ("you entered too many '.'")
    except:
         print ("you entered an email not valid")
    finally:
         print ("end")

emailvalidation("")