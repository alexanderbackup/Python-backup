# numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]) = "abc"
def numbers_to_message(pressed_sequence):
    key_board = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 
             7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: ' '}

    def convert(seq_check, capital_check):
        if seq_check == []:
            return ''
        t = len(seq_check)
        while t > len(key_board[seq_check[0]]):
            t -= len(key_board[seq_check[0]])
        if capital_check:
            return key_board[seq_check[0]][t-1].upper()
        else:
            return key_board[seq_check[0]][t-1]
    result = ''
    seq_check = []
    capital_check = False

    for i in pressed_sequence:
        if i == 1:
            capital_check = True
        elif i == 0:
            result += convert(seq_check, capital_check)
            result += key_board[0]
            seq_check = []
        elif i in seq_check or seq_check == []:
            seq_check.append(i)
        else:
            result += convert(seq_check, capital_check)
            if capital_check:
                capital_check = False
            if i == -1:
                seq_check = []
            else:
                seq_check = [i]
    result += convert(seq_check, capital_check)
    return result

#print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))





def message_to_numbers(message):
    key_board = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 
             7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0: ' '}    
    result = []
    for i in message:
        if i.isupper():
            result += [1]
            i = i.lower()
        for k, v in key_board.items():
            if i in v:
                temp = [k for i in range(v.index(i)+1)]
                if result != [] and temp[0] == result[-1]:
                    result += [-1] + temp
                else:
                    result += temp
    return(result)


message_to_numbers("abc")
message_to_numbers("a")
print(message_to_numbers("Ivo e Panda")) #= [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
print(message_to_numbers("aabbcc")) #= [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]










