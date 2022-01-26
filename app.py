import pandas as pd
import numpy as np
import streamlit as st
from streamlit_folium import folium_static
import folium

df = pd.read_csv("data.csv")

paris = folium.Map(location = [48.862578, 2.339828], width=500,height=500, tiles = "https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png", attr= 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', zoom_start = 12)

type_dict = {'SANISETTE':"lightgray", 'TOILETTES':"darkpurple", 'WC PUBLICS PERMANENTS':"lightblue", 'URINOIR':"darkblue", 'LAVATORY':"cadetblue", 'URINOIR FEMME':"blue"}

# for i in range(df.shape[0]):
#     html=f"""
#     <p>Adresse : {df.iloc[i]["ADRESSE"]} {df.iloc[i]["ARRONDISSEMENT"]}</br>
#     </br>
#     Horaire : {df.iloc[i]["HORAIRE"]}</br>
#     Accès PMR : {df.iloc[i]["ACCES_PMR"]}</br>
#     Relai bébé : {df.iloc[i]["RELAIS_BEBE"]}</br></p>
#     """
#     iframe = folium.IFrame(html=html, width=500, height=200)
#     popup = folium.Popup(iframe, max_width=2650)
#     folium.Marker(
#     location=[float(df["lat"][i]), float(df["lon"][i])],
#     tooltip=html,
#     icon=folium.Icon(color=type_dict[df["TYPE"][i]]),
#     ).add_to(paris)

st.title("Une envie pressante ? :toilet:")

choice = st.radio("", options=["Toutes les sanisettes", "Plus d'options"])

if choice == "Plus d'options":
    pmr = st.radio("Accès PMR", options=["Oui", "Non"])
    print(pmr)
    baby = st.radio("Relais Bébé", options=["Oui", "Non"])

    if pmr == "Oui" and baby == "Non":
        df_map = df[(df.RELAIS_BEBE == "Non") & (df.ACCES_PMR == "Oui")].reset_index()
    elif pmr == "Non" and baby == "Oui":
        df_map = df[(df.RELAIS_BEBE == "Oui") & (df.ACCES_PMR == "Non")].reset_index()
    elif pmr == "Non" and baby == "Non":
        df_map = df[(df.RELAIS_BEBE == "Non") & (df.ACCES_PMR == "Non")].reset_index()
    elif pmr == "Oui" and baby == "Oui":
        df_map = df[(df.RELAIS_BEBE == "Oui") & (df.ACCES_PMR == "Oui")].reset_index()
else:
    df_map = df

for i in range(df_map.shape[0]):
    html=f"""
    <p>Adresse : {df_map.iloc[i]["ADRESSE"]} {df_map.iloc[i]["ARRONDISSEMENT"]}</br>
    </br>
    Horaire : {df_map.iloc[i]["HORAIRE"]}</br>
    Accès PMR : {df_map.iloc[i]["ACCES_PMR"]}</br>
    Relai bébé : {df_map.iloc[i]["RELAIS_BEBE"]}</br></p>
    """
    iframe = folium.IFrame(html=html, width=500, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    folium.Marker(
    location=[float(df_map["lat"][i]), float(df_map["lon"][i])],
    tooltip=html,
    icon=folium.Icon(color=type_dict[df_map["TYPE"][i]]),
    ).add_to(paris)

folium_static(paris)
