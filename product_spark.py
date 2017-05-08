'''
Liwei Song
05/07/2017
also fold method from https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html#fold
'''


from pyspark import SparkContext
from operator import mul



if __name__ == '__main__':
	sc = SparkContext()
	#use fold to get product from 1 to 1000
	nums = sc.parallelize(range(1,1001)).fold(1, mul)
	print('the product of 1:1000: '+str(nums))