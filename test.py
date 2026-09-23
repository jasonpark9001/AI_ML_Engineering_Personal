def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkles") 
        func(*args, **kwargs)
        
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you add fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream")

get_ice_cream("vanilla")    