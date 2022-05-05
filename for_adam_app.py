

import streamlit as st
import pandas as pd
import altair as alt

import geopandas


df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
st.write(gdf.head())
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world[world.continent == 'South America'].plot(
    color='white', edgecolor='black')
gdf.plot(ax=ax, color='red')
st.pyplot()

# %%
import geopandas
zipfile = "zip:////Users/james/Downloads/adam/il_ia_mo.geojson.zip"
df_il_ia_mo = geopandas.read_file(zipfile)
# %%
df_il_ia_mo['lontitude'] = df_il_ia_mo.point_object.x
df_il_ia_mo['latitude'] = df_il_ia_mo.point_object.y
# %%
