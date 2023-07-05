import streamlit as st
import numpy as np
import json
import geopandas as gpd
import pyproj
import plotly.graph_objs as go
import folium
from streamlit_folium import st_folium
import pandas as pd
from folium.plugins import LocateControl, MarkerCluster
from bs4 import BeautifulSoup
from PIL import Image

# Utility functions
def load_poi_data(path, target_crs="epsg:3005"):
    df = pd.read_csv(path)
    poi_data = gpd.GeoDataFrame(
        df.loc[:, [c for c in df.columns if c != "geometry"]],
        geometry=gpd.GeoSeries.from_wkt(df["geometry"]),
        crs="epsg:3005",  # Assuming the original CRS is EPSG:4326 (geographic CRS)
    )
    poi_data = poi_data.to_crs(target_crs)  # Reproject to the target CRS
    poi_data['geometry_center'] = poi_data['geometry'].centroid
    return poi_data


# Setting page config
st.set_page_config( page_title="Optimal location of EV charging stations",
    page_icon="https://img.icons8.com/external-phatplus-lineal-color-phatplus/64/external-ev-ev-car-phatplus-lineal-color-phatplus.png",
    layout="wide")


# Power location: https://img.icons8.com/external-tal-revivo-green-tal-revivo/100/external-power-location-on-map-for-quick-ev-charge-battery-green-tal-revivo.png
# https://img.icons8.com/external-phatplus-lineal-color-phatplus/64/external-ev-ev-car-phatplus-lineal-color-phatplus.png", width=64
# logo_url = "https://img.icons8.com/external-others-phat-plus/64/external-electric-electric-vehicles-color-line-others-phat-plus-14.png"
logo_url = "https://img.icons8.com/external-phatplus-lineal-color-phatplus/64/external-ev-ev-car-phatplus-lineal-color-phatplus.png"
st.image(logo_url, width=64)
st.header("Optimal placement of EV charging stations in Saarbrücken, Germany")
# st.write("[![Star](<https://img.shields.io/github/stars/><username>/<repo>.svg?logo=github&style=social)](<https://gitHub.com/><username>/<repo>)")
st.markdown("Optimal Placement of EV station based on socio-economic features such as points-of-interest, existing EV charging stations, residential, and commercial areas, etc.")

# Declaring icons: 
park_icon = "https://img.icons8.com/external-victoruler-linear-colour-victoruler/64/external-ferris-wheel-buildings-victoruler-linear-colour-victoruler.png"
parking_space ="https://img.icons8.com/external-bearicons-blue-bearicons/64/external-PARKING-SPACE-capsule-hotel-bearicons-blue-bearicons.png"
restaurant_icon ="https://img.icons8.com/plasticine/100/restaurant.png"
residential_icon="https://img.icons8.com/external-xnimrodx-lineal-color-xnimrodx/64/external-residential-city-xnimrodx-lineal-color-xnimrodx.png"
school_icon = "https://img.icons8.com/external-nawicon-outline-color-nawicon/64/external-school-back-to-school-nawicon-outline-color-nawicon.png"
retail_icon ="https://img.icons8.com/cotton/64/shopping.png"
community_center_icon = "https://img.icons8.com/doodle/48/community.png"
place_of_worship_icon = "https://img.icons8.com/plasticine/100/praying-man--v1.png"
university_icon = "https://img.icons8.com/plasticine/100/graduation-cap.png"
cinema_icon = "https://img.icons8.com/doodle/48/popcorn.png"
library_icon = "https://img.icons8.com/external-goofy-color-kerismaker/96/external-library-education-goofy-color-kerismaker.png"
commercial_icon = "https://img.icons8.com/stickers/100/client-company.png"
government_icon = "https://img.icons8.com/external-soft-fill-juicy-fish/60/external-government-buildings-soft-fill-soft-fill-juicy-fish.png"

    
col1, col2= st.columns([0.8, 0.2])

