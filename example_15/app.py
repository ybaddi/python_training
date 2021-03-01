def say_hello(name): return f"Hello {name}"

def say_nice(name): 
    return f"Hello {name}, nice to meet you"

def say_greet(func): 
    return func('youssef')


print(say_greet(say_hello))

print(say_greet(say_nice))

# ##############################

def parent(): 
    print("Print from The parent func")

    def first_child(): 
        print("Print from The first func")

    def secomd_child(): 
        print("Print from The second func")

    first_child()
    secomd_child()

parent()

# ############################## inner function

def parent_1(num): 

    def first_child(): 
        return "Print from The first func call"

    def secomd_child(): 
        return "Print from The second func call"

    func = first_child if (num == 1) else secomd_child
    return func
    # if num == 1: 
    #     return first_child
    # else: 
    #     return secomd_child

func_1 = parent_1(1)
print (func_1)

# #################################

def my_decorator(func): 
    def wrapper():
        print("befor function call")
        func()
        print("after function call")

    return wrapper

def say_hi():
    print("hi")

say_h = my_decorator(say_hi)
say_h()
print(say_h)
print("****************")
# ##############################
from datetime import datetime
def not_run_in_the_night(fun): 
    def wrapper():
        heur = datetime.now().hour
        print(heur)
        if not 7<= heur < 22:
            fun()
        else: pass
    
    return wrapper


say_h_2 = not_run_in_the_night(say_hi)
say_h_2()
print("****************")
# ##############################  

def my_decorator_2(func): 
    def wrapper():
        print("befor function call")
        func()
        print("after function call")

    return wrapper

@my_decorator_2
def say_hi_2():
    print("hi")

say_hi_2()