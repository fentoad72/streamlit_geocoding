
import time 
import base64


import streamlit as st
import pandas as pd 
import geopandas as gpd 

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt

import folium
from streamlit_folium import folium_static

def draw_map(df):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="mygeocoder")

    from geopy.extra.rate_limiter import RateLimiter
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    df['location'] = df['full_address'].apply(geocode)
    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    df['lat'] = df['point'].apply(lambda t: t[0] if t else None)
    df['long'] = df['point'].apply(lambda t: t[1] if t else None)

   
    #print(df)
    
    # center on Silverton
    m = folium.Map(location=[37.6300, -107.8139], tiles='cartodb positron',zoom_start=9)
    #st.write(df[0])
    for index, row in df.iterrows():
        loc = [row['lat'],row['long']]
        # add marker for Liberty Bell
        tooltip = row['full_address']
        folium.Marker(
             loc, popup=row['full_address'], tooltip=tooltip
        ).add_to(m)
    folium_static(m)

    return
    

def main():
    import pandas as pd

    file = st.file_uploader("Choose a file")
    if file is not None:
        file.seek(0)
        df = pd.read_csv(file, low_memory=False)
        with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
        st.write(df.head())
        st.write(df.shape)

        draw_map(df)
    

    

if __name__ == "__main__":
    main()  
