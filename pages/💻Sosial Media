import streamlit as st
import time

st.markdown("# Widget ❄️")
st.sidebar.markdown("# Widget ❄️")

'...and now we\'re done!'

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
st.snow()

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)
    st.write('Makanan favorit: ', option)
    st.write('Warna Favorit: ', options)
with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 100, 50, key='my_slider')
    option = st.selectbox(
     'Apa makanan kesukaanmu?',
     ('Pempek', 'Gudeg', 'Rendang','Sate'))
    options = st.multiselect(
     'Warna favorit',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
    checkbox_input = st.checkbox('Agree or Disagree', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