with col2: 
    with st.container():
        # Expander
        with st.expander("Select options to view"):
            parking_check = st.checkbox(
            "Parks"
            )
            parkingSpaces_check = st.checkbox(
            "Parking spaces"
            )
            restaurant_chk = st.checkbox(
            "Restaurant"
            )
            residential_Chk = st.checkbox(
            "Residential"
            )
            school_Chk= st.checkbox(
            "Schools"
            )
            retail_Chk=st.checkbox(
            "Retail"
            )
            community_center_Chk= st.checkbox(
            "Community center"
            )
            place_of_worship_Chk= st.checkbox(
            "Place of worship"
            )
            university_Chk =st.checkbox(
            "University"
            )
            cinema_Chk =st.checkbox(
            "Cinema"
            )
            library_Chk =st.checkbox(
            "Library"
            )
            commercial_Chk =st.checkbox(
            "Commercial"
            )
            government_Chk =st.checkbox(
            "Government"
            )
            ev_stations_chk = st.checkbox(
            "EV Charging Stations"
            )
            population_chk = st.checkbox(
            "Population density"
            )
        st.subheader("Legend")
        image = Image.open('Data/Icon list.png')
        st.image(image, caption='Legend', width = 200) 
    

with col1:
        
    # Get cleaned/processed data for existing EVs after EDA
    df_ev_data = pd.read_csv('Data/cleaned_ev_data_germany.csv')
    df_saarbrucken = df_ev_data[df_ev_data['City'] == 'Saarbrücken']


    # create a map object of the city of Saarbrucken
    saarbrucken_map_markers = folium.Map(location=[49.24015720000001, 6.996932700000002])

    # Adding different Tiles for fun
    folium.TileLayer('openstreetmap').add_to(saarbrucken_map_markers)
    folium.TileLayer('stamenterrain').add_to(saarbrucken_map_markers)
    folium.TileLayer('stamentoner').add_to(saarbrucken_map_markers)
    folium.TileLayer('stamenwatercolor').add_to(saarbrucken_map_markers)

    

    folium.Marker(
        location=[49.24015720000001, 6.996932700000002],
        popup="Saarbrucken",
        icon=folium.Icon(color="red",icon="glyphicon glyphicon-pushpin"),
    ).add_to(saarbrucken_map_markers)

    # Map existing EVs
    for  cp,type, lat, lng in zip( df_saarbrucken['Number of Charging Points'],df_saarbrucken['Charging Station Type'],df_saarbrucken['Latitude'], df_saarbrucken['Longitude']):
        # ev_img = 'https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-power-location-on-map-for-quick-ev-charge-battery-color-tal-revivo.png'
        # ev_img = "https://img.icons8.com/external-icongeek26-linear-colour-icongeek26/64/external-EV-Power-Tank-ev-station-icongeek26-linear-colour-icongeek26.png"
        ev_img ='https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-power-location-on-map-for-quick-ev-charge-battery-filled-tal-revivo.png'
        
        
        ev_icon = folium.CustomIcon(ev_img, icon_size=(20, 20), popup_anchor=(0, -22))
        ev_html = folium.Html(f"""<p style="text-align: center;"><span style=" font-size: 12px;"><b>Existing EV Charging station:</b> <br><b>Number of charging points:</b> {cp} <br> <b>Charging Station Type:</b> {type}</span></p>
        <p style="text-align: center;">
        """, script=True)
        popup = folium.Popup(ev_html, max_width=700)
        
        ev_marker = folium.Marker(location=[lat, lng], icon=ev_icon, popup=popup)
        ev_marker.add_to(saarbrucken_map_markers)

    # Enable geolocation button on map
    LocateControl(auto_start=False).add_to(saarbrucken_map_markers)

    # Now for POIs
    # Get Curated data
    df_poi_data= load_poi_data('Data/all_city_data_with_pop.csv')
    df_saarbrucken_poi = df_poi_data[df_poi_data['city'] == 'Saarbrucken']

    #Plot centroids:
    df_saarbrucken_poi["latitude"]=df_saarbrucken_poi["geometry_center"].get_coordinates()["y"]
    df_saarbrucken_poi["longitude"]=df_saarbrucken_poi["geometry_center"].get_coordinates()["x"]

    for lat, lng, parking, park_space, restaurant,residential,school,retail, community_center,place_of_worship,university,cinema,library,commercial,government, evs in zip(df_saarbrucken_poi.latitude, 
                                df_saarbrucken_poi.longitude,
                                df_saarbrucken_poi.parking,
                                df_saarbrucken_poi.parking_space,
                                df_saarbrucken_poi.restaurant,
                                df_saarbrucken_poi.residential,
                                df_saarbrucken_poi.school,
                                df_saarbrucken_poi.retail,
                                df_saarbrucken_poi.Community_centre,
                                df_saarbrucken_poi.place_of_worship,
                                df_saarbrucken_poi.university,
                                df_saarbrucken_poi.cinema,
                                df_saarbrucken_poi.library,
                                df_saarbrucken_poi.commercial,
                                df_saarbrucken_poi.government,
                                df_saarbrucken_poi.EV_stations):
        icons_size= 5
        op =1
        

        if parking != 0 and parking_check==True:
            custom_marker = folium.Marker(location=[lat+0.0015, lng], popup=f"Parks: {parking}",opacity=op, icon=folium.CustomIcon(park_icon,icon_size=((parking+icons_size)/1.5, (parking+icons_size)/1.5), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if park_space != 0 and parkingSpaces_check ==True:
            custom_marker = folium.Marker(location=[lat, lng], popup=f"Parking spaces: {park_space}",opacity=op,  icon=folium.CustomIcon(parking_space,icon_size=((park_space+icons_size)/4, (park_space+icons_size)/4), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if restaurant != 0 and restaurant_chk:
            custom_marker = folium.Marker(location=[lat, lng+0.0015], popup=f"Restaurant: {restaurant}",opacity=op,  icon=folium.CustomIcon(restaurant_icon,icon_size=((restaurant+icons_size), (restaurant+icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if residential != 0 and residential_Chk:
            custom_marker = folium.Marker(location=[lat+0.0015, lng+0.0015], popup=f"Residential: {residential}", opacity=op, icon=folium.CustomIcon(residential_icon,icon_size=((residential+icons_size), (residential+icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if school != 0 and school_Chk:
                custom_marker = folium.Marker(location=[lat+0.0017, lng+0.0017], popup=f"Schools: {school}", opacity=op, icon=folium.CustomIcon(school_icon,icon_size=((school*icons_size), (school*icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if retail != 0 and retail_Chk:
                custom_marker = folium.Marker(location=[lat+0.0017, lng], popup=f"Retail: {retail}", opacity=op, icon=folium.CustomIcon(retail_icon,icon_size=((retail+icons_size), (retail+icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if community_center != 0 and community_center_Chk:
                custom_marker = folium.Marker(location=[lat, lng+0.0017], popup=f"Community center: {community_center}", opacity=op, icon=folium.CustomIcon(community_center_icon,icon_size=((community_center*icons_size), (community_center*icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if place_of_worship != 0 and place_of_worship_Chk:
                custom_marker = folium.Marker(location=[lat, lng+0.0017], popup=f"Place of worship: {place_of_worship}", opacity=op, icon=folium.CustomIcon(place_of_worship_icon,icon_size=((place_of_worship*icons_size), (place_of_worship*icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if university != 0 and university_Chk:
                custom_marker = folium.Marker(location=[lat+0.0017, lng], popup=f"University: {university}", opacity=op, icon=folium.CustomIcon(university_icon,icon_size=((university*icons_size*2), (university*icons_size*2)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if cinema != 0 and cinema_Chk:
                custom_marker = folium.Marker(location=[lat+0.0017, lng], popup=f"Cinema: {cinema}", opacity=op, icon=folium.CustomIcon(cinema_icon,icon_size=((cinema*icons_size), (cinema*icons_size)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if library != 0 and library_Chk:
                custom_marker = folium.Marker(location=[lat+0.0010, lng], popup=f"Library: {library}", opacity=op, icon=folium.CustomIcon(library_icon,icon_size=((library+icons_size*2), (library+icons_size*2)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if commercial != 0 and commercial_Chk:
                custom_marker = folium.Marker(location=[lat, lng+0.0010], popup=f"Commercial: {commercial}", opacity=op, icon=folium.CustomIcon(commercial_icon,icon_size=((commercial+icons_size*2), (commercial+icons_size*2)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if government != 0 and government_Chk:
                custom_marker = folium.Marker(location=[lat+0.0010, lng+0.0010], popup=f"Government: {government}", opacity=op, icon=folium.CustomIcon(government_icon,icon_size=((government+icons_size*2), (government+icons_size*2)), popup_anchor=(0, -22))).add_to(saarbrucken_map_markers)
        if evs!=0 and ev_stations_chk:
            folium.Circle(
                location=[lat, lng],
                radius=float(evs*20),
                color='red',
                fill=True,
                fill_color='red',
                opacity=1
            ).add_to(saarbrucken_map_markers)


    # Plot grid:
    if population_chk:
        sim_geo = gpd.GeoSeries(df_saarbrucken_poi["geometry"]).simplify(tolerance=0.001)
        geo_json = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_json, style_function=lambda x: {'lineColor': '#228B22', "fill_opacity":0.7,"fillColor": "orange"})
        geo_j.add_to(saarbrucken_map_markers)


        ev_saar = df_saarbrucken_poi["population"]
        maps=folium.Choropleth(
            geo_data=geo_json,
            name="choropleth",
            data=ev_saar,
            columns=["population"],
            key_on="feature.id",
            # fill_color="YlGn",
            # fill_opacity=0.5,
            # line_opacity=.1,
            fill_color='YlOrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            highlight=True,
            legend_name="Population (%)"
        ).add_to(saarbrucken_map_markers)

    # TODO
    # Plot predictions: 
    # pred_icon_cross ="https://img.icons8.com/ios-filled/100/FA5252/marker-x.png"
    # pred_icons_pin = "https://img.icons8.com/ios-filled/100/map-pin.png"
    pred_icon_cross="https://img.icons8.com/ios-filled/100/x.png"
    # pred_icons_pin_colored= "https://img.icons8.com/arcade/64/map-pin.png"
    # pred_icon_ev ="https://img.icons8.com/external-icongeek26-glyph-icongeek26/64/external-EV-Location-ev-station-icongeek26-glyph-icongeek26.png"

    # Get predictions for Saarbrucken
    df_predicted = load_poi_data('Data/saarbrucken_predicted_EV_stations.csv')

    #Plot centroids:
    df_predicted["latitude"]=df_predicted["geometry_center"].get_coordinates()["y"]
    df_predicted["longitude"]=df_predicted["geometry_center"].get_coordinates()["x"]

    for lat, lng, predicted_evs in zip(df_predicted.latitude, 
                                df_predicted.longitude,
                                df_predicted.predicted_EV_stations):
            if predicted_evs!=0:
                pred_ev_icon = folium.CustomIcon(pred_icon_cross, icon_size=(20, 20), popup_anchor=(0, -22))
                folium.Marker(location=[lat, lng], icon=pred_ev_icon, popup=str("Predicted EV")).add_to(saarbrucken_map_markers)




    # Map folium markers and save to html file
# width=1250, height=500
    # Other mapping code (e.g. lines, markers etc.)
    folium.LayerControl().add_to(saarbrucken_map_markers)
    st_folium(saarbrucken_map_markers,   width=1550, height=800, center=[49.24015720000001, 6.996932700000002], returned_objects=[],zoom=13)
    st.caption("Map of Saarbrücken")
    saarbrucken_map_markers.save("Mymap.html")

   




st.divider()

# EDA / Results 
st.subheader("EDA")
image = Image.open('Data/Number of different types of infrastructure in Saarbrucken.png')
st.image(image, caption='Number of different types of infrastructure in Saarbrucken') 