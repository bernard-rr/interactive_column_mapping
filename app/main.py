import streamlit as st
import pandas as pd
from .utils import gather_mappings, data_wrangling


def run_app():
    """Run the Streamlit app for interactive column mapping."""
    
    # Set the app title
    st.title("Interactive Column Mapping")
    
    # Upload Excel file
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        
        # Get desired columns input from user
        col = st.text_input("Enter a desired column (add one at a time):", value="")
        desired_columns = []
        
        if st.button("Add Column"):
            desired_columns.append(col)
            st.write("Desired Columns:", desired_columns)
        
        # Combine default option with dataframe columns
        input_columns = ["[Do not map]"] + list(df.columns)
        
        # Get column mappings
        mappings = gather_mappings(desired_columns, input_columns)
        
        # If user submits the mappings, display the processed dataframe
        if st.button("Submit Mapping"):
            df_out = data_wrangling(df, mappings, desired_columns)
            st.write(df_out)


# Run the app if the script is executed directly
if __name__ == "__main__":
    run_app()
