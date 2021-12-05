import pandas as pd 
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

def main():
    df = pd.read_csv("userdata.csv")
    df.to_csv("userdata.csv")
    s1 = df.UserID.unique()
    s11 = st.sidebar.selectbox('User ID',(s1))
    df1 = df.loc[df["UserID"] == s11]
    df1 = df1.head(20)
    df1 = df1[['UserID','Order','OrderType']]
    return(df1)

s = main()
st.dataframe(s)
