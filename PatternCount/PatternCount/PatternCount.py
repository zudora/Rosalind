

def patternCount(Text, Pattern):

    count = 0

    for i in range(0, len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count

Pattern = "AGCCTTTAG"
Text = "TAACAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTGAGCCTTTGAGCCTTTTAGCCTTTCAGCCTTTAGCCTTTAAGCCTTTCCGCATCGAGCCTTTCAGCCTTTCGTAGCCTTTCGAGCCTTTAGCCTTTCAGCCTTTAGAGCCTTTAAGCCTTTAGTCGATGTAGCCTTTAGCCTTTAGCCTTTAGCCTTTGCAGCCTTTAGTAGGCAAGCCTTTTAGCCTTTGAGCCTTTCGAGCCTTTCTCGCTAGCCTTTAGCCTTTGGTGAGCCTTTTAGCCTTTAGCCTTTTCGCAGCCTTTTGAGCCTTTCTTGTTTGAATGGCAAGAGCCTTTTCGAGCCTTTAGCCTTTGAGCCTTTCAGCCTTTAAAAGCCTTTCGTTAGCCTTTAGCCTTTATCGAGCCTTTAAGCCTTTTATGCAAAGCCTTTGAGCCTTTAGCCTTTCAGCCTTTCAGCCTTTCATTGACAAGCCTTTCAGCCTTTAGCCTTTAGCCTTTCTCAGCCTTTGAGCCTTTGAGCCTTTGTCGAGCCTTTTTTCAGAGCCTTTTAGCCTTTAGCCTTTGAGCCTTTAGCCTTTAGCCTTTTACGAGCCTTTGCAAGCCTTTCAGCCTTTCCAAGCCTTTAGCCTTTGCTTTAGCCTTTCATGGGATAGCCTTTAGCCTTTATTAAGCCTTTTTTATCAAGCCTTTGTAGCCTTTAAGCCTTTCCAGCCTTTAGGAGCCTTTGTATAGCCTTTTGAGCCTTTCTACAGTAAAGCCTTTTTTGGTCAGCCTTTCTAGCCTTTGATAGCCTTTCTGAAGCCTTTGGCGGAGCCTTTCTGTTAACAGCCCAGCCTTTCTCATAGCCTTTGCGGTATCAGCCTTTGCAGCCTTTCTGGAGCGATAGCCTTTCAGCCTTTCCGAGCCTTTTTCAGAGCCTTTGAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTCCGAGCCTTTTCAGCCTTTACAGCCTTTTTAGCCTTTGAGCCTTTCACAGCCTTTGAGCTAGCCTTTAAGTTAAAGCCTTTAGCCTTTCAGCCTTTACATTAGCCTTTTAGCCTTTTCAGCCTTTAGAGCCTTTAGCCTTTGCTGAAGCCTTTAGTAGCCTTTAGCCTTTGCGAAGCCTTTCTGGTGCAACAAGTGAAGCCTTTGCCCTAGCCTTTGCTAGCCTTTCCGAGCCTTTGTCGATATAGCCTTTAGCCTTTAGAAAGCCTTTAGCCTTTGCTAGCCTTTATAGCCTTTAGCCTTTAGCCTTTCCCAGCCTTTAGCCTTTATCCTAAGCCTTTAGCCTTTTCCAGAAGCAGCCTTTTGATCAGAGCCTTTCTTCGGACTGCTCCCAGCCTTTAGCCTTTCAGCCTTTAGCCTTTAGCCTTTCAGCCTTTAGCCTTTTCTAGCCTTTAGCCTTTGTGTAGCCTTTCTAGCCTTTACGAGCCTTTGCCCAGCCTTTCCCAGCCTTTGAGAGCCTTTACCATATAGCCTTTACATAAGCCTTTGATGAGCCTTTAGCCTTTCGAGCCTTTCAGCCTTTACTCCAGCCTTTATAGCCTTTATATAGCCTTTCCTGTTAGGCCGTCGGTGCAGCCTTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTTAGCCTTTCAGCCTTTGCTAGCCTTTCCAGCCTTTACAGCCTTTTACCGAGCCTTTCCATCAGCCTTTAGCCTTTATATCTCTGATCGGGTAGCCTTTCGGCTAGCCTTTGGTAGCCTTTTTCAGCCTTTATGTAAAGCCTTTGTAGCCTTTGATGTGAGCCTTTAGAAGCCTTTGTCAGCCTTTTAGCCTTTAGCCTTTAGCCTTTTTAAGCCTTTTACAAGCCTTTACTCAGAGCCTTTACGAGCCTTTTAGCCTTTGCAGCCTTTTAGCCTTTTGATGAGCCTTTGCGGAGCCTTTTCTTTCAGCCTTTTGGCAGCCTTTAGCCTTTGTACAGCCTTTTTGAGCACAGCCTTTCGCGAAAGAGCCTTTATCAGCCTTTAAGCCTTTGCTAGCCTTTAGCCTTTTGAGCCTTTAGCCTTTGTATCTGTCTATCATCGAGCCTTTCTAAGCCTTTGCGGAAGCCTTTAGCCTTTGTCAGCCTTTCAAAGCCTTTAGCCTTTTATTCAAGCCTTTGAACCATAGCCTTTGGCAGCCTTTCAAGCCTTTGACGACAGCCTTTAGCCTTTCATTAGCCTTTTAGGAGGCTCATCCGTCTAGCCTTTAAATAGCCTTTAGCCTTTATAGCCTTTAAGCCTTTAGCCTTTTAAGCCTTTGAGAGCCTTTAAAGCCTTTAAACCAAGCCTTTGCGAAGCCTTTAGCCTTTAGCCTTTCGCAGCCTTTAGCCTTTCGAGCCTTTTGTAGCCTTTTGGAGAGCCTTTGGGCAAGCCTTTAGTATAAGCCTTTAGCCTTTTAGCCTTTCAAGCCTTTAGCCTTTAAGCCTTTGGCACAGCCTTTTGAGCCTTTCAGGAGCCTTTATTGGTGAGCCTTTAGTATAGCCTTTTCAGCCTTTGGCAGCCTTTAATGAAAGCCTTTGCTCAGCCTTTTTCAGCCTTTACAGCCTTTCAAGCCTTTAGCCACAAGCCTTTAGCCTTTAGCCTTTCAGCCTTTGCGAGCCTTTGTAGCCTTTAAGCCTTTCAGCCTTTAGCCTTTAGCCTTTTTCAAGCCTTTTCAGCCTTTCAAAGCCTTTCAAGCCTTTGAAGCCTTTCTAAGCCTTTGAGCCTTTGAGCCTTTGAGCCTTTAGCCTTTGTTCCTAGCCTTTATAGCCTTTTAGGCAGCCTTTCAGAGCCTTTTAAGCCTTTAGCCTTTCAGAAAGAGCCTTTAGCCCAGCCTTTTGATTAGCCTTTAGGGAACAGCCTTTAGCCTTTTAAGCCTTTGGTATACAATCAACGCAGCCTTTAGCCTTTAAGCCTTTTGGAGCCTTTCAGACTGATCCCAGCCTTTCAGCCTTTCTCAGCCTTTAAGCCTTTCTCCAAGCCTTTTGAGCCTTTTCGAGCCTTTAGTGAGCCTTTTGAAGCCTTTGTTTAGCCTTTTGTATAGGGTAGCCTTTAGCCTTTCCGGAAGCCTTTTGTAGCCTTTAAGCCTTTTGTCCGGGAAAGCCTTTGTAAGCCTTTAATGCAGCCTTTCCTATAGCCTTTAAGCCTTTCAGCCTTTTGGAGCCTTTTCTCAGCCTTTAGCCTTTCGCCAGCCTTTCTCCCGAGCAGCCTTTTAGAAAAAGCCTTTTAGCCTTTTACCGTGGACAGCCTTTCACGAGCCTTTACAGGCTAGCCTTTAGCCTTTGCTAGCCTTTTCCCAGCCTTTTGAGCCTTTAAGCCTTTCTAAGTTCTACGCTTGGGCTAAAGCCTTTAGCCTTTAAGCCTTTCAGCCTTTTGCAGCCTTTATATAACTTGAGCCTTTAGCCTTTAGCCTTTATAGCCTTTAGCCTTTTAGCCTTTTATATCCCTTAAGCCTTTGTAAGCCTTTAGCCTTTAAGCCTTTACGAGGAAAGCCTTTCATGCAGCCTTTAGCCTTTAGCCTTTGAGCCTTTCCAGCCTTTCAGCCTTTCAGCCTTTAGCCTTTAGCCTTTAGCCTTTTAGCCTTTATGAGCCTTTATAGCCTTTAGCCTTTTCACCAGCCTTTCCAGATGCACAAGCCTTTCAGCCTTTAGCCTTTCGAGCCTTTGGCTTATAGCCTTTCATCAGCCTTTCTAGCCTTTTAGCCTTTAGCCTTTAGCCTTTTCTAGCCTTTCAGCCTTTAGCCTTTTCGAAGCCTTTAGCCTTTTTAGCCTTTAGCTCAGCCTTTAGCCTTTATCTAACAGCCTTTAGCCTTTAGCCTTTAAAGCCTTTATGTCCAATTCTAACAGCCTTTAGCCTTTAAAGCCTTTGCAGCCTTTGAGCCTTTTAGCCTTTGAAGCCTTTAGCCTTTGTCAGCCTTTCCAGCCTTTTAGCCTTTAGCAGCCTTTAGTACGCCAGCCTTTAGCCTTTGTATAAGCCTTTAGCCTTTAGCCTTTCCACTAGCCTTTAGCCTTTAGAGGAGCGATAGCCTTTCAGCCTTTAGAAAGCCTTTGTTGCTGCTAGCCTTTGGGTTCTCAGCCTTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTTGTAGCCTTTTACATAGGATTGATTCAAAAGCCTTTTTGAGCCTTTCTGCATTAGCCTTTTCCTCTAGCCTTTAGCCTTTCGCAGCCTTTAGCCTTTTAGAGCCTTTAGATAGCCTTTCGCGACAGCCTTTTGTTTAGCCTTTAGCCTTTGTTAGCCTTTGAGCCTTTGAGCCTTTTAGCCTTTCCTAGCCTTTCAGCCTTTCCAAAGCCTTTGACAGGGTGTAGCCTTTCTAGCCTTTTTAGCCTTTAGCCTTTAAACTTAAGCCTTTTTAGCCTTTAGCCTTTCAACCCAGCCTTTAGCCTTTTAAGCCTTTAGCCTTTAGCCTTTTTAGAAGCCTTTTAGCCTTTAGCCTTTGGAGCCTTTCAGATCTCAGCCTTTTCGAGCCTTTTAGCCTTTTCAGAAAAGTAGCCTTTTTAGCAGCCTTTTAAAGCCTTTGGAGCCTTTAGCCTTTAGCCTTTGTAGCCTTTTCCCAAAAGCCTTTACAGCCTTTGTGAGCCTTTTAGTTCGTTTGAGCCTTTCCAGCCTTTCAGCCTTTAGCCTTTATAGCCTTTTGCGAGAAGCCTTTAAGCCTTTAGCCTTTTGACGTTCTAGAGCCTTTGGAGCCTTTCACGCGAGCCTTTCAAGCCTTTGACTCCGCAGCCTTTTCGCGACCAGCCTTTGCCGTGCCAGCCTTTAGCCTTTCAACACAGCCTTTAGCCTTTGGGCCGCAGAGCCTTTGAGTAGCCTTTAGCCTTTGACAGCCTTTAGCCTTTCTAGCCTTTGCAGCCTTTGTCTAGGTAGCCTTTAGCCTTTAGCCTTTCTAGCCTTTTAGCCTTTAGCCTTTTGAGCCTTTTGGAAGCCTTTCAGCCTTTAGCCTTTCGCGAGCCTTTGAGCCTTTACCCAGCCTTTACGGAGCCTTTAGCCTTTCCCATAGCCTTTAGCCTTTCCAGCCTTTAGCCTTTTAGCCTTTCAAATCTAAGCCTTTCGCATATATGGTAGCCTTTAGCCTTTAGCCTTTATGGTCCTTCAGTTTGAGCCTTTTAGAGCCTTTAAAGGAGCCTTTGTAAGACGAAGGTAGCCTTTAGCCTTTGCCAGCCTTTTTAGCCTTTAGCCTTTAAAAAGCCTTTGAGCCTTTAGCCTTTAGCCTTTGAGCCTTTAGCCTTTTCTCCTAGCCTTTCATAGCCTTTGAGCCTTTAGCCTTTTAGCCTTTTAGCCTTTAGCCTTTAGCCTTTGGAGGTCAGCCTTTATGTTAAAGCCTTTAGTTCCCAGCCTTTCAGCCTTTAGCCTTTAGCCTTTGAGCCTTTCAGCCTTTTAGCCTTTCAGCCTTTCAGCCTTTGAAGCCTTTTGTAGCCTTTGCCCGAGCCTTTAGCCTTTAGCCTTTCCCAACCCTGATCCGTAGCCTTTGGGCTGATCCTGAGCCTTTTCAGCCTTTAAGCCTTTAGCCTTTAGCCTTTGAGAAGCCTTTAGCCTTTCAGCCTTTAACAGCCTTTAAGCCTTTATAGCCTTTAGCCAGCCTTTGCAGCCTTTCAGTAGCCTTTAGCCTTTAGCCTTTCTAGCCTTTCTTGGAGCCTTTCCCAGCCTTTAAGAGCCTTTAGCCTTTTAGCCTTTCAGCCTTTAGCCTTTTCGTAGCCTTTGACCATTGTCAGCCTTTCTACTGAGCCTTTCATAGCCTTTTTTAGCCTTTCTAGCAGCCTTTGGAGCCTTTAGAAGAGCCTTTAGCCTTTTAAGCCTTTGAGCCTTTAACACAAGCCTTTATCTGGGCCGCGAGCCTTTTCAACCTAACTACAGCCTTTCTAAGCCTTTAGCCTTTAGCCTTTCAGCCTTTTAGCCTTTACCGAGCCTTTGCGGGAAGCCTTTAAAGAGCCTTTAGAAAAAGCCTTTGGGATAGCCTTTCCAGCCTTTCCAGCCTTTTTAGCCTTTTCCTCAAGATTTAGCCTTTGATGAAGCCTTTGAGCCTTTAGCCTTTCATTGAGCCTTTTAAGCCTTTCAGCCTTTTCTCATCAGCCTTTCACAGCCTTTCTACAGCCTTTAGCCTTTAGCCTTTGGAGCCTTTTCGCCCCGAGCCTTTAGCCTTTAGCCTTTTAGCCTTTCAGCCTTTGTAGCCTTTAGAGCCTTTGCTTAGCCTTTAGCCTTTAGTAGCCTTTAGATAGCCTTTTCTGGGAGCCTTTACAGCCTTTAGCCTTTAGCCTTTAGCCTTTTAAAGCCTTTCCCCAAAGCCTTTGTTGAGCCTTTAGCCTTTACAGTCTAGCCTTTAGCCTTTCAAGCCTTTACCTTAGCCTTTGGCAGCCTTTCTAGCCTTTAGCCTTTTCAGCCTTTAGCCTTTAAGCCTTTAGCCTTTTCGAGCCTTTGAGCCTTTAAGCCTTTATAAAAAGCCTTTAGCCTTTAAGCCTTTACCAGCCTTTAGCCTTTCAGCCTTTTATCGGAAAGCCTTTAAGCCTTTTAGCCTTTCAGCCTTTGAGCCTTTCAGCCTTTAGCCTTTGGCAAAGCCTTTTTGCAGCCTTTGGAAGCCTTTAGCCTTTTTCAAGCCTTTCAGCCTTTAGCCTTTGCACGTATTAGGAAGCCTTTTACTCTAAGCCTTTATCAGCCTTTAGCCTTTAGCCTTTAAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTAGCCTTTACGGTCAGCCTTTGGTAGCCTTTTCAGCCTTTAAGCCTTTAAGCCTTTGAGCCTTTAGCCTTTAGCCTTTGAGCCTTTAAGAGCCTTTCAGCCTTTTTTAGCCTTTTAGCCTTTGAGCCTTTCCTAGCCTTTCAAGCCTTTGAGCCTTTCGAAGCCTTTTAGCCTTTAGCCTTTAGCCTTTATGGAGCCTTTAGCCTTTAGCGGAGCCTTTGAGCCTTTACAGAGCCTTTAGCCTTTAGCCTTTTAAGCCTTTTGCAGCCTTTCAAAGAGCCTTTAGCCTTTACGGAGCCTTTAGCCTTTAAGCCTTTCTCACTAGCCTTTTTAGCCTTTGAGCCTTTATGACGAAGCCTTTAGCCTTTTGTCGTGACCTGAGCCTTTAGCCTTTACAGCCTTTCAGCCTTTAGCCTTTCTTAAAAGCCTTTTAGCCTTTTTGAGCCTTTACAGCCTTTCGAGCCTTTGAGCCTTTCCCAGCCTTTGAAGCCTTTTGGACAGAGCCTTTGCTAGCCTTTAGCCTTTTAGCCTTTAGCCTTTAGCCTTTACTTAGCCTTTTAGCCTTTATGGATAGCCTTTAGCCTTTGAGAGCCTTTGCCTAGCCTTTGAAGCCTTTTTAGCCTTTAACGAGCCTTTAGCCTTTAGCCTTTAGCCTTTAAGCCTTTAGCCTTTCGAGCCTTTCTCAGCCTTTGTAGCCTTTAGCCTTTAGAGCAGCCTTTAGCCTTTCCAGCCTTTAGCCTTTTCAGCCTTTAGCCTTTCAGCCTTTGCCCCGAGCACGTAGCCTTTACAGCCTTTAGCCTTTAGCCTTTTAGCCTTTACAGCCTTTTGAGCCTTTAGCCTTTGAAAGCCTTTTGAAGAGCCTTTCAGCCTTTCTTACTAGCCTTTGCAGCCTTTTAGCCTTTCCGAGCCTTTGATAGCCTTTGTCGGTAAGCCTTTGTAGAGCCTTTAGCCTTTAAGCCTTTGGTAAAGAGCCTTTTCAACAGCCTTTCGGAGCCTTTCGCTACAAGCCTTTTGGCCTAGCCTTTAGCCTTTCAGCCTTTCAAGAGCCTTTAGCCTTTCGCAGCCTTTATAGCCTTTCAGCCTTTCAGCCTTTAGCCTTTAGAGCCTTTGAGCCTTTCGTTATCTAAGCCTTTACTCCATAGCCTTTGAGCCTTTAGCCTTTGTCAGTCGAGCCTTTGTTCTTGAGCCTTTAGCCTTTGCAGCCTTTAGCCTTTTGTTTGTGGAGCCTTTAGCCTTTGAATACAGCCTTTAGCCTTTAGCCTTTAGCCTTTCTAGCCTTTCAGCAGCCTTTGTAGCCTTTGAACCAGCCTTTAGCCTTTTAGCCTTTTCCTTAGCCTTTCCAGCCTTTTAGTGAGCCTTTAGCCTTTGCACCAGCCTTTAGCCTTTAGCCTTTCAGCCTTTAGCCTTTCGAGCCTTTTAGCCTTTGAACAGCCTTTTGAGCCTTTGACGATATGAGCCTTTAGCCTTTTGTAGCCTTTTTTAGCCTTTGAACAGCCTTTGGAGTCAAGCCTTTACGCAGCCTTTCCAGCCTTTCAGCCTTTAGCCTTTGGTCAGCCTTTTCAGAGCCTTTGCGGTTAGCCTTTGAATAGCCTTTAAAGCCTTTCTCAGCCTTTGTAAGCCTTTAGCCTTTTAGCCTTTGTGAGCCTTTCAGCCTTTCCGAGCCTTTAGCCTTTGCCTACGGAAGCCTTTAGCCTTTGCTATCAGCTTGAGCCTTTTAGCCTTTAGTAGCAGCCTTTTAGCCTTTTAGCCTTTCAGCCTTTCTCTAGCCTTTAGCCTTTATCCGAGCCTTTACCAGCCTTTGAGCCTTTAGCCTTTATAGCCTTTATACGTAGCTAGCCTTTAGCCTTTAGAGCCTTTACCCTGTACCAGCCTTTAAGCCTTTCTCGTGAAGCCTTTAGCCTTTGAGCCTTTCGAGCCTTTAGCCTTTAGCCTTTAAGCCTTTTTGTGTGAGCCTTTAGCCTTTGGGGAGCCTTTAGCCTTTCAGCCTTTTAGCCTTTTCAAGCCTTTAGCCTTTAGCCTTTTGAGCCTTTAAAGCCTTTAGCCTTTAGGTAGCAAGCCTTTCGTTATAGCCTTTTATAAGCCTTTTTTAATGAGCCTTTAGCCTTTAGCCTTTGAGCAGCCTTTAGCCTTTAGTAGCCTTTTGATATTAGCCTTTCAGCCTTTAGCCTTTCCCCGAGCCTTTGTTAGAGCCTTTGCAGCCTTTGGAGCCTTTAGCCTTTCGGAGCCTTTAGCCTTTGGGACAGCCTTTAGCCTTTAGCCTTTGAAGCCTTTTGCAGCCTTTAAGATAGCCTTTGAGCCTTTTCAGCCTTTACAGCCTTTAAGCCTTTAGCCTTTGAGCCTTTGAGCCTTTTGAGCCTTTTAGCCTTTGTTGCAGCCTTTAGCCTTTAGCCTTTTAGCCTTTAGCCTTTAGCCTTTGAGCCTTTGAGCCTTTTAGCCTTTAGCCTTTGAGCCTTTTGGACAGCCTTTCTGAGCCTTTCGTAGCCTTTACCGCAAGCCTTTATAGCCTTTGAAGAGGAGCCTTTATAGCCTTTCAGAAGCCTTTTAAGCCTTTTCGCAGCCTTTTATCAGCCTTTAGCCTTTAGCCTTTTAGCCTTTCAGCCTTTAGCCTTTACAAGCCTTTAGCCTTTAGCCTTTATCAAGCCTTTCTAGCCTTTGAGCCTTTGTGAGCCTTTGTGTCAGCCTTTCAAGCCTTTTTAAGTACAGCCTTTACTCAGCCTTTATAGCCTTTGTCGTAAGCCTTTAGCCTTTAGCCTTTGAAAAGCCTTTACGCACAGACAAGTAGCCTTTCAGCCTTTAAGCCTTTGAGTATGTCCTTGAGCCTTTAAAAGAGCCTTTGGTAGCCTTTAGCCTTTAGCCTTTTATAGCCTTTAAGCCTTTAAGCCTTT"

print patternCount(Text, Pattern)