
def accepts(*_type):
    def _accepts(func):
        def wrapper(*args):
            for i in range(len(args)):
                if not isinstance(args[i], _type):
                    if len(_type) == 1:
                        return "TypeError: Argument {0} of {1} is not {2}!".format(i, func.__name__, _type[0].__name__)
                    else:
                        all_types = [t.__name__ for t in _type]
                        return "TypeError: Argument {0} of {1} is not any of the types: {2}!".format(i, func.__name__, all_types)
            return func(*args)
        return wrapper
    return _accepts
    
@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

print(say_hello(4))

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

print(say_hello("Hacker"))

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

print(deposit("RadoRado", 10))

