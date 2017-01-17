import json
import xml.etree.ElementTree as ET


class JsonableMixin:
    serializeable_types =(dict,
                          list,
                          tuple,
                          str,
                          int,
                          float,
                          bool,
                          None
                         )
    def to_json(self, indent=4):
        data = {
            'dict': self.__dict__,
            'classname': self.__class__.__name__
                }
                
        for k, v in self.__dict__.items():
            if type(v) in self.serializeable_types:
                data["dict"][k] = v
        
        return json.dumps(data, indent=4)
    
    def to_before_json(self):
        data = {
            'dict': self.__dict__,
            'classmethod': self.__class__.__name__
               }
        for k, v in self.__dict__.items():
            if type(v) in self.serializeable_types:
                data['dict'][k] = v
            if isinstance(v, JsonableMixins):
                data['dict'][k] = v.to_before_json()
                
        return data   
           
           
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        classname = data.get('classname', None)
        
        if cls.__name__ != classname:
            raise ValueError('{} != {}'.format(cls.__name__,
                                               classname))
        return cls(**data['dict'])

class XmlableMixins:
    def to_xml(self):
        root = ET.Element('root')
        
        
    def from_xml(self, xml_string):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
