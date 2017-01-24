from ikea.fields import *


class BaseMeta(type):

    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)    
        if not hasattr(clsobj, '_tables'):
            clsobj._tables = {}
            
        if not hasattr(cls, '_registry'):
            clsobj._registry = []            
        
        if '__tablename__' in clsdict:
            cur_tablename = clsdict['__tablename__']
            cur_table_content = {}
            
            for k, v in clsdict.items():            
                if isinstance(v, Column):
                    if isinstance(v, PKColumn):
                        cur_table_content['PK'] = (k, vars(v))
                    if isinstance(v, IntegerColumn):
                        cur_table_content['INT'] = (k, vars(v))
                    if isinstance(v, TextColumn):
                        cur_table_content['TEXT'] = (k, vars(v))
            clsobj._tables[cur_tablename] = cur_table_content
        return clsobj
