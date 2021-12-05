import pandas as pd 
import streamlit as st
import warnings
from PIL import Image
warnings.filterwarnings("ignore")

STYLE = """
<style>
img {
    max-width: 100%;
}
</style> """

def main():
    html_temp = """
	<div style="background-color:tomato;"><p style="color:white;font-size:40px;padding:9px">Personalised-Food-Recommendation-For-Multi-Cuisine-Restaurants</p></div>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.sidebar.header("About App")
    st.sidebar.info("The owner of the five - star hotel wants to make a recommendation system, which will help food supply chain management to recommend food based on the favourite dishes and popular choice.Recommending food to the Customer based on their preference.Minimize time taken for food Recommendation")
    st.sidebar.text("Built with Streamlit")
    
    st.sidebar.header("For Any Queries/Suggestions Please reach out at :")
    st.sidebar.info("gauravkumarvishwakarma@gmail.com")    

    image = Image.open("Project1 logo.jpeg")
    st.image(image, caption='Food Recommendation System',use_column_width=True)

#st.title("Personalised-Food-Recommendation-For-Multi-Cuisine-Restaurants")
    #st.sidebar("Select a id which you'd like to get the recommdation of food :")
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
