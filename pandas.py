
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
    

def main():
    import pandas as pd
    df = pd.DataFrame({'name': ['3180 E 6th Ave,Durango,CO,81301',
                            '1364 Reese St, Silverton,CO,81433',
                           '81 Ball Ln,Durango,CO,81301']})
    print(df)

    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="mygeocoder")

    from geopy.extra.rate_limiter import RateLimiter
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=5)
    df['location'] = df['name'].apply(geocode)
    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    df['lat'] = df['point'].apply(lambda t: t[0] if t else None)
    df['long'] = df['point'].apply(lambda t: t[1] if t else None)

   
    #print(df)
    
    # center on Silverton
    m = folium.Map(location=[37.6300, -107.8139], tiles='cartodb positron',zoom_start=9)
    #st.write(df[0])
    for index, row in df.iterrows():
        loc = [row['lat'],row['long']]
        print(row['name'], loc)
        # add marker for Liberty Bell
        tooltip = row['name']
        folium.Marker(
             loc, popup=row['name'], tooltip=tooltip
        ).add_to(m)
    folium_static(m)


if __name__ == "__main__":
    main()  
