# Needleman-Wunsch

read.py:
    Takes in folder of cdr3 files of the format: seq, chain_type, read_count, v_chains, d_chains, j_chains. 
    Compiles all the information in a dictionary where they key is the patient id (of any format) and the value
    is a list of lists of the above information. 

NW.py
    First file reads BLOSUM matrix txt file passed in. Uses Needleman-Wunsch algorithm to align two sequences and returns either a score, or a percent identity match based on the highest possible alignment score of the longer sequence of the two passed in. 

Main.py
    Given a list of interested sequences, search all patients' chains and account for number of similar chains based on chosen cutoff. 

Make sure to have cdr3 files in a seperate folder specifically called 'cdr3'. 

This can also be utilized for more traditional cases where only 2 sequences need to be compared. 