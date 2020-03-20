import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats
import os
import xlsxwriter

print(os.getcwd())
shp_filepath = "/Users/anniewen/Documents/Dev/NAIS/EasternOntarioCAR_10kgrid_corn/10kecar_polygon_CornSubset.shp" # path to shape file
tif_dirpath="Temperature" # Path to folder containing tifs of interest
output_dir = " "

lst_files = os.listdir(tif_dirpath)

data = gpd.read_file(shp_filepath)
newdf = data['ID']
df_x = newdf.to_frame()

count = 0
for tif in lst_files:
    count += 1

    stats = zonal_stats(shp_filepath, os.path.join(tif_dirpath,tif))
    mean_lst = [f['mean'] for f in stats]
    np_mean_list = np.asarray(mean_lst)

    df_x.insert(count, tif, np_mean_list)

print(df_x)
print(os.getcwd())

writer = pd.ExcelWriter("Extracted_Values.xlsx", engine='xlsxwriter')
df_x.to_excel(writer, sheet_name="replace")

writer.save()