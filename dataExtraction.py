import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats
import os
import xlsxwriter

print(os.getcwd())
shp_filepath = "/Users/anniewen/Documents/Dev/NAIS/EasternOntarioCAR_10kgrid_corn/10kecar_polygon_CornSubset.shp" # path to shape file
tif_dirpath=["Temperature", "RDPA" ] # List of paths to folder containing tifs of interest
d = {}
output_dir = " "

writer = pd.ExcelWriter("Extracted_Values.xlsx", engine='xlsxwriter')

for dir in tif_dirpath:
    lst_files = os.listdir(dir)

    data = gpd.read_file(shp_filepath)
    newdf = data['ID']
    df_x = newdf.to_frame()

    count = 0
    for tif in lst_files:
        count += 1

        stats = zonal_stats(shp_filepath, os.path.join(dir,tif))
        mean_lst = [f['mean'] for f in stats]
        np_mean_list = np.asarray(mean_lst)

        df_x.insert(count, tif, np_mean_list)
    # d["{0}".format(dir)] = df_x
    df_x.to_excel(writer, sheet_name=dir)

print(os.getcwd())
writer.save()