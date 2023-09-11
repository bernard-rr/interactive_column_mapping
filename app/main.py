import streamlit as st
import pandas as pd
import gzip
import base64
from utils import gather_mappings, data_wrangling
import urllib.parse

@st.cache(allow_output_mutation=True)
def load_file(file):
    return pd.read_excel(file)

def run_app():
    """Run the Streamlit app for interactive column mapping."""
    
    st.title("Interactive Column Mapping")
    # Link to readme for instructions
    st.markdown("[Read the instructions here](https://github.com/bernard-rr/interactive_column_mapping#usage)")

    # Adding the feedback email link
    email = "bernardchidi5@gmail.com"
    subject = urllib.parse.quote("Feedback on the ICMT")
    feedback_link = f"[Send me feedback](mailto:{email}?subject={subject})"
    st.markdown(feedback_link)

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
                    # Button to download the processed gzipped CSV file
                    st.markdown(get_file_download_link(df_out), unsafe_allow_html=True)

def get_file_download_link(df, filename="processed_data.csv.gz"):
    """Generate a link allowing the data in a given panda dataframe to be downloaded as a gzipped CSV"""
    csv_as_string = df.to_csv(index=False).encode()
    with gzip.open(filename, 'wb') as f:
        f.write(csv_as_string)
        
    b64 = base64.b64encode(open(filename, "rb").read()).decode()
    return f'<a href="data:application/gzip;base64,{b64}" download="{filename}">Download compressed CSV file</a>'

if __name__ == "__main__":
    run_app()
