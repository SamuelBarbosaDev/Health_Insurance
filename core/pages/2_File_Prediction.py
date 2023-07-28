import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="core/img/stethoscope.png"
)

st.sidebar.header('File Prediction')

st.title("Insurance cost prediction")

st.markdown("Predict medical insurance cost using a csv file:")

# -- Model -- #
path = r'core/models/model.pkl'

with open(path, 'rb') as file:
    model = pickle.load(file)

data = st.file_uploader('Upload your file')

if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction=insurance_prediction)

    st.markdown('Insurance cost predition:')
    st.write(df_output)
    st.download_button(
        label='Download CSV',
        data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv',
        file_name='predicted_insurance.csv'
    )
