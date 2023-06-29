import os
import numpy as np

bl = {}

# creates a 2x2 dict where can index into bl matrix using
#bl[A][A] = 4 (example)
def blosum_dict(file):
    f = open(os.getcwd() + "/BLOSUM/" + file)
    keys = f.readline().split("  ")

    #instantiate our set of keys
    keys[0] = 'A'
    for k in keys:
        bl[k] = None
    lines = f.readlines()
    key = None

    # go through txt file line by line
    for line in lines:
        temp_dict = {}
        line = line.split(" ")
        key = line[0]

        # remove all unnecessary values resulting from split
        line.remove(key)
        line.remove('\n')
        while '' in line:
            line.remove('')

        # relate values to proper keys in temp_dict
        for i in range(len(keys)):
            temp_dict[keys[i]] = line[i]   
        bl[key] = temp_dict

# NW algorithm
# Takes in 2 sequences, gap penalty, whether we should find max score 
# and similarity cutoff
# Follows NW algorithm to align sequences
def nw(seq1, seq2, gap_penalty = -4, finding_max = False, cutoff = 0.5):
    n = len(seq1)
    m = len(seq2)

    # score matrix to keep track of alignment score
    # traceback matrix to use to display alignment
    score = np.zeros((m+1, n+1))
    traceback = np.zeros((m+1, n+1))

    # Assign values to first row/column w/ gap penalties
    for i in range(0, m+1):
        score[i][0] = gap_penalty * i
    for j in range(0, n+1):
        score[0][j] = gap_penalty * j 
    
    # Fill out score matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = score[i-1][j-1] + int(bl[seq1[j-1]][seq2[i-1]])
            top = score[i-1][j] + gap_penalty
            left = score[i][j-1] + gap_penalty

            score[i][j] = max(diag, top, left)

    # Calculate the max possible score of our sequences  
    if(finding_max):
        if(n > m):
            max_score = nw(seq1, seq1, gap_penalty)
        else:
            max_score = nw(seq2, seq2, gap_penalty)
    
        # if our alignment is high enough
        # return 1 indicating sequences are similar
        if(score[m][n]/max_score >= cutoff):
            return 1
        else:
            return 0
    return score[m][n]


    

