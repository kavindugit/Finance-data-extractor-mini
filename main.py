import streamlit as st
import pandas as pd
from data_extractor import extract
import re

# Title
st.title("Financial Data Extractor")

# Paragraph input
text_input = st.text_area(
    "Enter financial paragraph",
    placeholder="Example: The company reported revenue of $120M (estimated $115M) and EPS of $2.5 (estimated $2.3)."
)


# Extract button
if st.button("Extract"):
    if text_input:
        extracted_data = extract(text_input)
        data ={
            'Measure': ['Revenue', 'EPS'],
            'Estimated': [extracted_data['revenue expected'], extracted_data['eps_expected']],
            'Actual': [extracted_data['revenue actual'], extracted_data['eps_actual']]
        }
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("Please enter a financial paragraph to extract data.")


