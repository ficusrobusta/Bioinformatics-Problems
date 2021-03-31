# The Secondary and Tertiary Structures of DNA

# Problem

# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

# Sample Dataset
# AAAACCCGGT

# Sample Output
# ACCGGGTTTT

# Solution

DNA = "AAAACCCGGT"

Rev = DNA[::-1]
Rev

Rev_com = Rev.translate(str.maketrans({'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}))

print(Rev_com)


# Alternative solution

DNA = "AAAACCCGGT"

Rev = DNA[::-1]
Rev
Rev_com = Rev.translate(str.maketrans('ATGC', 'TACG'))
print(Rev_com)
