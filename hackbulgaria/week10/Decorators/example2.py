
def decorator_func(func):
    def wrapper_func(smth):
        return "Print: {0} end ?".format(func(smth))
    return wrapper_func

class DecoratorClass:

    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        return "Print FROM CLASS: {} end ?".format(self.func( *args,
                                                              **kwargs))
                                                              
#@decorator_func
@DecoratorClass
def say_smth(smt):
    return "22 WAT " + smt
    
print(say_smth("Cancur"))                                            
