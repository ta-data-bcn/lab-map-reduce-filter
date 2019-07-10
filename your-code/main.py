# Import reduce from functools, numpy and pandas
import pandas as pd
from functools import reduce
import numpy as np

location = '../data/58585-0.txt'
with open(location, 'r', encoding="utf8") as f:
    prophet = f.read().split(' ')

prophet = [3,4,5,3,32,4,5,3,45,3,34,43,3,4,23,34,234,23,3,32,3,2]

print(prophet)

#print(prophet)
prophet3 = prophet
prophet2 = prophet[:575]
print(prophet2)
# your code here
list_to_remove = []


def remove(word,index):
    if index < 576:
        list_to_remove.append(word)
        prophet3.remove(word)


list(map(remove,prophet,range(len(prophet))))

print(prophet)
#print(len(prophet))
#print(list_to_remove)
print(prophet3)
