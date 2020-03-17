import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats
import os
import xlsxwriter

print(os.getcwd())
shp_filepath = "/Users/anniewen/Documents/Dev/NAIS/10kecar_polygon_CornSubset.shp"
tif_filepath="RDPS_Tempavg_20101101.tif"
output_dir = " "

data = gpd.read_file(shp_filepath)
newdf = data['ID']

df_x = newdf.to_frame()

stats = zonal_stats(shp_filepath, tif_filepath)
mean_lst = [f['mean'] for f in stats]
np_mean_list = np.asarray(mean_lst)

df_x.insert(1, 'replace', np_mean_list)

print(df_x)
print(os.getcwd())

writer = pd.ExcelWriter("Extracted_Values.xlsx", engine='xlsxwriter')
df_x.to_excel(writer, sheet_name="replace")

writer.save()