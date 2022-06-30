import numpy as np
import pandas as pd
import nltk.util
from nltk.util import ngrams as ngr

raw_data=pd.read_csv('COS.csv')
not_viable_data=raw_data[pd.isna(raw_data.iloc[:,-1])]
viable_data=raw_data[~pd.isna(raw_data.iloc[:,-1])]
row_string=str(viable_data['FIT ELEMENTS'])
import re

row_list=re.split('; |, |\*|\n',row_string)[0:-2]

words = pd.DataFrame(viable_data['FIT ELEMENTS']).stack().str.split("[^\w+]").explode().tolist()
word_counts = dict()
for i in words:
  if i != '':
    word_counts[i] = word_counts.get(i, 0) + 1

bigrams = [b for l in row_list for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
bigram_counts = dict()
for i in bigrams:
  if '' not in i:
    bigram_counts[i] = bigram_counts.get(i, 0) + 1
print('hi')