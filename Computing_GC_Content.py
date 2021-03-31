
# Identifying Unknown DNA Quickly
# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# Sample Dataset
# >Rosalind_6404 
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC 
# TCCCACTAATAATTCTGAGG 
# >Rosalind_5959 
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT 
# ATATCCATTTGTCAGCAGACACGC 
# >Rosalind_0808 
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC 
# TGGGAACCTGCGGGCAGTAGGTGGAAT 

# Sample Output
# Rosalind_0808 
# 60.919540

# Solution
import re
import pandas as pd

FASTA = ">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG>Rosalind_5959CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

FASTAsplit = FASTA.split(">")

FASTA_df = pd.DataFrame(FASTAsplit, columns = ["sequence"])

FASTA_df

FASTA_df.sequence = FASTA_df.sequence.str.lstrip()
FASTA_df

FASTA_df = FASTAseries.drop([0])

FASTA_df['ID'] = FASTA_df['sequence']

FASTA_df['sequence'] = FASTA_df['sequence'].str[13:]
FASTA_df['ID'] = FASTA_df['ID'].str[:13]
FASTA_df = FASTA_df.set_index('ID')

FASTA_df["GC content"] =  FASTA_df['sequence'].str.count('[CG]') / FASTA_df["sequence"].str.len() * 100

FASTA_df["GC content"] 

High_GC = [FASTA_df["GC content"].idxmax(), FASTA_df["GC content"].max()]

High_GC
