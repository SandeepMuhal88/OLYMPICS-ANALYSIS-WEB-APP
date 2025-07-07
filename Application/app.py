import streamlit as st
import pandas as pd
import Preproccesor

df =Preproccesor.preprocessor
st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athelete wise Analysis')
)


st.dataframe(df)