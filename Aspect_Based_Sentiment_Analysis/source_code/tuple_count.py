# -*- coding: utf-8 -*-
"""tuple_count.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oLOaZPyxPviR_h5m2zB9uWWUfNj2t3xj
"""

import os
from google.colab import drive
drive.mount('/content/drive')
os.chdir('/content/drive/My Drive')

from collections import Counter
import pandas as pd
import csv
import pickle

def format_input(input_string):
    try:
        formatted_input = eval(input_string)
        if isinstance(formatted_input, list):
            return formatted_input
        else:
            raise ValueError("Input is not a list")
    except Exception as e:
        print("Error formatting input:", e)
        return None


def element_count(txt):
  left_words_counter = Counter()
  txt = format_input(txt)

  for item in txt:
    left_word = item[0]
    print(left_word)
    if isinstance(left_word, str):
       left_words_counter[left_word] += 1
       left_word_counts = element_count(txt)
       print("Left word counts:", left_word_counts)
    return left_words_counter


# Load dataset
dataset = pd.read_csv('output_2023.csv', encoding="utf-8").iloc[0:2, 7]

aspect_dict = {}
for i in range(dataset.shape[0]):
  tmp_finalcluster = dataset.iloc[i]
  print(tmp_finalcluster)
  tmp_finalcluster = format_input(tmp_finalcluster)
  for item in tmp_finalcluster:
    left_word = item[0]
    print(left_word)
    if left_word in aspect_dict.keys():
      aspect_dict[left_word] += 1
    else:
      aspect_dict[left_word] = 1

print(aspect_dict)
with open('element_count_output.pkl', 'wb') as f:
  pickle.dump(aspect_dict, f)

