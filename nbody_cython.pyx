'''
nbody_opt
Origin runtime: 109.37762977881721s
Optimaized runtime: 31.88759896794022s
Optimaized runtime in cython:7.890879561828963
R=13.861272234836322
Could reach to under 30s easily.
'''
import timeit
import cython
"""
    N-body simulation.
"""
from itertools import combinations

cdef float PI = 3.14159265358979323
cdef float SOLAR_MASS = 4 * PI * PI
cdef float DAYS_PER_YEAR = 365.24

cdef dict BODIES = {
'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

'jupiter': ([4.84143144246472090e+00,
             -1.16032004402742839e+00,
             -1.03622044471123109e-01],
            [1.66007664274403694e-03 * DAYS_PER_YEAR,
             7.69901118419740425e-03 * DAYS_PER_YEAR,
             -6.90460016972063023e-05 * DAYS_PER_YEAR],
            9.54791938424326609e-04 * SOLAR_MASS),

'saturn': ([8.34336671824457987e+00,
            4.12479856412430479e+00,
            -4.03523417114321381e-01],
           [-2.76742510726862411e-03 * DAYS_PER_YEAR,
            4.99852801234917238e-03 * DAYS_PER_YEAR,
            2.30417297573763929e-05 * DAYS_PER_YEAR],
           2.85885980666130812e-04 * SOLAR_MASS),

'uranus': ([1.28943695621391310e+01,
            -1.51111514016986312e+01,
            -2.23307578892655734e-01],
           [2.96460137564761618e-03 * DAYS_PER_YEAR,
            2.37847173959480950e-03 * DAYS_PER_YEAR,
            -2.96589568540237556e-05 * DAYS_PER_YEAR],
           4.36624404335156298e-05 * SOLAR_MASS),

'neptune': ([1.53796971148509165e+01,
             -2.59193146099879641e+01,
             1.79258772950371181e-01],
            [2.68067772490389322e-03 * DAYS_PER_YEAR,
             1.62824170038242295e-03 * DAYS_PER_YEAR,
             -9.51592254519715870e-05 * DAYS_PER_YEAR],
            5.15138902046611451e-05 * SOLAR_MASS)}
cdef list liter = list(combinations(BODIES,2))    

cpdef void advance(dict BODIES,list liter,int iterations,float dt):

    '''
        advance the system one timestep
    '''
    cdef str body1, body2, body
    cdef float x1, y1, z1, x2, y2, z2, m1, m2, m
    cdef list v1, v2
    cdef float dx, dy, dz
    cdef float compute_m
    cdef list r
    cdef float vx, vy, vz
    for _ in range(iterations):
        for body1, body2 in liter:
            ([x1, y1, z1], v1, m1) = BODIES[body1]
            ([x2, y2, z2], v2, m2) = BODIES[body2]
            (dx, dy, dz) = x1-x2, y1-y2, z1-z2
            compute_m=dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            v1[0] -= dx * (m2)*compute_m
            v1[1] -= dy * (m2)*compute_m
            v1[2] -= dz * (m2)*compute_m
            v2[0] += dx * (m1)*compute_m
            v2[1] += dy * (m1)*compute_m
            v2[2] += dz * (m1)*compute_m
               
            
        for body in BODIES.keys():
            
            (r, [vx, vy, vz], m) = BODIES[body]
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz
    
cpdef float report_energy(dict BODIES,list liter,float e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    cdef str body1, body2
    cdef float x1, y1, z1, x2, y2, z2, m1, m2, dx, dy, dz,m, vx, vy, vz
    cdef list v1, v2
    for body1, body2 in liter:
        ((x1, y1, z1), v1, m1) = BODIES[body1]
        ((x2, y2, z2), v2, m2) = BODIES[body2]
        (dx, dy, dz) = x1-x2, y1-y2, z1-z2
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5) 
   
    cdef str body
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

cpdef void offset_momentum(dict BODIES, tuple ref,float px=0.0,float py=0.0,float pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
        
    '''
    cdef list r, v
    cdef float vx, vy, vz
    cdef float m
    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


cpdef void nbody(int loops,str reference,int iterations,dict BODIES=BODIES,list liter=liter):
    
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # Set up global state
   
    offset_momentum(BODIES,BODIES[reference])

    
    for _ in range(loops):
        report_energy(BODIES,liter)
        advance(BODIES,liter,iterations,0.01)
        print(report_energy(BODIES,liter))
    
    
   


if __name__ == '__main__':   
    print(timeit.timeit(lambda:nbody(100, 'sun', 20000,BODIES,liter), number=1))