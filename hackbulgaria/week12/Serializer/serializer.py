import json
from datetime import datetime


class MetaSerializer(type):
    def __new__(cls, name, bases, clsdict):
        json_stuff = None
        #(a call to .is_valid() has been made before that):
        _is_valid_called = True
        
        
        
        
        clsobj = super().__new__(cls, name, bases, clsdict)
        return clsobj

class Serializer(metaclass=MetaSerializer):

    def __init__(self, _obj):
        self._obj = _obj
        
    def is_valid(self, thing=None):
        print(vars(self._obj))
        
    def data(self):
        return self.json_stuff
        
class EmailField():
    pass
   
class CharField():
    pass
       
class DateTimeField():
    pass   
           
class CommentSerializer(Serializer):
    email = EmailField()
    content = CharField()
    created_at = DateTimeField()
    

class Comment(object):
    def __init__(self, email, content, created_at=None):
        self.email = email
        self.content = content

        if created_at is None:
            created_at = datetime.now()

        self.created_at = created_at


 
    
comment = Comment(email='radorado@hakbulgaria.com', content='wie naistina li hakvate?')
serializer = CommentSerializer(comment)
serializer.is_valid()

