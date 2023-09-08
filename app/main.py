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
        process_input = st.button("Process Columns Input")

        if process_input and desired_cols_str:
            desired_columns = [col.strip() for col in desired_cols_str.split(",") if col.strip()]
            
            if desired_columns:
                input_columns = ["[Do not map]"] + list(df.columns)
                mappings = gather_mappings(desired_columns, input_columns)

                if st.button("Submit All Mappings"):
                    with st.spinner('Processing data...'):
                        df_out = data_wrangling(df, mappings, desired_columns)
                        st.write(df_out.head())

                    # Download the processed Excel file
                    st.markdown(get_file_download_link(df_out, "processed_data.xlsx"), unsafe_allow_html=True)

        # Button to view README
        if st.button("Instructions"):
            st.write("For instructions, please check the README file [here](https://github.com/bernard-rr/lit_column_mapping/blob/main/README.md).")  # Replace 'YOUR_README_URL' with the actual URL.

def get_file_download_link(df, filename):
    """Generate a link allowing the data in a given panda dataframe to be downloaded"""
    import base64
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    b64 = base64.b64encode(open(filename, "rb").read()).decode()
    return f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}">Download Excel file</a>'

if __name__ == "__main__":
    run_app()
