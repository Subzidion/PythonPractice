def decorate(func):
    def newFunc():
        print("I can run some code before the function I decorate starts")
        func()
        print("I can also run coder after the function I decorate finishes")
    return newFunc

@decorate
def func():
    print("I am actually running the function now.")

func()
