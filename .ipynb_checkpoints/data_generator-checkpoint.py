import pandas as pd
import glob
import os
import numpy as np

def concatenate_rasters():
    search_path = "data/*.csv" 
    all_files = glob.glob(search_path, recursive=True)
    processed_dfs = []
    raster_files = [f for f in all_files if "raster_data" in f.lower()]
    processed_dfs = []
    for filename in raster_files:
        df = pd.read_csv(filename) 
        site_id = filename.split('site')[1].replace('.csv', '')
        df.insert(0, 'site', site_id)
        processed_dfs.append(df)

    data = pd.concat(processed_dfs, axis=0, ignore_index=True)
    data.to_csv("data/data.csv", index=False)
    return data
