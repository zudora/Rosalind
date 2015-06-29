from hamming_dist import find_hamming_dist as ham

def find_most_freq_kmer(text, k, d):
    #All most frequent k-mers with up to d mismatches in Text
    freq_dict = {}
    most_freq = []
    max_freq = 0
        
    for i in range(0, len(text) - k + 1):        
        # add all kmers to dictionary. Dupes don't matter since they're set to 0
        next_kmer = text[i:i+k]
        freq_dict[next_kmer] = 0
        count = len(freq_dict)
        
        if "GCACACAGAC" in freq_dict:
           print "Found first"
        if "GCGCACACAC" in freq_dict:
            print "Found second"
                              
    for i in range(0, len(text) - k + 1):
        
        test_kmer = text[i:i+k]
        
        for item in freq_dict:
            dist = ham(test_kmer, item)
            
            if dist <= d:
                if test_kmer not in freq_dict:
                    print "Wat"
                freq_dict[test_kmer] += 1
            
    for item in freq_dict:
        #print item, freq_dict[item]       
        if freq_dict[item] > max_freq:
            max_freq = freq_dict[item]

    for item in freq_dict:        
        if freq_dict[item] == max_freq:
            most_freq.append(item)
    #print max_freq
    return most_freq

#text = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
#leng = len(text)
#new_freq_list = find_most_freq_kmer(text, 10, 2)

def gen_all_kmers(k):
    kmer_list = []
    partial_list = []
    sym_list = ["A", "B", "C", "D"]

    for i in range(0, k):
        if i == 0:
            partial_list.append(sym_list[i])        
        elif i < k:
            temp_list = []
            for item in kmer_list:
                temp_string = item + sym_list[i]
                partial_list.append(temp_string)
        
        else:
            pass
        kmer_list = partial_list
    return kmer_list

listo = gen_all_kmers(3)
print listo

def count_d(pattern, text, max_dist):
    #Count of occurences of pattern with d distance
    count = 0
    patt_len = len(pattern)

    for i in range(0, len(text) - patt_len + 1):
        test_patt = text[i:i+patt_len]
        
        dist = ham(pattern, test_patt)
        if dist <= max_dist:
            count += 1 
            #print "match: ", test_patt, ", ", str(i)
         
    return count


#count1 = count_d("TGT", "CGTGACAGTGTATGGGCATCTTT", 1)
#print "count1=",count1
