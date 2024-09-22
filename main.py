import streamlit as st

st.set_page_config(page_title="Multi-format Analysis App", layout="wide")

st.title("Multi-format Analysis App")
st.write("Welcome to the Multi-format Analysis App. This application allows you to upload CSV, Excel, or JSON files and perform various statistical analyses.")

st.markdown("""
### Instructions:
1. Use the sidebar to navigate between different pages.
2. Start by uploading your CSV, Excel, or JSON file on the Home page.
3. Select the required columns for analysis on the Home page.
4. Perform C-index computations on the C-Index page.
5. Calculate IDI and NRI on the IDI/NRI page.

### Supported File Formats:
- CSV (.csv)
- Excel (.xlsx)
- JSON (.json)

### Overview of Metrics:

#### C-Index (Concordance Index):
The C-Index measures the predictive accuracy of a survival model. It ranges from 0.5 to 1.0, where 0.5 indicates random predictions and 1.0 indicates perfect predictions. A higher C-Index suggests better model performance.

#### IDI (Integrated Discrimination Improvement):
IDI quantifies the improvement in prediction performance between two models. A positive IDI indicates that the new model improves risk prediction compared to the old model.

#### NRI (Net Reclassification Improvement):
NRI assesses the improvement in risk classification offered by a new model compared to an old model. A positive NRI suggests that the new model improves risk classification.

### Navigation:
- **Home**: Upload file (CSV, Excel, or JSON), preview data, split dataset, and select columns
- **C-Index**: Compute and compare C-index for old and new models
- **IDI/NRI**: Calculate Integrated Discrimination Improvement and Net Reclassification Improvement

Please select a page from the sidebar to begin your analysis.
""")

# Add this code to ensure the sidebar is always visible
st.sidebar.title("Navigation")
st.sidebar.info("""
1. Start with the Home page
2. Then go to C-Index page
3. Finally, visit the IDI/NRI page
""")
