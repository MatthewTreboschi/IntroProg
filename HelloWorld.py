def login(name,password):
    print ("logged in")
def register(name,password):
    print ("registered")

def begin():
    print("Welcome to Password Generator login")
    option = input("login or registor (login,reg): ")
    if(option!="login" and option!="reg"):
        option = begin()
    return option
opt = begin()
def GetInfo():
    if(opt=="login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else: 
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)
