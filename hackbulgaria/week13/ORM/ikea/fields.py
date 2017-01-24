class Column:
    def __init__(self, *args, **kwargs):
        pass
        
class PKColumn(Column):
    pass
    
class IntegerColumn(Column):
    def __init__(self, number):
        self.number = number
    
class TextColumn(Column): 
    def __init__(self, max_length=None):
        self.max_length = max_length
