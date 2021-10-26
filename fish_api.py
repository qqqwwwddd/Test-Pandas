import numpy as np
import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt

bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
#print(bream_length)
bream_weight= pd.read_csv("bream_weight.csv").to_numpy().flatten()
#print(bream_weight)
smelt_length = pd.read_csv("smelt_length.csv").to_numpy().flatten()
#print(smelt_length)
smelt_weight = pd.read_csv("smelt_weight.csv").to_numpy().flatten()
#print(smelt_weight)

plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length,smelt_weight)
plt.show()