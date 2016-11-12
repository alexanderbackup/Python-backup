# Word Counter
def word_counter():
	word = input()
	rolls_columns = input()
	rolls_columns = [int(i) for i in rolls_columns.split()]
	
	count = 0

	if len(word) > rolls_columns[0] or len(word) > rolls_columns[1]:
		print('Invalid number of rows or columns!')
		return

	grid = {}  # horizontal rows
	for i in range(rolls_columns[0]):
		grid[i] = input().replace(' ', '')
		
	grid_2 = {}  # vertical grid (reverse horizontal for easy search)
	for i in range(rolls_columns[1]):
		grid_2[i] = ''
		for j in range(rolls_columns[0]):
			grid_2[i] += grid[j][i]
	
	def count_words(word, d):  # takes searched word and d -> grid dict
		count = 0
		if word == word[::-1]:
			check = False
		else:
			check = True
		for column, row in d.items():
			if word in row:
				count += len([i for i in row.split(word) if i == ''])
			if word[::-1] in row and check:
				count += len([i for i in row.split(word) if i == ''])
		return count
	
	count += count_words(word, grid) + count_words(word, grid_2)
	print(count)

word_counter()


