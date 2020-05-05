import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

map_df = gpd.read_file('ZIP_CODE_040114/ZIP_CODE_040114.shp')
df = pd.read_csv('u.csv')

df['ZIPCODE'] = df['Zip Code']




map_df['ZIPCODE'] = map_df['ZIPCODE'].apply(lambda x: int(x))

merge1 = pd.merge(map_df, df, on = 'ZIPCODE')


fig, ax = plt.subplots(1, figsize=(10, 6))
vmin, vmax = min(merge1['Positive']) - 10, max(merge1['Positive']) + 10
merge1.plot(column='Positive', cmap= 'Accent', linewidth=0.8, ax =ax, edgecolor='0.9')
sm = plt.cm.ScalarMappable(cmap='Accent', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []# add the colorbar to the figure
cbar = fig.colorbar(sm)

plt.savefig('m.png')


merge1.plot(kind='scatter', x = 'latitude', y = 'longitude', s='Total', c='Total', cmap= 'Accent', linewidth=0.8, ax =ax, edgecolor='0.9')
plt.savefig('n.png')