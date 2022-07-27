import pandas

with open("urban.txt", encoding="UTF-8") as f:
    urban_items = [line.rstrip() for line in f]
	
colnames = ["word", "frequency"]
data = pandas.read_csv("urban-vectors-frequencies-nopunc.tsv", sep="\t", encoding="UTF-8", names = colnames)
words = data.word.tolist()


unique_values = []
for item in words:
	if item not in urban_items:
		unique_values.append(item)

		
with open ('urban_unique.txt', 'w') as text_file:
	for word in unique_values:
		text_file.write(str(word) + '\n')
		
text_file.close()

