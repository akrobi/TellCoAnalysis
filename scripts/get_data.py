import pandas as pd
import numpy as np
from IPython.display import Image
import warnings
warnings.filterwarnings('ignore')

# pd.set_option('max_column', None)
db = pd.read_excel('../data/Week1_challenge_data_source.xlsx', na_values=['?', None])
db.head()