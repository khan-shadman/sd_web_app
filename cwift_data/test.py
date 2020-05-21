import pandas as pd 

filePath = 'CWIFT2015_LEA1314.txt'
cwift_df = pd.read_csv(filePath, delimiter='\t')

print(cwift_df)