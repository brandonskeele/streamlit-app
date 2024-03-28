import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Popular Name Trends")

url = "https://github.com/esnt/Data/raw/main/Names/popular_names.csv"
df = pd.read_csv(url)

name = st.text_input("Enter a name", "John")
name_df = df[df["name"] == name]

tab1, tab2 = st.tabs(["Male", "Female"])

st.header(f"{name} over time")

with tab1:
    plot_df = name_df[name_df["sex"] == "M"]
    fig_m = px.line(plot_df, x="year", y="n")
    st.plotly_chart(fig_m)

with tab2:
    plot_df = name_df[name_df["sex"] == "F"]
    fig_f = px.line(plot_df, x="year", y="n")
    st.plotly_chart(fig_f)

with st.sidebar:
    year = st.slider("Choose a year", 1910, 2021)
    year_df = df[df["year"] == year]

    girls_names = year_df[year_df.sex=="F"].sort_values("n", ascending=False).head(5)[["name", "n"]]
    boys_names = year_df[year_df.sex=="M"].sort_values("n", ascending=False).head(5)[["name", "n"]]

    top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], ignore_index=True, axis=1)
    top_names.columns = ["Girls", "Girls Count","Boys", "Boys Count"]
    top_names.index += 1

    st.header(f"Top Names in {year}")
    st.dataframe(top_names)