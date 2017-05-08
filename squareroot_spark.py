'''
Liwei Song
05/07/2017
fold method from https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html#fold
get average square root from 1 to 1000
'''


from pyspark import SparkContext
from operator import add
import math


if __name__ == '__main__':
	sc = SparkContext()

	nums = sc.parallelize(range(1,1001))
	#get square root of each number
	sqrt_nums = nums.map(lambda x: math.sqrt(x))
	#use fold to add up all square root
	sum_sqrt=sqrt_nums.fold(0,add)
	#get average
	avg_sqrt=sum_sqrt/(1000)
	print('the average square root of 1:1000: '+str(avg_sqrt))