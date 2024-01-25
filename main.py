# @Author : Cheng Huang
# @Time   : 15:15 2022/9/26
# @File   : main.py
import os
import time

from experiment.complete_result import get_complete_result
from experiment.kMeansExp import get_res_k_means
from experiment.write_result import get_res


if __name__ == '__main__':
    '''
        :parameter1 : dataset DBPEDIA or LMDB
        :parameter2 : k(number of cluster)
        :parameter3 : m(fuzzy parameter)
    '''

    ks = [3, 4, 5, 6, 7, 8, 9]
    ms = [2, 5, 9]

    # Get the result for GUESs on ESBM
    for k in ks:
        for m in ms:
            get_res("dbpedia", k, m, "transe")
            get_res("lmdb", k, m, "transe")


    # Get the result for GUESs-hard on ESBM
    for k in ks:
        for m in ms:
            get_res_k_means("dbpedia")
            get_res_k_means("lmdb")


    # Get the result for GUESs on ESBM+
    for k in ks:
        for m in ms:
            get_complete_result("dbpedia", k, m, "transe")
            get_complete_result("lmdb", k, m, "transe")


