import pickle
import pandas as pd
import streamlit as st

# Page config:
st.set_page_config(
    page_title='Insurance Prediction'
)

# Page title:
st.title('Insurance Prediction')

# -- Parameters --:
age = st.number_input(
    label='Age',
    value=18,
    min_value=18,
    max_value=999
)
bmi = st.number_input(
    label='BMI',
    value=25.,
)
children = st.slider(
    label='Children',
    value=0,
    min_value=0,
    max_value=5
)
smoker = st.selectbox(
    label='Smoker',
    options=['no', 'yes']
)

# -- Model --:
path = r'models/model.pkl'

with open(path, 'rb') as file:
    model = pickle.load(file)


def prediction():
    df_input = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker': smoker
    }])
    prediction = model.predict(df_input)[0]

    return prediction


# Predict
if st.button('Predict'):
    try:
        insurance = prediction()
        st.success(f'**Predicted insurance price:** ${insurance:,.2f}')
    except Exception as error:
        st.error(
            f"""
                Couldn't predict the input data.
                The following error occurred:
                {error}
            """
        )
