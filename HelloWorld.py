def login(name,password):
    pass
def register(name,password):
    pass

def begin():
    print("Welcome to Password Generator login")
    option = input("login or registor (login,reg): ")
    if(option!="login" and option!="reg"):
        begin()
begin()
