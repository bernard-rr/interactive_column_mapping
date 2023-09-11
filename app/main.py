import streamlit as st
import pandas as pd
import base64
import zipfile
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
                    # Button to download the processed data inside a zipped folder
                    st.markdown(get_file_download_link(df_out), unsafe_allow_html=True)

def get_file_download_link(df, csv_filename="processed_data.csv", zip_filename="processed_data.zip"):
    """Generate a link allowing the data in a given panda dataframe to be downloaded inside a zip file"""
    csv = df.to_csv(index=False)
    with zipfile.ZipFile(zip_filename, 'w') as zf:
        zf.writestr(csv_filename, csv)
        
    b64 = base64.b64encode(open(zip_filename, "rb").read()).decode()
    return f'<a href="data:application/zip;base64,{b64}" download="{zip_filename}">Download zipped CSV file</a>'

if __name__ == "__main__":
    run_app()
