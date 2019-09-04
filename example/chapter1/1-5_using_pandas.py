# 1-5_using_pandas.py
import pandas as pd
def solution(df):
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
	# Write your code here.
	df['avg'] = (df['math']+df['science'])/2
	df['avg_high'] = df['avg']>2.5
	return df
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 

data = {"name": ["Moon", "Choi", "Song", "Jang"],
           "math": [4.0, 2.1, 4.7, 2.6],
           "science": [3.8, 1.7, 0.7, 2.4]}
df = pd.DataFrame(data, columns=["name", "math", "science"])
print(solution(df))