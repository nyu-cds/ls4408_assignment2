'''
Liwei Song
04/22/2017
This file test the functions in parallel_sorter
Run this file by using mpiexec -n x python assignment11_test.py, x is an interger higher than 0.
'''

import unittest
from parallel_sorter import *
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



'''inheritence from unittest.TestCase'''
class assignment11_Test(unittest.TestCase):
    #test if the list is split into different bins, the num of which is equal to the size of processors
    def test_initial(self):
        all_num=[0,2,3,4,5,6,7,8,9,10]
        size=2
        result_split=split(all_num,size)  
        self.assertEqual(len(result_split),size)
    # test if the array is really sorted or not
    def test_sort_list(self):
        sep_array=None
        if rank==0:
            sep_array=user_generate()
        sorted_l=sort_list(sep_array)
        if rank==0:
            #test scattered arrays are return to processor 0, and it is well sorted.
            self.assertEqual(list(sorted_l),list(np.sort(np.concatenate(sep_array))))
        else:
            self.assertEqual(None,sep_array)
        

if __name__ == '__main__':
    unittest.main()
    