
# TODO: Nobody cares sabout SQL, I have metaprogramming to do !

DB_NAME = 'test_ikea.db'
                
def create_table(tbl_name, tbl_contet: iter):
    
    print('='*5,'Creating Tables !', '='*5)
       
    result = None
    print(tbl_name)
    for k, v in tbl_contet.items():
        print(k, v)
        
           
    create_custom_query = '''
        CREATE TABLE IF NOT EXISTS {0} (
        {1}    
        )
    '''.format(tbl_name, result)
    
def insert_into_table(tbl_name, **_content):

    print('='*5,'Inserting into Tables !', '='*5)   
    result = None
    for k, v in _content.items():
        print(k, v)
    
    insert_into_table = '''
        INSERT INTO {0} values ({1})
    '''.format(tbl_name, result)
    
def filter_table(tbl_name, **_content):
    
    print('='*5, 'Filtering ?', '='*5)
