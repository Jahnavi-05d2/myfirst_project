import streamlit as st
import requests

st.set_page_config(
    page_title="Jaanu's Currency Converter",
    page_icon="💱"
)

st.title("💱 Jaanu's Currency Converter")
st.write("Convert currencies using the latest available exchange rate.")

currencies = {
    "US Dollar (USD)": "USD",
    "Indian Rupee (INR)": "INR",
    "Euro (EUR)": "EUR",
    "British Pound (GBP)": "GBP",
    "Japanese Yen (JPY)": "JPY",
    "Australian Dollar (AUD)": "AUD",
    "Canadian Dollar (CAD)": "CAD"
}

amount = st.number_input(
    "Enter amount",
    min_value=0.01,
    value=1.00
)

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "From",
        list(currencies.keys())
    )

with col2:
    to_currency = st.selectbox(
        "To",
        list(currencies.keys()),
        index=1
    )

if st.button("💱 Convert"):
    from_code = currencies[from_currency]
    to_code = currencies[to_currency]

    if from_code == to_code:
        result = amount
    else:
        url = (
            f"https://api.frankfurter.app/latest"
            f"?amount={amount}&from={from_code}&to={to_code}"
        )

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            result = data["rates"][to_code]

        except Exception:
            st.error("Unable to get the exchange rate. Please try again.")
            st.stop()

    st.success(
        f"{amount:.2f} {from_code} = {result:.2f} {to_code}"
    )