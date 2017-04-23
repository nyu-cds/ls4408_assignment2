'''
Liwei Song
04/22/2017
It first prompts user to input the size of the array, the lower bound and upper bound
by using np.random.randint(lower,higher,array_size).
Then, the array is splitted into several bins, the number of bins is equal to the size of ranks.
'''

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Split the list into several lists.
def split(all_num,size):
	all_chunks=[]
	n_min=min(all_num)
	n_max=max(all_num)
	delta=(n_max-n_min)/size
	for order in range(size):
	    chunk=[]
	    if order==0:
	        for num in all_num:
	            if num>=n_min and num<=n_min+delta:
	                chunk.append(num)
	    else:
	        for num in all_num:
	            if num>n_min+order*delta and num<=n_min+(order+1)*delta:
	                chunk.append(num)
	    all_chunks.append(chunk)
	return all_chunks

#prompts user to enter size of array, lower bound and upper bound of the array
def user_input():
	while(True):
		try:
			#size should be positive number
			array_size=10000
			input_lower=input('Please input a number for lower bound:')
			lower=float(input_lower)
			input_upper=input('Please input a number for upper bound (larger than lower bound):')
			higher=float(input_upper)
			all_num = np.random.randint(lower,higher,array_size)
			sep_array=split(all_num,size)
			break
		#the upper bound should be larger than the lower bound
		except ValueError:
			print('Not valid input array')
	return sep_array


def sort_list(sep_array):
    if rank == 0:
    	sep_array= sep_array   
    else:
        sep_array = None
	#scatter the array to differnt processes
    sep_array=comm.scatter(sep_array, root=0)

    chunk_sort=np.sort(sep_array)
    #gather the sorted array from different processes to the rank 0.
    final=comm.gather(chunk_sort,root=0)
    
    if rank==0:
    	#flatten sorted arrays from differnt processes.
        sorted_list=np.concatenate(final)

        return sorted_list

# return the sorted array
def output_sorted():
	sep_array=None
	if rank==0:
		sep_array=user_input()
	a=sort_list(sep_array)
	return(a)


if __name__=="__main__":
	s=output_sorted()
	if rank==0:
		print('Finish sorting')
    




