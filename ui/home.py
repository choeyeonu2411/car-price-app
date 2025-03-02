import streamlit as st

def run_home() :
    st.subheader('자동차 데이터를 분석하고 예측하는 App')
    st.text('데이터 캐글에 있는  Car_Purchasing_Data.csv 파일을 사용합니다.')
    st.text('EDA 탭에서 데이터를 분석하고, ML 탭에서 예측 수행 합니다.')
    st.image('image/car.jpg',use_container_width=True)