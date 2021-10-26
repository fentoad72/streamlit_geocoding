
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
    #from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="mygeocoder")

    #from geopy.extra.rate_limiter import RateLimiter
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=5)
    df['location'] = df['full_address'].apply(geocode)
    print("after location thinbg")
    st.write("after geocode")
    st.dataframe(df['location'])
    bad_df = df[df.location.isnull()]
    st.write("bad codes")
    st.dataframe(bad_df)

    


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
