# **Interactive Column Mapping Tool**

## **Project Overview**
The Interactive Column Mapping Tool is a Streamlit application designed to allow users to upload Excel files, map their columns interactively to desired column names, and then download the processed data. It aims to simplify and streamline the process of data wrangling for datasets with varying column names.

## **Installation & Setup**
1. Ensure you have Python installed. This project requires Python 3.7+.
2. Clone this repository:
   ```
   git clone https://github.com/bernard-rr/interactive_column_mapping
   ```
3. Navigate to the project directory and set up a virtual environment:
   ```
   cd path-to-directory
   python -m venv venv
   source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

## **Usage**

### **Uploading Your File:**
1. Click on the "Browse files" button under "Choose an Excel file".
1. Navigate to the location of your Excel file and select it.
1. Once selected, the file will be uploaded automatically.

### **Specifying Desired Columns:**
1. List your desired columns in the text area provided.
1. Use commas to separate column names.
1. Press `CRTL + ENTER` to apply.

### **Mapping Columns:**
1. Use the drop-down selectors to map your desired columns to the columns from the uploaded Excel file.
1. If a desired column shouldn't map to any uploaded column, select "[Do not map]".

### **Processing & Downloading:**
1. Click "Submit All Mappings".
1. After processing, a preview of your data will appear.
1. To download the processed data, click "Download Excel file".

## **Troubleshooting**
- **File not uploading**: Ensure the file is an `.xlsx` format. Other formats are not supported.
- **Mappings not saving**: Refresh the page and try again. Ensure all mappings are selected before submitting.

## **Contributing**
Contributions are welcome! Please fork this repository and create a pull request with your changes.