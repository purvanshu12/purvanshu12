# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:30:09 2021

@author: Purvanshu
"""
import streamlit as st
import pickle
import numpy as np
DT_model=pickle.load(open('DT.pkl', 'rb'))
KNN_model=pickle.load(open('KNN.pkl', 'rb'))
NB_model=pickle.load(open('NB.pkl', 'rb'))
SVM_model=pickle.load(open('SVM.pkl', 'rb'))
def main():
    st.title("Created by Purvanshu Bhatt")
    html_temp = """
    <div style="background-color:tral ; padding:10px">
    <h2 stle= "color:white;text-align:center;">Flower Prediction System</h2>
    </div>
    """
    st.markdown (html_temp,unsafe_allow_html=True)
    activities=['Decision Tree','KNN','NB','SVM']
    option=st.sidebar.selectbox('Whichh model you use?',activities)
    st.subheader(option)
    sl=st.slider('Select Sepal Length', 0.0,10.0)
    sw=st.slider ('Select Sepal width',0.0,5.0)
    pl=st.slider ('select petal length', 0.0,10.0)
    pw= st.slider ('Select petal width' ,0.0,5.0)
    feature_list=[sl,sw,pl,pw]
    single_pred = np.array(feature_list).reshape(1,-1)
    
    clas=['setosa','versicolor','virginica']
    if st.button('predict'):
     if option =='decision Tree':
         st.success(clas[int(DT_model.predict(single_pred))])
     
    elif option=='KNN':
        st.success(clas[int(KNN_model.predict(single_pred))])
    elif option=='NB':
        st.success(clas[int(NB_model.predict(single_pred))])
    else:
        st.success(clas[int(SVM_model.predict(single_pred))])
if __name__=='__main__':
    main()