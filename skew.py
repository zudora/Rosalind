#CATGGGCATCGGCCATACGCC
#Give all values of Skew-sub-i (GAGCCACCGCGATA) for i ranging from 0 to 14.
#    0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

# We can compute Skewi+1(Genome) from Skewi(Genome) according to the nucleotide in position i of Genome. 
#   If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1
#   if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1
#   otherwise, Skewi+1(Genome) = Skewi(Genome).

def skew(genome, irange):
    skew_list = []
    for i in range(0, irange):
        nuc = genome[i]
        if nuc == "G":
            pass
        elif nuc == "C":
            pass
        else:
            pass
    return skew_list


genome = "CATGGGCATCGGCCATACGCC"
irange = 14

skew_list = skew(genome, irange)

