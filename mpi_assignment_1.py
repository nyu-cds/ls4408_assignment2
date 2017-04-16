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