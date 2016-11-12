


def reduce_file_path(path):
    print('\n', path)
    result = []
    for i in path.split('/'):
        if i == '..' and result != []:
            result.pop()
        elif '.' in i or '' == i:
            pass
        else:
            result.append('/'+i)
    if result == []:
        result.append('/')
	#print(''.join(result))
    return ''.join(result)




print (reduce_file_path("/"))

print (reduce_file_path("/srv/../"))

print (reduce_file_path("/srv/www/htdocs/wtf/"))

print (reduce_file_path("/srv/www/htdocs/wtf"))

print (reduce_file_path("/srv/./././././"))

print (reduce_file_path("/etc//wtf/"))

print (reduce_file_path("/etc/../etc/../etc/../"))

print (reduce_file_path("//////////////"))
print (reduce_file_path("/../"))
