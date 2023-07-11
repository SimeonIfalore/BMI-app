import streamlit as st
st.title('Simeon\'s BMI Calculator')

#adding images
from PIL import Image
image = Image.open("C:\\Users\\Simeon\\Downloads\\pexels-pixabay-209887.jpg")
st.image(image, width= 500)

#INPUTING PARAMETERS
name = st.text_input('Type your name, press enter and then move to the next box')
weight = st.number_input("Enter your weight (in kgs)")
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if (status == 'cms'):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")
elif (status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if (st.button('Calculate BMI')):

    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of BMI index
    if (bmi < 16):
        st.error(f'hey {name} you are extremely underweight! Please visit a Dietician')
    elif (bmi >= 16 and bmi < 18.5):
        st.warning(f'{name} you are underweight, You need to take your health serious')
    elif (bmi >= 18.5 and bmi < 25):
        st.success(f'😀 You are healthy {name} , Keep it up')
    elif (bmi >= 25 and bmi < 30):
        st.warning(f'Hello {name} you are overweight')
    else:
        st.error(f'OOOps {name}, You are Obesed')