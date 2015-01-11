#Given: A string s of length at most 200 letters and four integers a, b, c and d.

#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

s = "QEPU0gADz8xnTReE5cWTzS5vXyMsNinoxoxTamstriatusxm3xiy4V5HMgClFELMCE1wQ1ZpcB6fgRt1Z8aybCuEDlDsuvxgz3SPZYoI9VLSOl964rnoPMikYkksqp4DO3im3PAAZponvbIgj4Mj2rfteGz4PHLcz5Af73EI9Oj6uR0."

inds = [28, 32, 38, 45]

startInd = inds[0]
endInd = inds[1]
nextSt = inds[2]
nextEnd = inds[3]

print s[startInd:endInd+1], s[nextSt:nextEnd+1]




