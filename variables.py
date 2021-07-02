global_var = "I am global variable"

def func():
    local_var = "I am local variable"
    global global_var
    
    print(global_var)
    print(local_var)

func()

try:
    print(local_var)
except Exception:
    print("local_var not available here!!")
