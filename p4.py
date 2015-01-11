import math
# Given: Two positive integers a and b (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset

# 100 200

# 7500
 


a = 4239
b = 8315
n = a
s = 0

while n <= b:
	if n%2 != 0:
		s+= n
	n+=1

print s