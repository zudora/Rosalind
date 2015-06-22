
def pattStart(pattern, genome):
    posList = []
    posString = ""
    pattLen = len(pattern)
    for i in range(0, len(genome)):
        if genome[i:i+pattLen] == pattern:
            posString += " " + str(i)

    return posString

outString = pattStart("GCAAGAGGC", "CCGCGCAAGAGTTTGGCAAGAGTGCAAGAGCGCAAGAGTAGGCAAGAGGCAAGAGTATTAGTAGCAAGAGGCAAGAGTCTGCAAGAGCCGCAAGAGGCAAGAGGGCAAGAGAGCAAGAGTTGTGCAAGAGGCAAGAGGATTCGCAGTCCGCAAGAGTGCAAGAGTGGGCAAGAGGCAAGAGGGCAAGAGCACGACGATATTAGCAAGAGAGCAAGAGCTGCTGTCGGCAAGAGTATAGCAAGAGTGGCAAGAGGCGAACCGGTGAGCAAGAGGCAAGAGTGATGCAAGAGTGTATGCAAGAGGGCAAGAGAGATGTTCTAGCAAGAGCATACTCCACTCGCAAGAGGAGCAGACGGCAAGAGGCAAGAGCGCAAGAGAGCAGATAAACTGCAAGAGAGCAAGAGCGCAAGAGTCACCGCAAGAGCGCGCAAGAGGCAAGAGGCAAGAGTGCTGCAAGAGCGCAAGAGGCAAGAGACAGCAAGAGACGCAAGAGCAAGCTGGAGCAAGAGGCAAGAGGCAAGAGAGCAAGAGAGCAAGAGCGGACGCAAGAGACCTAGCAAGAGATGCAAGAGGCAAGAGAGCAAGAGTGTGGCAAGAGTTTTTGCAAGAGTCGGCAAGAGGCAAGAGGCAAGAGTGGCCCGCAGCAAGAGTGGCAAGAGAGCAAGAGCTTGCAAGAGGGCAAGAGGTTGGAGCAAGAGCTTGCAAGAGTGTGCAAGAGCACGCAAGAGGGCAAGAGTGCGCAAGAGTGCAAGAGAGGGGCAAGAGCGCAAGAGCAGCGCAAGAGTCGCAAGAGCCGGCAAGAGTAGTTTGGGCAAGAGCGCAAGAGGCAAGAGACCTTTGCAAGAGTGCAAGAGTTATCGCAAGAGTCGCAAGAGGCAAGAGGATAGGGCAAGAGGCAAGAGATATCAACGCAAGAGACAGCAAGAGAAGCAAGAGCGCAAGAGATGGCAAGAGAGCAAGAGGCAAGAGGCAAGAGTGAGCAAGAGTTGACTGCAAGAGCGAGCAAGAGGCAAGAGGTGCAAGAGATCGCAAGAGGCAAGAGGCAAGAGTAGCAAGAGGCAAGAGGGCAAGAGGCAAGAGGATGAGCAAGAGTAGCAAGAGATGGCAAGAGGATGCAAGAGCGAGCAAGAGGCAAGAGACAGCAAGAGAAGGCAAGAGGGCAAGAGGTCGCGCAAGAGGCAAGAGTGCAAGAGCGTTGACTCTGCAAGAGGCAAGAGGCAAGAGGCAAGAGGTGCAAGAGGCAAGAGGTCAAAAGGCAAGAGTGAAAGCAAGAGAACGTACGCAAGAGGCAAGAGCCATATTGGTGCCAAGGCAAGAGAGGCAAGAGGCAAGAGCGCAAGAGCGCAAGAGGGCAAGAGGGTGCGCAAGAGGCGCAAGAGGCAAGAGATGTTGGCAAGAGGCGTCTAGCAAGAGGCAAGAGCAGCAAGAGGCGCAAGAGGCAAGAGAAGTGGGCAAGAGGCAAGAGGCAAGAGGCGGGAGCAAGAGGCAAGAGTCCGCAAGAGACTAATAGCTGCAAGAGCTCAGCTCATGCAAGAGGCAAGAGGCAAGAGAACGCAAGAGTGTCGCAAGAGGTATCAAGCAAGAGGCAAGAGTAGCAAGAGTGCAAGAGTAGCAAGAGGGCAAGAGGCAAGAGGTAGCAAGAGAAACTAGGGCAAGAGATATCGCCAGCAAGAGAAACTGCAAGAGCAGGCAAGAGGCAAGAGGCAAGAGAGGCAAGAGCGGGCAAGAGTGCAAGAGGCAAGAGTGAAGCAAGAGGTATAGTACCGCAAGAGGCAAGAGTCCTAGGCAAGAGGCAAGAGTGCAAGAGATGGACGCAAGAGGCAAGAGGCAAGAGGAGCAAGAGTGCAAGAGCGCAAGAGAGCAAGAGCCATGCAAGAGGTGCAGCAAGAGGCAAGAGTAGGGCGGCAAGAGGGTGGCAAGCAAGAGGCAAGAGGCAAGAGGGGGCAAGAGTTCGTGTGCAAGAGATGAGCAAGAGGCAAGAGTACACAAGCAAGAGGCATCCTAGGGCAAGAGCGCAAGAGCATAGTGCAAGAGGCAAGAGACAGCAAGAGATAAATCGCAAGAGGCAAGAGAGCAGGCAAGAGTGGCGCAAGAGGCAAGAGGCAAGAGCGCAAGAGAGTCGAAGCTACTGCAAGAGAGCAAGAGATAGCAAGAGGCAAGAGCTCGGCAAGAGCCAGCAAGAGTTCAGGCAAGAGATCTTCATTGCAAGAGAAGTAGCAAGAGGCAAGAGAGCAAGAGATATGCAAGAGTAATATTGATCGCAAGAGCCCGATGTAGAGCAAGAGGGTGCAAGAGGGTCCGAGCAAGAGAGGCAAGAGTTTTCGCAAGAGGCAAGAGCCGCTTCGGCAAGAGTTCCGCAAGAGGGCAAGAGAGGCAAGAGGCAAGAGACCGACTCGCAAGAGGCAAGAGAACCACGCAAGAGTGGCAAGAGCGCAAGAGGCAAGAGAGCGGGCAAGAGTCGCAAGAGGCAAGAGAGCGCAAGAGTGCAAGAGTCGCAAGAGAACCCGCAAGAGAAATGCAAGAGGGTTGCAAGAGTGGCAAGAGGTACGGCAAGAGACGAGCAAGAGGGCAAGAGGTTCCCCGCAAGAGGCAAGAGGTCAGGCAAGAGGCAAGAGCAGCAAGAGTGCAAGAGGCAAGAGTAAAGGCAAGAGGGCAAGAGCGCAAGAGGCAAGAGTACCTGGCAAGAGCGCAAGAGGCAAGAGAGTGCAAGAGCGTATGCAAGAGGGGCAAGAGCCAATAGCAAGAGTTCTGTTCTAGCAAGAGATATGCAAGAGATTGCAAGAGCCGGCAAGAGCTTGAGCAAGAGTACTATGAGCAAGAGGAGCAAGAGAGACCCCCTCATTCCCGCAAGAGACAATGCAAGAGGCAAGAGTCAGCAAGAGATGCTATGATTGCAAGAGCGTCGCAAGAGGCAAGAGCACGGCAAGAGGCTAGCAAGAGTTGTGCAAGAGCCAGTGCAAGAGGCAAGAGAGGCAAGAGCTAGCGCAAGAGGGCAAGAGGCAAGAGGCAAGAGCTGCAAGAGGCAAGAGGCAAGAGATGCAAGAGGCAAGAGGCAAGAGGGCAAGAGGGCAAGAGGTGTCGCAAGAGGCAAGAGAAGTGCAAGAGACGCAAGAGGCAAGAGCCGGACGCAAGAGCAGCGCAAGAGTGCAAGAGAGCAAGAGAGATTGCAAGAGTGCAAGAGTTTGGCGCAAGAGCGGCAAGAGCATGCAAGAGGCAAGAGGCAAGAGCTTGGCAAGAGTGGCAAGAGTGCAAGAGTACCAAGCAAGAGCCCAAGCAAGAGGGCGGCAAGAGTCGCAAGAGCGACAGTTTGGCAAGAGGCAAGAGGCAAGAGGGTTCGCAAGAGAGCGCAAGAGGCAAGAGGCAAGAGACACGGCAAGAGGCAAGAGGGGAGGCCGGGCAAGAGCGCAAGAGGCAAGAGCGATATCAGCAAGAGAGGGCGATATCACGGCAAGAGGGGCAAGAGCAGCACTAGGCAAGAGGACTTGCAAGAGGCAAGAGCGACGCGCAAGAGCTTGCAAGAGCCATGCAAGAGCGCAAGAGCTAGCAAGAGTCACGCAAGAGGGCGGCAAGAGCGCAAGAGGCAAGAGGGTAGCAAGAGGCAAGAGAGTGCAAGAGGCAAGAGCCGCGCACTGCAAGAGGCAAGAGGGGCAAGAGTCGGCAAGAGAACTGCAAGAGCGTGGGTGCAAGAGCTGCAAGAGAGCCGCAAGAGGCAAGAGGCAAGAGCAATCCACTAAGCAAGAGAGGCAAGAGGCAAGAGTGCAAGAGGCAAGAGCTGTGCAAGAGGGACGCAAGAGAGCAAGAGGGGCAAGAGGCAAGAGGAATACTGCAAGAGCGCAAGAGGCAAGAGGCAAGAGAGCAAGAGCGCAAGAGAGTACGCAAGAGTGGCAAGAGCGCAAGAGTCCAACGCAAGAGCGAGCAAGAGTCTGCAGCAAGAGGAGCAAGAGAGGAGCAAGAGGCAAGAGCCGGGCAAGAGGGCAAGAGCCTTGCAAGAGTACCGCAAGAGAGGGTAGGCAAGAGGACTGTGCAAGAGGCAAGAGGCAAGAGGCAAGAGACGGCAAGAGGCAGTGCAAGAGAGCTAGAAGACCGGGCAAGAGGGGCGCAAGAGTACGCAAGAGTGCAAGAGGGAGCATAGCAAGAGGTAGCCGCAAGAGGCAAGAGTCTGCAAGAGAGCAAGAGTCGAGTCGCAAGAGTAGCAAGAGACTGCAAGAGCGCAAGAGTAGCAAGAGGGGCAAGAGAGCAAGAGCAAAGTAGCAAGAGACTTCAGCAAGAGGGACTGGCAAGAGGCAAGAGTAGCAAGAGAATAAGCAAGAGCCAGCAAGAGGCAAGAGTGCAAGAGGTGCAAGAGTGCTGCAAGAGCTGCAAGAGAGGCAAGAGGCAAGAGTGGGCAAGAGTGATTGGCGGCAAGAGGTAGCAAGAGTCGCAAGAGCGCAAGAGAGCAAGAGGGCAAGAGGGGGCAAGAGGGTGGGTGCAAGAGTGATAATCGCAAGAGGCGGCAAGAGTGCAAGAGGGTGCAAGAGGGGTCGCAAGAGACGCAAGAGTGCAAGAGCCCTGCAAGAGCTGCAAGAGTCCCGATCCGCAAGAGTGCAAGAGAGCAAGAGAGGCAAGAGGCAAGAGCCATTTTGCAAGAGTGCAAGAGAGAGCGCAAGAGTGCAAGAGAGCAAGAGGTGGATCTGCAAGAGCGCAAGAGTAGCAAGAGGCAAGAGACGAAGCAAGAGATAACGCTACAGCAAGAGCCTGCAAGAGGCAAGAGAGGCCAGTAGGCAAGAGGCAAGAGCTGCAAGAGGCAAGAGGCAAGAGTACGCAAGAGGCAAGAGTGCAAGAGAAGTTAGGGCAAGAGGCAAGAGGCAAGAGTGGCAAGAGGGCAAGAGGCAAGAGTGCAAGAGGCAAGAGCGGGCAAGAGGTGCAAGAGTGGGCAAGAGCTGCCATGCAAGAGGCAAGAGATGGCAAGAGGGCAAGAGGATGCAAGAGCAGCAAGAGGCAAGAGGCAGCAAGAGACACGAGGCAAGAGGAACTATGCAAGAGGCAAGAGGCAAGAGTAATTCTGCAAGAGCATGAGACTGGGCGCAAGAGGCAAGAGTGCAAGAGGATCGCAAGAGCGCAAGAGCAGCGCAAGAGTATCCTAAACTTGCAAGAGCTGGAGCAAGAGTTCCATGATGGCAAGAGGAGCAAGAGCATGCAAGAGCTAGCAAGAGAGGCCGCACCTTAGGCAAGAGTTTGAACGCAAGAGTAGTCGCAAGAGGCAAGAGGAGCAAGAGACAATATGCAAGAGCTGGCAAGAGGTGCAAGAGTCCGTGCAAGAGACGGATCAAAGGGCAAGAGTCCGCAAGAGGCAAGAGGTTAGCAAGAGCGCAAGAGCAGCAAGAGGCAAGAGAGCAAGAGGCAAGAGTGCGCAAGAGAGCAAGAGGCAAGAGGCAAGAGAGGTGCAAGAGGCAAGAGAACGCAAGAGAGCGCAAGAGGTGCAAGAGCCGGCAAGAGCCAGGCAAGAGTTTGCAAGAGGTGCAAGAGGGGCAAGAGGCAAGAGTCGCAAGAGCCTATAGCAAGAGGCAAGAGGCAAGAGGCAAGAGGCAAGAGGCAAGAGTACAGGGCAAGAGCGCAAGAGCGGGGCAAGAGACCAGCAAGAGGGCAAGAGTGCAAGAGTGGCAAGAGGCAAGAGTAGGCAAGAGGGCAAGAGATAGCAAGAGAGCAAGAGGGGGACTTGCAAGAGGCAAGAGCATCGCGGGCAAGAGAGCAAGAGCAGAGCAAGAGCGCTCGCAAGAGAGCAAGAGCGCAAGAGGCAAGAGCAAGCAAGAGGTAAGAGGGCAAGAGGCAAGAGTGCAAGAGGACGCAAGAGGGCAAGAGGCAAGAGGGCAAGAGGAGCAAGAGGCAAGAGCCGAGGGCAAGAGCATAGCAAGAGGGCGCAAGAGGGGCAAGAGGCAAGAGGCGCAAGAGGGCAAGAGTGCAAGAGTCGCAAGAGCGCAAGAGCAGCAAGAGTGAACCGCAAGAGGCAAGAGAAAGGGAAGCAAGAGAGCTGCAAGAGACCCGCAAGAGGCAAGAGTCTTGGCAAGAGGCAAGAGCGCAAGAGAGGCAAGAGGCAAGAGCCAGCAAGAGGCAAGAGGGGCAAGAGCTGCAAGAGCAAAACTGGGCAAGAGTAGCAAGAGAAAGTGCAAGAGGTGCAAGAGTGCAAGAGTGCAAGAGGCTGAGCAAGAGAAAGGGAGCAAGAGCGCAAGAGAATGCGCAAGAGGCAAGAGAACTGGCAAGAGTTCGAGCAAGAGGCAAGAGATGCGCAAGAGGGCAAGAGCGCGCAAGAGGTGCAAGAGGGCAAGAGGGGCAAGAGCCGCAAGAGCGCAAGAGCGCAAGAGGCGCAAGAGTCTTGCAAGAGCGCAAGAGTACGCAAGAGTGGCAAGAGGGCAAGAGGTGGCAAGAGGAGCAAGAGTGGCAAGAGGCAAGAGTTCGGCAAGAGGCGCAAGAGTGATGGCAAGAGCCGCAAGAGTGCAAGAGATGCAAGAGTCGCAAGAGGCAAGAGGCAAGAGCACGCAAGAGTTAGCAAGAGGCAAGAGGCAAGAGCCTGAACGCAAGAGCGCAAGAGCTCGGACGACGCAAGAGCCGCAAGAGGCGCAAGAGAATGCGGCAAGAGCGAGCAAGAGAGCAAGAGGCAAGAGGCCTTCCGCAAGAGAGCAAGAGCTCGGTGCAAGAGGCAAGAGGCAAGAGCGCAAGAGTAAGGCAAGAGGCAAGAGAAACTGCAAGAGCTAGATTGCAAGAGTCCCGCAAGAGACAGCAAGAGTACACCTAAGCAAGAGGCGCAGCAAGAGGTCGGCAAGAGTACGCAAGAGTTGGGCAAGAGCGCGGCAAGAGGCAAGAGTCAGAGAAGCAAGAGGGTGCAAGAGGCAAGAGGAAGTCAGAGTATTTTTTTTTCGGAGTTTAGCAAGAGACGCCTTCTTGCAAGAGGGGCAAGAGAGGGGCGCAAGAGGCAAGAGTGCAAGAGTGGCAAGAGGCAAGAGGCAGCAAGAGGGGCAAGAGACAAGCAAGAGGCAAGAGCCTCGGGCAAGAGCGCAAGAGGCAAGAGTATCGCAAGAGGCAAGAGGTATTTACGCAAGAGGCAAGAGGATGTGCAAGAGTATGCAAGAGATTTGCAAGAGCGCAAGAGAGCAAGAGGCAAGAGACGCAAGAGGTAATGCCGCAAGAGGCCGCGGGCGCGTTGCAAGAGCCGGCAAGAGTCGCAAGAGCTGCAAGAGGTAGTGGAGGGCAAGAGTTGCAAGAGTTGGCAAGAGTCGCAAGAGGTTCGCAAGAGGGGCAAGAGTTCCCGCAAGAGGATGGCAAGAGTAGCAAGAGCGACCGCAAGAGGCAAGAGGCAAGAGAGCAAGAGAGAGGCAAGAGAAGCAAGAGTGCAAGAGGGTAAGCAAGAGGCAAGAGAGCAAGAGGGCAAGAGGCAAGAGGCGAGATAGGACTTGCAAGAGGGGAGCAAGAGGCAAGAGAGTGCAAGAGGCAAGAGGCAAGAGAGTTCGGCAAGAGTTAGGCAAGAGACTAAATGCAAGAGGCAAGAGCTATCAGCAAGAGGCAAGAGTGGCAAGAGGCAAGAGAGCAAGAGCGTCAGCCTGCAAGAGGGGAGGGCAAGAGAGCAAGAGGCAAGAGGGCAAGAGATGCAAGAGGAGCAAGAGGCAAGAGCGATATTGGGCAAGAGGAGGCAAGAGATGGCAAGAGGAGCAAGAGATCGCAAGAGTTATACGCAAGAGGCAAGAGGGCAAGAGTGCAAGAGAGGCAAGAGTAGCAAGAGGGCAAGAGAAGCAAGAGGCAAGAGCCAGCAAGAGCAACGATTGCAAGAGGCAAGAGCTTGCCGCAAGAGGCAAGAGGGCAAGAGATCGAGCAAGAGAGCAAGAGAGCAAGAGTTGCAAGAGAAACCCTGCATCGCAAGAGTTGGAATGGCAAGAGCGCAAGAGTGCAAGAGGGCAAGAGGGCAAGAGATACCGCAAGAGATGCAAGAGGGGGGCAAGAGGCAAGAGGCAAGAGAATAGCAAGAGGCAAGAGGCAAGAGTGCAAGAGGAGCAAGAGCGCCGCAAGAGGCAAGAGGGCGTACCCTGCAAGAGAGGAGAAGGGCAAGAGAATGCAAGAGAAGCAAGAGTGCCGGGCAAGAGATGTGCAAGAGGCAAGAGGCAAGAGGCAGAATCTAGGGGGCAAGAGGCAAGAGCTGTGTGCAAGAGTCATGCAAGAGTATTAGGCAAGAGACGGCAAGAGATTGCAAGAGATGCAAGAGGCAAGAGTCGCAAGAGTCTTCGCAAGAGTCATGCAAGAGGTCCGTCCATGGCAAGAGGCTGCAAGAGGCAAGAGCAGACGCAAGAGTAGGCAAGAGAGCAAGAGTTGCAAGAGTAGCAAGAGGCAAGAGGTGCGCAAGAGAGCAAGAGGCAAGAGTGCAAGAGAAATGCAAGAGTGCAAGAGGGCAAGAGGCAAGAGCGCAAGAGCAATGCAAGAGGCAAGAGACGCCTGCAAGAGGCGCAAGAGACCGCGGCGCAAGAGGCAAGAGATCGGCAAGAGACTGCAAGAGCGCAAGAGCGCAAGAGCTGCGCAAGAGACGGATGCCGCAAGAGGCAAGAGCTCGCAAGAGATGGCAAGAGGGCAAGAGCGAATAGCAAGAGCCCCTGGCAAGAGTGCAAGAGTTTGTGGTGCGCAAGAGCCGGCAAGAGGCAAGAGAGCAAGAGGCAAGAGGTGCAAGAGGCAAGAGTTGCAAGAGGAAAGGCAAGAGTGACGGGCAAGAGTTGCAAGAGAGCAAGAGTTCCCTACGCAAGAGTAGCAAGAGTGCAAGAGTGCAAGAGGTTCGCAAGAGAGGCAAGAGGCAAGAGGAGGCAAGAGGCTCCCTCTAATAGCAAGAGGCAAGAGTGCAAGAGCGGCAAGAGGAGCGCAAGAGTGCAAGAGACGCAAGAGGGAAGGCGCAAGAGTGACTGCAAGAGGTTATGCAAGAGAGCAAGAGGCAAGAGCGCAAGAGAGTGCAAGAGGCAAGAGGGCAAGAGGCCAAGCAAGAGGCGCCGCAAGAGAGAGCAAGAGGCGCAAGAGAACTACGGCAAGAGGCAAGAGGCAAGAGGGCAAGAGGCAAGAGCGCAAGAGGCAAGAGGCAAGAGATTCTGAGCGTGCGCAAGAGCCATTGGCAAGAGATTTCATCGAGGCAAGAGGGGGCAAGAGTAACATGCAAGAGGCAAGAGGCAAGAGTGCAAGAGAGTATAGCAAGAGTTGCAAGAGGGAGCAAGAGTGCAAGAGCAGCAAGAGCGGCAAGAGGGCAAGAGGCAAGCAAGAGGCAAGAGGCAAGAGGGCAAGAGGATGCGCAAGAGGCAAGAGGGCAAGAGGCAAGAGTGCAAGAGAACATCAAGCAAGAGGCAAGAGAGTTGGGACGCAAGAGTGCAAGAGTGCAAGAGGCAAGAGTGCAAGAGGCAAGAGTAGGCGCAAGAGTGACGCAAGAGGCAAGAGGCAAGAGGCAAGAGACGCAAGAGATGATAAGCAAGAGGCAAGAGCTGCTGCAAGAGGGCGCAAGAGTATCTAGTCACCAGCAAGAGGCAAGAGAAAAGCAAGAGACGTGCAAGAG")
print outString