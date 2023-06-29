import csv
from read import *
from NW import *
# important COVID-19 sequences we are searching for
##################################
# CHANGE IF USING FOR OTHER REASON
##################################
sequences = ['CQQYGSSPR', 'CSSYEGSNNFV', 'CQQLNSYPPY', 
             'CQQYYSTPY', 'CQQSYSTPR', 'CQQYGTTPR', 'CSSYTSSSTSV', 
             'CCYAGSSTL', 'CSSYTSSSTR', 'CCSYAGSSTW', 'CSSYAGSNNL', 
             'CSSYAGSNNL', 'CQQYNSYPY', 'CQQYNSYPW', 'CQQHDSTL', 
             'CQQYNSYPY', 'CQQYDNLPL', 'CQQYYSTPY', 'CQQSYSTLAL', 
             'CQQSYVSPTY', 'CQSYDSSNHVV']


def compare():
    keys = info_dict.keys()
    table = np.zeros((len(keys), len(sequences)))
    for i in range(len(sequences)):
        seq = sequences[i]
        for j in range(len(keys)):
            temp = list(keys)
            k = temp[j]
            for chain in info_dict[k][0]:
                table[j][i] = table[j][i] + nw(seq, chain, gap_penalty=-4, finding_max=True, cutoff=0.70)
    return table

def makeCSV(results):
    with open('results.csv', 'w') as f:
        writer = csv.writer(f)
        header = sequences.insert("", 0)
        writer.writerow(header)
        keys = list(info_dict.keys())
        for i in range(len(results)):
            input = results[i]
            input.insert(keys[i], 0)
            writer.writerow(input)


def main():
    path("cdr3")
    blosum_dict("BLOSUM62.txt")
    #results = compare()
    #print(results)


    ########################
    # IMPORTANT
    # If want to simply compare two sequences use below and comment out line x
    # nw(seq1, seq2)
    ########################

if __name__=="__main__":
    main()