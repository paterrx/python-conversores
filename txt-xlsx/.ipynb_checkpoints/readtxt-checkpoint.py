import pandas as pd
df = pd.read_csv('input.csv')
# can replace with:
# df = pd.read_csv('input.tsv', sep='\t') for tab delimited
df.to_excel('output.xlsx', 'Sheet1')