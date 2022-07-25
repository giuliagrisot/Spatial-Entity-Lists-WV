# imports
import csv
import json
from gensim.models import FastText
from gensim.test.utils import datapath
from gensim.test.utils import get_tmpfile
from collections import Counter

model = FastText.load_fasttext_format ("corpus-de.bin")


with open("rural.txt", encoding="UTF-8") as f:
    rural_items = [line.rstrip() for line in f]

data = {}
for item in rural_items:
    data[item] = model.wv.most_similar(item)

with open('DErural-items.json', 'w') as outfile:
    json.dump(data, outfile)

with open ('DErural-items.tsv', 'w') as outcsv:
	for keyword, similar in sorted (data.items (), key = lambda x: x[0]):
		line = [keyword]
		for simword, distance in similar:
			line += [simword, str (distance)]
		outcsv.write ('\t'.join (line) + '\n')

# list of frequencies

c = Counter()
for data_item in data.values():
	for x in data_item:
		c[x[0]] += 1
		
with open ('rural-vectors-frequencies.tsv', 'w') as outcsv:
	for keyword, number in c.most_common():
		outcsv.write (f'{keyword}\t{number}\n')
