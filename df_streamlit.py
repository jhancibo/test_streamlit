import streamlit as st
import pandas as pd
import altair as alt

from urllib.error import URLError

@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("experimentDescription")

try:
    #df = get_UN_data()
    df = pd.read_csv("streamlit_df_demo.csv")
    df = df.set_index("experimentDescription")
    year = st.multiselect(
        "Choose experimentDescription", options=list(df.index), default=["Avg_Planting_Avg_Harvest","Avg_Planting_Auto_Harvest"]
    )
    if not year:
        st.error("Please select at least one harvest year.")
    else:
        data = df.loc[year]
        #data /= 1000000.0
        st.write("### Corn yield median (GWAD) (kg/ha)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Corn yield median (GWAD) (kg/ha)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Corn yield median (GWAD) (kg/ha):Q", stack=None),
                color="experimentDescription:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )