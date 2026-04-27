arrays = [2, 8, 9, 48, 8, 22, -12, 2]
arrays2 = [x + 2 for x in arrays if x >5]
array = list(dict.fromkeys(arrays2))
print(arrays)
print(array)