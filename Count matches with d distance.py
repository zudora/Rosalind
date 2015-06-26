from hamming_dist import find_hamming_dist as ham

def find_count(text, pattern, dist):
    count = 0
    patt_len = len(pattern)

    for i in range(0, len(text) - patt_len + 1):
        test_patt = text[i:i+patt_len]
        if ham(pattern, test_patt) <= dist:
            count += 1

    return count

text = "AACAAGCTGATAAACATTTAAAGAG"
pattern = "AAAAA"
dist = 2

test_count = find_count(text, pattern, dist)
print "Count = ", test_count