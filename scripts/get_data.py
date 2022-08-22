import pandas as pd
import numpy as np
from IPython.display import Image
import warnings
warnings.filterwarnings('ignore')

# pd.set_option('max_column', None)
db = pd.read_excel(r'~\\Documents\\projects\\10academy\\week1\\TellCoAnalysis\\data\\TellCo_financial_data.xlsx', na_values=['?', None])
print(db.head())