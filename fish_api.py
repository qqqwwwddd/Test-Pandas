import numpy as np
import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt

#1. 불러오기
bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
#print(bream_length)
bream_weight= pd.read_csv("bream_weight.csv").to_numpy().flatten()
#print(bream_weight)
smelt_length = pd.read_csv("smelt_length.csv").to_numpy().flatten()
#print(smelt_length)
smelt_weight = pd.read_csv("smelt_weight.csv").to_numpy().flatten()
#print(smelt_weight)

#2. bream_data, smelt_data 시각화
plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length,smelt_weight)
# plt.show()

#3. fish_length, fish_weight 만들기
fish_length = np.concatenate((bream_length, smelt_length))
# print(fish_length.shape)
fish_weight = np.concatenate((bream_weight, smelt_weight))
# print(fish_weight.shape)
fish_data = np.column_stack((fish_length, fish_weight)) 
#print(fish_data)

#4. 타겟 데이터 만들기
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
#print(fish_target)

#5. 데이터 셔플하기
indexes = np.arange(49)
np.random.shuffle(indexes)
#print(indexes)
fish_data = fish_data[indexes]
fish_target = fish_target[indexes]

#6. 훈련데이터, 검증데이터 나누기 
train_data = fish_data[:39]
train_target = fish_target[:39]
test_data = fish_data[39:]
test_target = fish_target[39:]

print(train_data)
print(train_target)
print(test_data)
print(test_target)


