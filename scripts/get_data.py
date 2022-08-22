import pandas as pd
import numpy as np
from IPython.display import Image
import warnings
warnings.filterwarnings('ignore')

pd.set_option('max_column', None)
db = pd.read_csv('/content/drive/Shareddrives/10 Academy/Intensive training/Batch 6/Content-B6/Week-1/data/diabetic_data.csv', na_values=['?', None])
# db = pd.read_csv('<path-to-your-csv-inside-your-drive>',  na_values=['?', None])
db.head()