import time
import random
import streamlit as st

state = st.session_state

# State machine states
if 'READY_TO_SEND' not in state:
    state.READY_TO_SEND = False
if 'CODE_CONFIRMED' not in state:
    state.CODE_CONFIRMED = False

# Session values
if 'CODE' not in state:
    state.CODE = ''
if 'RAND_KEY' not in state:
    state.RAND_KEY = 0

message = st.empty()
def sendmail():
    message.success('Message sent')
    time.sleep(2)
    message.empty()

if not state.READY_TO_SEND:
    with st.form(key='my_email_form', clear_on_submit=False):
        email = st.text_input(label='Please enter your email address', placeholder='name@company.com')
        if st.form_submit_button(label='send'):
            state.READY_TO_SEND = True

def _code_confirm_cb():
    state.CODE_CONFIRMED = True

if state.READY_TO_SEND and not state.CODE_CONFIRMED:
    fixed_digits = 4
    state.RAND_KEY = random.randrange(1111, 9999, fixed_digits)
    message.info(f'DEBUG (code hint): {state.RAND_KEY}')

if state.READY_TO_SEND:
    with st.form(key='my_code', clear_on_submit=True):
        state.CODE = st.text_input(label='Enter code', key='code')
        if st.form_submit_button(label='Confirm', on_click=_code_confirm_cb):
            print(state.CODE, state.RAND_KEY)
            # state.CODE = state.code
            if str(state.CODE) == str(state.RAND_KEY):
                state.READY_TO_SEND = False

if state.CODE_CONFIRMED:
    state.CODE_CONFIRMED = False
    sendmail()
    st.experimental_rerun()
