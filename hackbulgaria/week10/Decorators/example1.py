    
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return"<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper
        
@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "Someone named {}".format(name)    
#print(get_text("John"))

def tag_name(tag_name):
    def p_decorate(func):
       def func_wrapper(name):
           return "<{1}>{0}</{1}>".format(func(name), tag_name)
       return func_wrapper
    return p_decorate

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"
        
    @tag_name("div")
    @tag_name("p")
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print(my_person.get_fullname())
