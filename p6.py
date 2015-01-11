# Given: A string s of length at most 10000 letters.

# Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.

# Sample Dataset

# We tried list and we tried dicts also we tried Zen
# Sample Output

# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1

s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

wf = {}
c = 0
lastSp = -1
wordSt = 0

for word in s.split(' '):
		if word in wf:
			wf[word] += 1
		else:
			wf[word] = 1

# while c < len(s):
	
# 	if s[c] == " ":
# 		word = s[wordSt : c]
# 		if word in wf:
# 			wf[word] += 1
# 		else:
# 			wf[word] = 1

# 		lastSp = c
# 		wordSt = c + 1

# 	c += 1

for word, freq in wf.items():
	print word, freq
