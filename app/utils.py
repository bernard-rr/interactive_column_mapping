import pandas as pd
import streamlit as st

def gather_mappings(desired_columns, input_columns):
    """Gather mappings for desired columns from user input via Streamlit."""
    mappings = {}
    for desired_col in desired_columns:
        value = st.selectbox(
            f"Map '{desired_col}' to:", 
            options=input_columns, 
            key=desired_col
        )
        if value != "[Do not map]":
            mappings[desired_col] = value
    return mappings

def data_wrangling(df, mappings, desired_columns):
    """Re-arrange and rename columns in the dataframe based on user mappings."""
    df = df.rename(columns=mappings)
    for col in desired_columns:
        if col not in df.columns:
            if col in mappings:
                df[col] = df[mappings[col]]
            else:
                df[col] = pd.NA
    df = df[desired_columns]
    return df
