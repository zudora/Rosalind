#CATGGGCATCGGCCATACGCC
#Give all values of Skew-sub-i (GAGCCACCGCGATA) for i ranging from 0 to 14.

# We can compute Skewi+1(Genome) from Skewi(Genome) according to the nucleotide in position i of Genome. 
#   If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1
#   if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1
#   otherwise, Skewi+1(Genome) = Skewi(Genome).

def skew(genome, irange):
    skew_i = 0
    skew_list = [0]
    for i in range(0, len(genome)):        
        nuc = genome[i]
        if nuc == "G":
            skew_i += 1
        elif nuc == "C":
            skew_i -= 1
        else:
            pass
        skew_list.append(skew_i)        
    return skew_list


genome = "GAGCCACCGCGATA"
#   Expected
#   [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2]
#   
#   [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2]   

irange = 14

skew_list = skew(genome, irange)
print skew_list

