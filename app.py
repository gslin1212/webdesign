from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st



# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Function to load data from the uploaded file
def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error: {e}")
            return None
    return None

# File uploader widget
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv,xlsx,xml,xls"])

# Load the data
df = load_data(uploaded_file)

# Check if the data is loaded successfully
if df is not None:
    # Initialize and use Pygwalker StreamlitRenderer
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
    
else:
    st.info("Please upload a CSV file to proceed.")
