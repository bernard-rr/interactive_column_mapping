import streamlit as st
import pandas as pd
from utils import gather_mappings, data_wrangling

@st.cache(allow_output_mutation=True)
def load_file(file):
    return pd.read_excel(file)

def run_app():
    """Run the Streamlit app for interactive column mapping."""
    
    st.title("Interactive Column Mapping")
    
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
    
    if uploaded_file:
        df = load_file(uploaded_file)
        
        desired_cols_str = st.text_area("Enter desired columns separated by commas:", value="")
        desired_columns = [col.strip() for col in desired_cols_str.split(",") if col.strip()]
        
        if desired_columns:
            input_columns = ["[Do not map]"] + list(df.columns)
            mappings = gather_mappings(desired_columns, input_columns)
            
            if st.button("Submit All Mappings"):
                with st.spinner('Processing data...'):
                    df_out = data_wrangling(df, mappings, desired_columns)
                    st.write(df_out.head())  # Display only the first few rows

if __name__ == "__main__":
    run_app()
