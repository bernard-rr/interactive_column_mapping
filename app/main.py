import streamlit as st
import pandas as pd
from utils import gather_mappings, data_wrangling

def run_app():
    """Run the Streamlit app for interactive column mapping."""
    
    # Set the app title
    st.title("Interactive Column Mapping")
    
    # Upload Excel file
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        
        # Get desired columns input from user using a text_area
        desired_cols_str = st.text_area("Enter desired columns separated by commas:", value="")
        
        # Parse the entered columns to create a list of desired columns
        desired_columns = [col.strip() for col in desired_cols_str.split(",") if col.strip()]
        
        # If there are any desired columns entered
        if desired_columns:
            # Combine default option with dataframe columns
            input_columns = ["[Do not map]"] + list(df.columns)
            
            # Gather the column mappings using the provided function
            mappings = gather_mappings(desired_columns, input_columns)
            
            # If user submits the mappings, display the processed dataframe
            if st.button("Submit Mapping"):
                with st.spinner('Processing data...'):
                    df_out = data_wrangling(df, mappings, desired_columns)
                    st.write(df_out.head())

# Run the app if the script is executed directly
if __name__ == "__main__":
    run_app()
