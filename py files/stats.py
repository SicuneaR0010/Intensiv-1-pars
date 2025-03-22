import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('cleaned_11K.csv', index_col=0)
# list = ["price","year_of_construction","floor","floors_count","rooms_count"]
# for obj in list:
#     df[obj] = df[obj].fillna(0)
#     df[obj] = df[obj].astype(int)

df['year_of_construction'] = df['year_of_construction'].replace(0,np.nan)
df.to_csv('cleaned_1_11K.csv')

# print(df.dtypes)
# # del df['phone']
# df.to_csv('cleaned_11K.csv')

# df['year_of_construction'] = df['year_of_construction'].fillna(-1)
# df['year_of_construction'] = df['year_of_construction'].astype(int)
# df['year_of_construction'].value_counts().to_csv('years_count.csv')



# year_mode_value = df['year_of_construction'].mode()[0]
# df['year_of_construction'] = df['year_of_construction'].fillna(year_mode_value)



# dash = pd.read_csv('years_count.csv')
# dash.sort_values(["year_of_construction"], axis=0, ascending=[False], inplace=True)

# plot = sns.barplot(x='year_of_construction', y='count', data=dash, palette='dark:pink', orient='v')
# plot.set_xticklabels(plot.get_xticklabels(), rotation=90, ha='right')
# sns.despine(left=True, bottom=True)

# plt.show()



# df = pd.read_csv('cleaned_11K.csv', index_col=0)

# print(df['year_of_construction'].value_counts())



# df['living_meters'] = pd.to_numeric(
#     df['living_meters'].str.replace(',', '.').apply(lambda x: x[:-3] if pd.notna(x) else np.nan),
#     errors='coerce'
# ).astype('float64')
# df['kitchen_meters'] = pd.to_numeric(
#     df['kitchen_meters'].str.replace(',', '.').apply(lambda x: x[:-3] if pd.notna(x) else np.nan),
#     errors='coerce'
# ).astype('float64')