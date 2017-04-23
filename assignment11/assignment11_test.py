'''
Liwei Song
04/22/2017
This file test the functions in assignment11
'''

import unittest
from assignment11 import *
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
        split_num=None
        if rank==0:
            all_num = np.sort(np.random.randint(10000,size=size*10))
            split_num = np.split(all_num, size)
            #split_num[0]=np.random.shuffle(split_num[0])
        sorted=sort_list(split_num)
        if rank==0:
            self.assertEqual(list(sorted),list(np.sort(all_num)))
        else:
            self.assertEqual(None,sorted)


if __name__ == '__main__':
    unittest.main()
    