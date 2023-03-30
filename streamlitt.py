# -*- coding: utf-8 -*-
"""streamlitt

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1epiDZZANSn2tklqfFW5jMKRjWU6qpEFL
"""

pip install streamlit==1.13.0

! pip install pyngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# from sklearn import  datasets 
# import sklearn.ensemble
# dt=datasets.load_iris()
# X=dt.data
# Y=dt.target
# from sklearn.ensemble import RandomForestClassifier
# RFC= RandomForestClassifier()
# prd=RFC.fit(X,Y)
# st.title("iris predection")
# st.header("............")
# sl=st.slider('sepal length', min_value=1 , max_value=20 , value=10 )
# sw=st.slider('sepal width', min_value=1 , max_value=20 , value=10  )
# pl=st.slider('petal length', min_value=1 , max_value=20 , value=10 )
# pw=st.slider('petal width', min_value=1 , max_value=20 , value=10  )
# sb=st.button("predict")
# if sb :
#    predct=RFC.predict([[sl,sw,pl,pw]])
#    species = dt.target_names[predct[0]]
#    st.write(f"The predicted species is {species}")

!streamlit run /content/app.py & npx localtunnel --port 8501