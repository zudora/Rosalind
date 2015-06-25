with open ("E-coli.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

def find_clump(genome, k, L, t):
    # A kmer pattern forms an (L, t) clump in string genome if
    # there is an interval L in which pattern appears at least t times

    kmerSet = set()
    length = len(genome)

    winRange = length - L
    
    for winStart in range(0, winRange + 1):        
        winEnd = winStart + L
        print "winStart: " + str(winStart) + ", winEnd: " + str(winEnd)
        if winStart == 0:
            localKmers = mostFreqkmer(k, genome[winStart:winEnd])
        else:
            dropKmer = genome[winStart - 1:winStart + k - 1]
            newKmer = genome[winEnd - k:winEnd]
            localKmers[dropKmer]-=1
            if newKmer in localKmers:
                localKmers[newKmer]+=1

            else:
                localKmers[newKmer] = 1
        for key in localKmers:
            if localKmers[key] >= t:
                kmerSet.add(key)       
        
    return kmerSet

def mostFreqkmer(kmerLen, inString):
    
    freqList = {}

    for index in range(0, len(inString) - kmerLen + 1):
        
        testString = inString[index:index + kmerLen]        
        if testString in freqList:
            freqList[testString]+=1
        
        else:
            freqList[testString] = 1

    return freqList

print "Opened file. " + data[0:10]
print str(len(data))
genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k = 9   
L = 500
t = 3
clump = find_clump(data, k, L, t)
clumpStr = ""
for val in clump:
    clumpStr += " " + str(val)
print "Done"
print clumpStr
print clump.count