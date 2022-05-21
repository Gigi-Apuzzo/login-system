import time
x = 0.5

u1 = []
p1 = []
adminu = []
adminp = []
username1 = []
password1 = []
user1dat = []
username2 = []
password2 = []
user2dat = []
username3 = []
password3 = []
user3dat = []
username4 = []
password4 = []
user4dat = []
username5 = []
password5 = []
user5dat = [] 

try:
  #admin login section
  u1 = input("Choose Admin Username: ")
  time.sleep(x)
  p1 = input("Choose Admin Password: ")
  adminu.append(u1)
  adminp.append(p1)
  
  while True:
    time.sleep(x)
    print("***************************")
    print("Welcome to the login system")
    print("***************************")
    time.sleep(x)
    
    lsq = input("Would you like to 'login', 'signup' or 'quit'?: ")
  
    if lsq == 'login':
      user = input("Enter Username: ")
      if user in username1:
        print("Username is Correct")
        passw = input("Enter Password: ")
        if passw in password1:
          print("Password is Correct")
          time.sleep(x)
          print("Login Success")
          time.sleep(x)
          dinp = input("Would you like to 'edit', 'read' or 'quit'?: ")
          if dinp == 'edit':
            user1dat.remove(t)
            new = input("Enter New Text: ")
            user1dat.append(new)
          elif dinp == 'read':
            print(user1dat)
            input("Press Enter when you are ready to exit.")
          elif dinp == 'quit':
            print("")
          else:
            print("Invalid Selection, please try again")
        else:
          print("Password is Incorrect")
          time.sleep(x)
      else:
        if user in username2:
          print("Username is Correct")
          passw = input("Enter Password: ")
          if passw in password2:
            print("Password is Correct")
            time.sleep(x)
            print("Login Success")
            time.sleep(x)
            dinp = input("Would you like to 'edit', 'read' or 'quit'?: ")
            if dinp == 'edit':
              user1dat.remove(t)
              new = input("Enter New Text: ")
              user1dat.append(new)
            elif dinp == 'read':
              print(user1dat)
              input("Press Enter when you are ready to exit.")
            elif dinp == 'quit':
              print("")
            else:
              print("Invalid Selection, please try again")
          else:
            print("Password is Incorrect")
            time.sleep(x)
        else:
          if user in username3:
            print("Username is Correct")
            passw = input("Enter Password: ")
            if passw in password3:
              print("Password is Correct")
              time.sleep(x)
              print("Login Success")
              time.sleep(x)
              dinp = input("Would you like to 'edit', 'read' or 'quit'?: ")
              if dinp == 'edit':
                user1dat.remove(t)
                new = input("Enter New Text: ")
                user1dat.append(new)
              elif dinp == 'read':
                print(user1dat)
                input("Press Enter when you are ready to exit.")
              elif dinp == 'quit':
                print("")
              else:
                print("Invalid Selection, please try again")
            else:
              print("Password is Incorrect")
              time.sleep(x)
          else:
            if user in username4:
              print("Username is Correct")
              passw = input("Enter Password: ")
              if passw in password4:
                print("Password is Correct")
                time.sleep(x)
                print("Login Success")
                time.sleep(x)
                dinp = input("Would you like to 'edit', 'read' or 'quit'?: ")
                if dinp == 'edit':
                  user1dat.remove(t)
                  new = input("Enter New Text: ")
                  user1dat.append(new)
                elif dinp == 'read':
                  print(user1dat)
                  input("Press Enter when you are ready to exit.")
                elif dinp == 'quit':
                  print("")
                else:
                  print("Invalid Selection, please try again")
              else:
                print("Password is Incorrect")
                time.sleep(x)
            else:
              if user in username5:
                print("Username is Correct")
                passw = input("Enter Password: ")
                if passw in password1:
                  print("Password is Correct")
                  time.sleep(x)
                  print("Login Success")
                  time.sleep(x)
                  dinp = input("Would you like to 'edit', 'read' or 'quit'?: ")
                  if dinp == 'edit':
                    user1dat.remove(t)
                    new = input("Enter New Text: ")
                    user1dat.append(new)
                  elif dinp == 'read':
                    print(user1dat)
                    input("Press Enter when you are ready to exit.")
                  elif dinp == 'quit':
                    print("")
                  else:
                    print("Invalid Selection, please try again")
                else:
                  print("Password is Incorrect")
                  time.sleep(x)
              else:
                if user in adminu:
                  print("Username is Correct")
                  passw = input("Enter Password: ")
                  if passw in adminp:
                    print("Password is Correct")
                    time.sleep(x)
                    print("Login Success")
                    time.sleep(x)
                    print(username1, password1)
                    time.sleep(0.1)
                    print(username2, password2)
                    time.sleep(0.1)
                    print(username3, password3)
                    time.sleep(0.1)
                    print(username4, password4)
                    time.sleep(0.1)
                    print(username5, password5)
                    time.sleep(x)
                    pc = input("Would you like to change your password? Enter 'y' or 'n': ")
                    if pc == 'y':
                      print("")
                    else:
                      print("Ok")
                      
                      time.sleep(x)
                  else:
                    print("Password is Incorrect")
                    time.sleep(x)
  
    elif lsq == 'signup':
      user = input("Choose username: ")
      if not username1:
        username1.append(user)
      elif not username2:
        username2.append(user)
      elif not username3:
        username3.append(user)
      elif not username4:
        username4.append(user)
      elif not username5:
        username5.append(user)
      else:
        print("Sorry, no signup space available.")
  
      passw = input("Choose Password: ")
      if not password1:
        password1.append(passw)
        t = input("Enter Text you would like to store: ")
        user1dat.append(t)
      elif not password2:
        password2.append(passw)
        t = input("Enter Text you would like to store: ")
        user2dat.append(t)
      elif not password3:
        password3.append(passw)
        t = input("Enter Text you would like to store: ")
        user3dat.append(t)
      elif not password4:
        password4.append(passw)
        t = input("Enter Text you would like to store: ")
        user4dat.append(t)
      elif not password5:
        password5.append(passw)
        t = input("Enter Text you would like to store: ")
        user5dat.append(t)
      else:
        print("Sorry, no signup space available.")
  
    elif lsq == 'quit':
      break
  
    else:
      print("Invalid Selection, please try again")
except:
  print("An error has occured, press enter to exit")
  input()