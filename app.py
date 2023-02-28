import streamlit as st
import time


st.title('My Name is :red[Rishi Singh] :sunglasses:')

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :joy:")
    
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.success('Done!')
    
st.snow()