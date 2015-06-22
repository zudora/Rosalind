
def mostFreqkmer(kmerLen, inString):
    
    freqList = {}

    for index in range(0, len(inString)):
        
        testString = inString[index:index + kmerLen]
        
        if testString in freqList:
            freqList[testString]+=1
        
        else:
            freqList[testString] = 1

    return freqList

newFreqList = mostFreqkmer(3, "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA")
maxFreq = 0
maxItem = ""
for item in newFreqList:
    if newFreqList[item] > maxFreq:
        maxFreq = newFreqList[item]
        maxItem = item

print maxFreq
print maxItem