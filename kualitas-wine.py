import pickle
import streamlit as st
import numpy as np

# membaca model
model = pickle.load(open('kualitas-wine.sav', 'rb'))

#judul web
st.title('Prediksi Kualitas Wine')

fixed_acidity = st.number_input('Input nilai keasaman tetap')
volatile_acidity = st.number_input('Input nilai keasaman mudah menguap')
citric_acid = st.number_input('Input nilai asam sitrat')
residual_sugar = st.number_input('Input nilai sisa gula')
chlorides = st.number_input('Input nilai klorida')
free_sulfur_dioxide = st.number_input('Input nilai sulfur dioksida bebas')
total_sulfur_dioxide = st.number_input('Input nilai total sulfur dioksida')

density = st.number_input('Input nilai densitas')
pH = st.number_input('Input nilai pH')
sulphates = st.number_input('Input nilai sulfat')
alcohol = st.number_input('Input nilai alkohol')

predict = ''

if st.button('Proses'):
    predict = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, 
                            free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
    if(predict[0] == 0):
        predict = 'Kualitas Wine Buruk'
    else:
        predict = 'Kualitas Wine Bagus'
    st.success(predict)
