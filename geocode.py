import time 
import base64

import streamlit as st
import pandas as pd 
import geopandas as gpd 

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt
import plotly_express as px 

st.title("Geocoding Application in Python")
st.markdown("Upload a CSV File with address columns (Street name & number, Postcode, City)")

def choose_geocode_column(df):
    st.sidebar.subheader("Select Address Column from the Sidebar")
    st.sidebar.info("Example:  289 Silver, Durango, CO 81301")
    selection = st.sidebar.selectbox("Select the column", df.columns.tolist())
    df["geocde_col"] = df[selection]
    return df



def main():
    file = st.file_uploader("Choose a file")
    if file is not None:
        file.seek(0)
        df = pd.read_csv(file, low_memory=False)
        with st.spinner('Reading CSV File...'):
            time.sleep(5)
            st.success('Done!')
        st.write(df.head())
        st.write(df.shape)

        #geocode_addresses = choose_geocode_column(df)
        df["full_address"] = df.address + "," + df.city + "," + df.state
        st.info("Addresses to be geocoded:")
        st.write(df)
        geolocator = Nominatim(timeout=10, user_agent = "myGeolocator")
        df['gcode'] = df.full_address.apply(geolocator.geocode)
        #df['lat'] = [g.latitude for g in df.gcode]
        #df['long'] = [g.longitude for g in df.gcode]
        

        
        st.write(df.head())
        #st.plotly_chart(display_map(geocoded_df))
        
        

        
if __name__ == "__main__":
    main()
