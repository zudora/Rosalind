
def find_clump(genome, k, L, t):
    # A kmer pattern forms an (L, t) clump in string genome if
    # there is an interval L in which pattern appears at least t times

    kmerSet = set()
    length = len(genome)
    winRange = length - L
    for winStart in range(0, winRange + 1):        
        winEnd = winStart + L
        localKmers = mostFreqkmer(k, genome[winStart:winEnd])
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

genome = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTACACA"
k = 9
L = 500
t = 3
clump = find_clump(genome, k, L, t)
clumpStr = ""
for val in clump:
    clumpStr += " " + str(val)
print clumpStr