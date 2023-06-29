import os
from NW import *
from BLOSUM import *
# dictionary to store all information from cdr3 files
# patient numbers keys, values is a list of list of
# all other information
info_dict = {}

# method to get all information from all cdr3 files
# and store them in info_dict for later use
def path(folder):
    path = os.getcwd() + "/" + folder
    for file in sorted(os.listdir(path)):
        if(file.endswith(".cdr3")):
            file_path = path + "/" + file
            temp = file.split(".")
            info_dict[temp[0]] = None
            read(file_path, temp[0])

# Method to take infomration from cdr3 file and store
# it as the value for the patient key in info_dict
def read(file, patient):
    Seq_list = []
    Chain_type = []
    Read_count = []
    V_chains = []
    D_chains = []
    J_chains = []
    f = open(file)
    f.readline()
    lines = f.readlines()
    for line in lines:
        array = line.split(',')
        Seq_list.append(array[0])
        Chain_type.append(array[1])
        Read_count.append(array[2])
        V_chains.append(array[3])
        D_chains.append(array[4])
        J_chains.append(array[5])
        info_list = [Seq_list, Chain_type, Read_count, V_chains, D_chains, J_chains]
        info_dict[patient] = info_list