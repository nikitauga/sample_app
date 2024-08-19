import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


# Layout
st.set_page_config(
    page_title="SimiLo",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Upload", "Download", "Query"],
        icons=["house", "cloud-upload", "download", "database"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title("Home")
    st.write("Welcome to the home page!")

elif selected == "Upload":
    st.title("Upload a File")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            edited_df = st.data_editor(df)
            
            if st.button("Save Changes"):
                edited_file_path = "edited_file.csv"
                edited_df.to_csv(edited_file_path, index=False)
                st.success("Changes saved successfully!")
                st.write("Download the edited file:")
                st.download_button(
                    label="Download CSV",
                    data=edited_df.to_csv(index=False),
                    file_name='edited_file.csv',
                    mime='text/csv'
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif selected == "Download":
    st.title("Download Data")
    
    # Input for SQL query
    query_input = st.text_area("Enter your SQL query:", "")
    
  

elif selected == "Query":
    st.title("Run a SQL Query")
    
    