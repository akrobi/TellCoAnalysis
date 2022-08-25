import pandas as pd
import numpy as np
from IPython.display import Image
import warnings
warnings.filterwarnings('ignore')

db = pd.read_excel(r'~\\Documents\\projects\\10academy\\week1\\TellCoAnalysis\\data\\first500valuesTellCo.xlsx', na_values=['?', None])
# print(db.head())

# column names. works
# print(db.columns.tolist())

# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The TellCo dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

percent_missing(db)

# to see which columns have missing values
print(db.isna().sum())

# # to see which columns* have large missing values
# large_missing = db[db[1] > 5].index.to_list()
# print(large_missing)

# identifying the top 10 handsets used by the customers
handsets = []
for handset in db:
    handsets.append(db['Handset Type'])
print(handsets)

# for handset in handsets:
