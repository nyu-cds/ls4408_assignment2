'''
Liwei Song
02/26/2017
'''

import  itertools as itert
def zbits(n,k):
	#create initial set
    all_combinations=set()
    #create differenet combinations of positions of 0 in the string
    combination=itert.combinations(range(n), r=k)
    for comb in combination:
    	#create a list of ones with length of n
        one_str=list(itert.repeat('1',n))
        for one in iter(comb):
        	#replace ones with zeros
            one_str[one]='0'
        #join the list into a string
        all_combinations.add("".join(one_str))
    return all_combinations

if __name__ == '__main__':
    assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}
    assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}
    assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}