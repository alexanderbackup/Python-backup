def is_number_balanced(n):
	n = str(n)
	if len(n) == 1:
		return True
	q = 0
	w = 0
	for i in range(len(n)//2):
		q += int(n[i])
		w += int(n[-i-1])
	return q == w
	
print(is_number_balanced(9))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))
