# from turtle import*
# import colorsys

# speed(0)
# bgcolor("black")
# h = 0
# for i in range(16):
#     for j in range(18):
#         c = colorsys.hsv_to_rgb(h,1,1)
#         color()
#         h += 0.005
#         rt(90)
#         circle(150 - j * 6 , 90)
#         lt(90)
#         circle(150 - j *6 ,90)
#         rt(180)
#     circle(40 ,24)
# done()

import  streamlit as st
st.title("welcome to our school")
st.title("Student Registration Form")
import pandas as pd

name = st.text_input("enter your name : ")
fathername = st.text_input("enter your father name : ")
adr = st.text_area("enter your address : ")
age = st.number_input("enter your age : ", min_value=0, max_value=100, value=0)
classs = st.selectbox("select your class : ", ["1", "2", "3", "4", "5"])
button = st.button("submit")
if button:
    st.write("your name is : ", name)
    st.write("your father name is : ", fathername)
    st.write("your address is : ", adr)
    st.write("your age is : ", age)
    st.write("your class is : ", classs)
    st.write("your data is submitted successfully")


