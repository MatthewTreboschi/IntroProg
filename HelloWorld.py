def login(name,password):
    pass
def register(name,password):
    pass

def begin():
    print("Welcome to Password Generator login")
    option = input("login or registor (login,reg): ")
    if(option!="login" and option!="reg"):
        option = begin()
    return option
opt = begin()
if(opt=="login"):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    login(name,password)
