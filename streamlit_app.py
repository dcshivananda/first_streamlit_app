import streamlit
import pandas as pd
my_fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe('my_fruits_list')
