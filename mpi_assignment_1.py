'''
Liwei Song
04/16/2017
This program create n processes
If rank is even, it will print Hello
If rank is odd, it will print Goodbye
'''


from mpi4py import MPI

comm = MPI.COMM_WORLD
#create an com_world object
rank = comm.Get_rank()
#get the rank of the process

if rank%2==0:
        print('Hello from process '+str(rank))
#print hello if even
if rank%2 ==1:
        print('Goodbye from process '+str(rank))
#print goodbye if odd