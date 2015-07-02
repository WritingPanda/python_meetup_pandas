from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt

# The initial set of baby names and birth rates
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

# To merge these two lists together, use the zip function
BabyDataSet = zip(names, births)

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

df.to_csv('../data/births_ex.csv', index=False, header=False)
