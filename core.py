from datetime import datetime, timedelta
import streamlit as st
import app

st.set_page_config(
    page_title="Crypto Price At Date",
    layout="wide"
    )

if 'date_value' not in st.session_state:
    st.session_state['date_value'] = datetime.now().date()
if 'time_value' not in st.session_state:
    st.session_state['time_value'] = datetime.now().time()
if 'amount' not in st.session_state:
    st.session_state['amount'] = 0.0

col1, col2 = st.columns(2)

with col1:
    st.title('Crypto Price At Specific Date')

    option = st.selectbox( 'Which coin?', app.symbols(), index=0)

    date_value = st.date_input('Enter the date', st.session_state['date_value'])

    time_value = st.time_input('Select a time', st.session_state['time_value'], step=timedelta(seconds=60))

    datetime_value = datetime.combine(date_value, time_value)

    st.session_state['amount'] = st.number_input('Enter the amount you had', step=0.00000001, format="%.8f")

    clicked = st.button('Calculate')

with col2:
    try:
        crypto_value = app.value_of_crypto_at(option, datetime_value)
        st.markdown('# Result', help='Value based on Binance API')
        
        st.markdown(f'### Price was `${crypto_value}` USDT')

        st.markdown(f'### You had `{st.session_state["amount"]:.8f} {option}`  at  *{datetime_value}*')
        
        st.markdown(f'### Equivalent to `${app.amount_in_usdt(st.session_state["amount"], crypto_value):.2f}` USDT')
        st.balloons()
    except Exception as e:
        st.error(f'Error: {e}')