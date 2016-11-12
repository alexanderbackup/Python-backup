def birthday_ranges(birthdays, ranges):
    result = []
    for i in ranges:
        count = 0
        for n in birthdays:
            if n >= i[0] and n <= i[1]:
                count += 1
        result.append(count)
    return result

print(birthday_ranges(
    [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], 
    [(4, 9), (6, 7), (200, 225), (300, 365)]))
