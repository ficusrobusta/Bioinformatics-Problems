# Problem

# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

# Sample Output
# 20 12 17 21

# Solution

s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
len(s)

Method 1

count_A = s.count('A') 
count_G = s.count('G')
count_T = s.count('T')
count_C = s.count('C')
print(count_A, count_C, count_G, count_T)

Method 2

count_A = 0
count_G = 0
count_T = 0
count_C = 0

for i in s: 
    if i == 'A': 
        count_A = count_A + 1
    elif i == 'G':
        count_G = count_G + 1
    elif i == 'C': 
        count_C = count_C + 1
    else: 
        i == 'T'
        count_T = count_T + 1


print(count_A, count_C, count_G, count_T)
