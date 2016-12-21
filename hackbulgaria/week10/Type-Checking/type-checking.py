import sys


def main():
    inpt = list(sys.stdin)
    funcs = []
    
    for i in inpt:
        row = i.strip('\t\r\n')
        if '::' in row:
            temp = [s.replace(' ', '') for s in row.split('::')]
            funcs.append(temp)   
        if '.' in row:
            temp2 = [s.replace(' ', '') for s in row.split('.')]
            funcs.append(temp2)
    result = []
    temp = None
    for i in funcs[:-1]:
        smth = i[1]
        if not temp:
            temp = smth[smth.index('->'):].replace('->', '')
        elif smth[:smth.index('->')].replace('->', '') == temp:
            result.append(True)
        else:
            result.append(False)
        temp = smth[smth.index('->'):].replace('->', '')     
    if all(result) and result != []:
        print(True)
    else:
        print(False)       
                
if __name__ == '__main__':
    main()
