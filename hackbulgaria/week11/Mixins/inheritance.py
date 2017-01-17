"""
1. Inheritance
2. Multiple Inheritance(MRO)
    2.1 Method Resolution Ordering
3. Mixins
"""
# 1
class Base:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
        
    def hit_me(self):
        print(getattr(self, 'args', None))
        print(getattr(self, 'kwargs', None))
        print("hit_me from Base")
        
        
class A(Base):
    def __init__(self, *args, **kwargs):
        if kwargs.get('a') == 4:
            kwargs['a'] = -6
        super().__init__(*args, **kwargs)
        
# 2
class Base1:
    def hit_me(self):
        print("hit_me from Base1")
        super().hit_me()  
        
class Base2:
    def hit_me_twice(self):
        print("hit_me_twice from Base2")
        
    def hit_me(self):   
        print("hit_me from Base2")
        #super().hit_me()
        self.hit_me_twice()
        
class A(Base1, Base2):
    def hit_me_twice(self):
        print("hit_me_twice from A")
        super().hit_me_twice()
        
    def hit_me(self):   
        print("hit_me from A")
        super().hit_me()
    
# 3

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
