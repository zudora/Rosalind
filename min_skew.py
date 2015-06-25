with open ("dataset_7_6.txt", "r") as myfile:
    data=myfile.read()

def min_skew(genome):
    skew_i = 0
    min_skew = 1000000
    min_list = []
    for i in range(0, len(genome)):        
        nuc = genome[i]
        if nuc == "G":
            skew_i += 1
        elif nuc == "C":
            skew_i -= 1
        else:
            pass
        if skew_i == min_skew:
             min_list.append(i + 1)
        elif skew_i < min_skew:
            min_list = [i + 1]
            min_skew = skew_i
    return min_list

genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
print data[0:10]
print data[len(data)- 11:len(data)]

min_list = min_skew(data)

print min_list