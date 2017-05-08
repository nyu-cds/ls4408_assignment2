'''
Liwei Song
05/07/2017
The code is modified based on wordcount_spark.py provided in the course website.
There are 17355 distinct words
'''


from pyspark import SparkContext
from operator import add # Required for reduceByKey
import re

# get separate words
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	sc = SparkContext("local", "wordcount")
	text = sc.textFile('pg2701.txt')
	words = text.flatMap(splitter)
	words_mapped = words.map(lambda x: (x,1))
	sorted_map = words_mapped.sortByKey()
	#use distinct method to get distinct numbers
	counts = sorted_map.distinct()
	#get counts for distinct numbers
	counts = counts.count()
	print('Number of Distict Word: '+str(counts))

	#I searched for  the distinct method at http://stackoverflow.com/questions/27987298/pyspark-distinct-count-on-a-csv-file