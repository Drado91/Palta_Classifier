import numpy as np
import pandas as pd
import nltk.util
from nltk.util import ngrams as ngr
import re

#Data import and split:
raw_data=pd.read_csv('COS.csv')
not_viable_data=raw_data[pd.isna(raw_data.iloc[:,-1])]
viable_data=raw_data[~pd.isna(raw_data.iloc[:,-1])]
def remove_one_appearance(dict):
  dict = {key: val for key, val in dict.items() if val != 1}
  return dict

def bigrams_and_singles_dict_creator(dataframe,column_label):
  row_string = str(dataframe[column_label])
  row_list = re.split('; |, |\*|\n', row_string)[0:-2]
  words = pd.DataFrame(dataframe[column_label]).stack().str.split("[^\w+]").explode().tolist()
  word_counts = dict()
  for i in words:
    if i != '':
      word_counts[i] = word_counts.get(i, 0) + 1
  bigrams = [b for l in row_list for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
  bigram_counts = dict()
  for i in bigrams:
    if '' not in i:
      bigram_counts[i] = bigram_counts.get(i, 0) + 1
  return remove_one_appearance(bigram_counts),remove_one_appearance(word_counts)

#Create single and bigrams dictionaries:
a,b=bigrams_and_singles_dict_creator(viable_data,'FIT ELEMENTS')
c,d=bigrams_and_singles_dict_creator(viable_data,'DEXTERITY ELEMENTS')
e,f=bigrams_and_singles_dict_creator(viable_data,'SENSORY ELEMENTS')
h,i=bigrams_and_singles_dict_creator(not_viable_data,'FIT ELEMENTS')
j,k=bigrams_and_singles_dict_creator(not_viable_data,'DEXTERITY ELEMENTS')
l,m=bigrams_and_singles_dict_creator(not_viable_data,'SENSORY ELEMENTS')

###Find words that exist only in one fit dictionaries
a=set(a)-set(h)
b=set(b)-set(i)
c=set(c)-set(j)
d=set(d)-set(k)
e=set(e)-set(l)
f=set(f)-set(m)
h=set(h)-set(a)
i=set(i)-set(b)
j=set(j)-set(c)
k=set(k)-set(d)
l=set(l)-set(e)
m=set(m)-set(f)
print('hi')