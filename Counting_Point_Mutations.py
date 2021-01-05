# Evolution as a Sequence of Mistakes

# Problem

# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
# is the number of corresponding symbols that differ in s and t. See Figure 2.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t)dH(s,t).

# Sample Dataset

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output

# 7

# Solution

def Hamming(s,t):
    count = 0
    i = 0
    for letter in s:
        if i < len(s):
            if s[i] != t[i]:
                count = count + 1
                i = i + 1
            else:
                count = count
                i = i + 1
        else:
            return

    print(count)


s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'

Hamming(s,t)
