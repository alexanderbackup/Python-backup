def is_credit_card_valid(number):
    if len(str(number)) % 2 == 0:
        return False
    number = str(number)
    temp = ''
    for i in range(len(number)):
        if i % 2 == 1:
            temp += str(int(number[i])*2)
        else:
            temp += str(int(number[i]))
    return sum(int(i) for i in temp) % 10 == 0


print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
