#Are two words anagrams?
def anagrams():
	words = input().lower().split(' ')
	def test(word1, word2):
		if word1 == word2 == []:
			return 'ANAGRAMS'
		elif word1[0] == word2[0]:
			return test(word1[1:], word2[1:])
		else:
			return 'NOT ANAGRAMS'
	return test(sorted(words[0]), sorted(words[1]))

#Gas Stations
def gas_stations(distance, tank_size, stations):
	travelled = 0
	fuel_left = tank_size
	result = []
	road = stations[:]
	road.append(distance)
	for i in range(len(road)-1):
		fuel_left -= road[i] - travelled
		travelled = road[i]
		if fuel_left < (road[i+1] - road[i]):
			result.append(road[i])
			fuel_left = tank_size
	return result

def test(n = 'n'):
	pass

test()
