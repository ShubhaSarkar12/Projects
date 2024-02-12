# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:08:50 2024

@author: shubh
"""

import pickle
import streamlit as st

st.title('Close Price Prediction :bar_chart:')

load = open('model.pkl','rb')
model = pickle.load(load)


def predict(Open,High,Low):
    prediction = model.predict([[Open,High,Low]])
    return prediction

def main():
    st.markdown('This is a very simple webapp for prediction of Close Price')
    Open = st.number_input('Open')
    High = st.number_input('High')
    Low = st.number_input('Low')
    if st.button('Predict'):
        result = predict(Open,High,Low)
        st.success('The Close Price is :₹{}'.format(result))
        
        
        
        
        
if __name__ == '__main__':
    main()