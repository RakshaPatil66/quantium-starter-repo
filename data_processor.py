import pandas as pd
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

combined = pd.concat([df0, df1, df2])
pink_morsel = combined[combined['product'] == 'pink morsel'].copy()

print(pink_morsel.head())

pink_morsel['price'] = pink_morsel['price'].replace('[\$,]','', regex=True).astype(float)
pink_morsel['sales'] = pink_morsel['price'] * pink_morsel['quantity']

final_df = pink_morsel[['sales','date','region']]
final_df.to_csv('data/formatted_pink_morsel.csv', index=False)
print("check your folder for formatted_pink_morsel.csv")
