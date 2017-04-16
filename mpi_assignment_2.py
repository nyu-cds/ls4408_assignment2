'''
Liwei Song
04/16/2017
parallel programming1 assignment10-part2
This program are made of 2 parts.
Rank 1 generates a number, ande send to Rank2
When n>=2, it sends number*rank to n+1.
When n is the last process, it will send number*rank to 1.


'''

import numpy
from mpi4py import MPI
import sys
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


ranNum = numpy.zeros(1)

#when rank is 0, it will prompt user to user an valid interger
if rank == 0:
    if rank==size-1:
        print('Should have more than one process')
        sys.exit(2)
    while (True):
        input_int = input('Please enter an valid interger smaller than 100:')
        try: 
            ranNum[0]=int(input_int)
            if ranNum[0]<100:
                break
            else:
                continue
        except ValueError:
            continue
    comm.Send(ranNum, dest=1)
    comm.Recv(ranNum, source=size-1)
    #receieve from the last rank
    print('Process 1 receieve a number: ' + str(int(ranNum[0])))

#send buffer number to rank+1
if rank>0:
    comm.Recv(ranNum, source=rank-1)
    ranNum=ranNum*rank
    if rank<size-1:
        comm.Send(ranNum, dest=rank+1)
    else:
        comm.Send(ranNum, dest=0)
        

    

        
        

