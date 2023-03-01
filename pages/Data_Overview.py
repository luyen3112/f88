import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st


st.set_page_config(page_title="Data Detail",
                page_icon = ":pig:",
                layout="wide")
                
st.title(":mag: Forecasting Data for March")
st.markdown("##")
 
df = pd.read_excel("EDA/CIMB_F88.xlsx")
df['Date'] = pd.to_datetime(df['Date']).dt.date
pd.set_option('display.max_rows', None)
st.dataframe(df)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data
df_xlsx = to_excel(df)
st.download_button(label='📥 Download data',
                                data=df_xlsx ,
                                file_name= 'data.xlsx')

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
