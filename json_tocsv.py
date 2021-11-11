import json
import pandas as pd

json_load = json.load(open('sample_test_data.json','r'))
input_keys = list(json_load.keys())
print('list_data is = ',input_keys)
for var in input_keys:
    list_data = json_load[var]

df = pd.DataFrame(list_data)
print(df.head(2))
#df.to_csv('output.csv')



