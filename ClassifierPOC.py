import numpy as np
import pandas as pd
import nltk.util
from nltk.util import ngrams as ngr
import re
import matplotlib.pyplot as plt
import operator

#Data import and split:
raw_data=pd.read_csv('COS.csv')
not_viable_data=raw_data[pd.isna(raw_data.iloc[:,-1])]
viable_data=raw_data[~pd.isna(raw_data.iloc[:,-1])]

def Normalize(dict):
  """Turns the counters in every element of dict2 to probabilities"""
  valsum=sum(dict.values())
  for d in list(dict.items()):
    dict[d[0]] = np.round(d[1] / valsum,2)
  return dict
def remove_one_appearance(dict):
  #Remove items from dictionary if value = 1
  dict = {key: val for key, val in dict.items() if val != 1}
  return dict
def bigrams_and_singles_dict_creator(dataframe,column_label):
  row_string = str(dataframe[column_label])
  row_list = re.split('; |, |\*|\n', row_string)[0:-2]

  # Create dictionary of words
  words = pd.DataFrame(dataframe[column_label]).stack().str.split("[^\w+]").explode().tolist()
  word_counts = dict()
  for i in words:
    if i != '':
      word_counts[i] = word_counts.get(i, 0) + 1

  # Create dictionary of bigrams
  bigrams = [b for l in row_list for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
  bigram_counts = dict()
  for i in bigrams:
    if '' not in i:
      bigram_counts[i] = bigram_counts.get(i, 0) + 1

  bigram_counts=remove_one_appearance(bigram_counts)
  word_counts= remove_one_appearance(word_counts)
  bigram_counts=Normalize(dict(sorted(bigram_counts.items(), key=operator.itemgetter(1), reverse=True)))
  word_counts = Normalize(dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)))
  return bigram_counts, word_counts
def Return_items_only_in_first_dict(dict_a, dict_b):
  # Find words that exist only in one fit dictionaries
  dict_a_copy = dict_a.copy()
  for ind in dict_a:
    if ind in dict_b:
      dict_a_copy.pop(ind)
  return dict_a_copy
def plot_dict(dict):
  plt.bar(list(dict.keys()), dict.values())
  plt.show()

#Create single and bigrams dictionaries:
fit_viable_bigrams,fit_viable_singles=                          bigrams_and_singles_dict_creator(viable_data,'FIT ELEMENTS')
dexterity_viable_bigrams,dexterity_viable_singles=              bigrams_and_singles_dict_creator(viable_data,'DEXTERITY ELEMENTS')
sensory_viable_bigrams,sensory_viable_singles=                  bigrams_and_singles_dict_creator(viable_data,'SENSORY ELEMENTS')
prodcut_viable_bigrams,prodcut_viable_singles=                  bigrams_and_singles_dict_creator(viable_data,'PRODUCT')
fit_not_viable_bigrams,fit_not_viable_singles=                  bigrams_and_singles_dict_creator(not_viable_data,'FIT ELEMENTS')
dexterity_not_viable_bigrams,dexterity_not_viable_singles=      bigrams_and_singles_dict_creator(not_viable_data,'DEXTERITY ELEMENTS')
sensory_not_viable_bigrams,sensory_not_viable_singles=          bigrams_and_singles_dict_creator(not_viable_data,'SENSORY ELEMENTS')
prodcut_not_viable_bigrams,prodcut_not_viable_singles=          bigrams_and_singles_dict_creator(not_viable_data,'PRODUCT')

fit_viable_single_dict                  =     Return_items_only_in_first_dict(fit_viable_singles,fit_not_viable_singles)
fit_not_viable_single_dict              =     Return_items_only_in_first_dict(fit_not_viable_singles,fit_viable_singles)
fit_viable_bigrams_dict                 =     Return_items_only_in_first_dict(fit_viable_bigrams,fit_not_viable_bigrams)
fit_not_viable_bigrams_dict             =     Return_items_only_in_first_dict(fit_not_viable_bigrams,fit_viable_bigrams)

dexterity_viable_single_dict            =     Return_items_only_in_first_dict(dexterity_viable_singles,dexterity_not_viable_singles)
dexterity_not_viable_single_dict        =     Return_items_only_in_first_dict(dexterity_not_viable_singles,dexterity_viable_singles)
dexterity_viable_bigrams_dict           =     Return_items_only_in_first_dict(dexterity_viable_bigrams,dexterity_not_viable_bigrams)
dexterity_not_viable_bigrams_dict       =     Return_items_only_in_first_dict(dexterity_not_viable_bigrams,dexterity_viable_bigrams)

sensory_viable_single_dict              =     Return_items_only_in_first_dict(sensory_viable_singles,sensory_not_viable_singles)
sensory_not_viable_single_dict          =     Return_items_only_in_first_dict(sensory_not_viable_singles,sensory_viable_singles)
sensory_viable_bigrams_dict             =     Return_items_only_in_first_dict(sensory_viable_bigrams,sensory_not_viable_bigrams)
sensory_not_viable_bigrams_dict         =     Return_items_only_in_first_dict(sensory_not_viable_bigrams,sensory_viable_bigrams)

prodcut_viable_single_dict              =     Return_items_only_in_first_dict(prodcut_viable_singles,prodcut_not_viable_singles)
prodcut_not_viable_single_dict          =     Return_items_only_in_first_dict(prodcut_not_viable_singles,prodcut_viable_singles)
prodcut_viable_bigrams_dict             =     Return_items_only_in_first_dict(prodcut_viable_bigrams,prodcut_not_viable_bigrams)
prodcut_not_viable_bigrams_dict         =     Return_items_only_in_first_dict(prodcut_not_viable_bigrams,prodcut_viable_bigrams)

print('hi')