# *args and **kwargs

def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)

args = [1,2,3]
kwargs = {"arg2":3, "arg1":4, "arg3":5}

func1(*args)
print(args)
print(*args)


func2(**kwargs)
print(kwargs)