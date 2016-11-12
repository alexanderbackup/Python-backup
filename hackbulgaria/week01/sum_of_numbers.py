def sum_of_numbers(s):
    temp_digit = '0'
    result = []
    for i in s:
        if i.isdigit():
            temp_digit += i
        else:
            result.append(int(temp_digit))
            temp_digit = '0'        

    return sum(result + [int(temp_digit)])

print(sum_of_numbers("ab125cd3"))
