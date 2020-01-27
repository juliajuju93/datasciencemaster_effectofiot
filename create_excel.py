import os
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize

img_folder_path = 'C:/Masterarbeit/No_Score/'
path = img_folder_path
files = []
datatrips = []
for r, d, f in os.walk(path):
    for file in f:
        
        if 'trips.json' in file:
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatrip = pd.DataFrame(json.load(read_file), index=['thing'])
                datatrips.append(datatrip)
                appended_data = pd.concat(datatrips)
                appended_data.to_excel("output_all.xlsx")
                