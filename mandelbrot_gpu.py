# 
# A CUDA version to calculate the Mandelbrot set
'''
Liwei Song
04/30/2017
'''
#
from numba import cuda
import numpy as np
from pylab import imshow, show
import math

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
    '''
    The whole image is divided into different blocks with number of x_threads*y_threads, and each block is assigned a thread.
    Each block is made by a combination of x_start point/y_end point and y_start point/y_end point.
    Then, each block is plotted by running compute_mandel in each thread, which is unique in each block. 
    
    
    '''
    ### YOUR CODE HERE
    #get absolute position of  a thread
    y, x = cuda.grid(2)
    #get the threads in x,y directions
    x_threads = cuda.blockDim.y * cuda.gridDim.y
    y_threads = cuda.blockDim.x * cuda.gridDim.x
    
    height = image.shape[0]
    width = image.shape[1]
    
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    
    #calculate how many points should be calculated in each thread in x/y direction
    x_per_thread=int(math.ceil(width/x_threads))
    y_per_thread=int(math.ceil(height/y_threads))
    
    #find start point and end point for each thread
    start_x=x*x_per_thread
    start_y=y*y_per_thread
    end_x=(x+1)*x_per_thread
    end_y=(y+1)*y_per_thread
    #make plot in each thread
    for x_i in range(start_x,end_x):
        if x_i<=width:
            real = min_x + x_i * pixel_size_x
        #break before reaching to the width limit
        else:
            break
        for y_i in range(start_y,end_y):
            #break before reaching to the height limit
            if y_i<=height:
                imag = min_y + y_i * pixel_size_y
                image[y_i, x_i] = mandel(real, imag, iters)
            else:
                break
    

if __name__ == '__main__':
    image = np.zeros((1024, 1536), dtype = np.uint8)
    blockdim = (32, 8)
    griddim = (32, 16)

    image_global_mem = cuda.to_device(image)
    compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
    image = image_global_mem.copy_to_host()
    imshow(image)
    show()