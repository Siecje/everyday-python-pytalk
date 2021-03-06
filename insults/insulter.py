import re
import sys
import math
import random

def read_insults(filename):
	with open(filename) as f:
		columns = [[], [], []]

		for line in f:
			items = re.split('\s+', line)
			for i, col in enumerate(columns):
				col.append(items[i])

		return columns

def randomize(column):
	return column[int(math.floor(random.random() * len(column)))]

prefix = 'You are a'
if len(sys.argv) > 1:
	prefix = '%s is a' % sys.argv[1]

items = map(randomize, read_insults('insults.txt'))

if items[0].startswith(('a', 'e', 'i', 'o', 'u')):
	prefix += 'n'

phrase = ' '.join([prefix] + items)

print '%s.' % phrase
