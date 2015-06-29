
def find_hamming_dist(string1, string2):
# compute Hamming distance. Uses two strings of same length as input    
    dist = 0
    str_len = len(string1)

    for i in range(0, str_len):
        if string1[i] != string2[i]:
            dist += 1

    return dist

string1 = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
string2 = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
dist = find_hamming_dist(string1, string2)
print dist

def approx_match(pattern, text, max_dist):
    #All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    pos_list = []
    patt_len = len(pattern)

    for i in range(0, len(text) - patt_len + 1):
        test_patt = text[i:i+patt_len]
        
        dist = find_hamming_dist(pattern, test_patt)
        if dist <= max_dist:
            pos_list.append(i)   
            #print "match: ", test_patt, ", ", str(i)
         
    return pos_list


## Find minimum Hamming matches

