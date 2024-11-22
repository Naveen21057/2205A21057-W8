import streamlit as st
import math

# Define the Tran_Eff function
def Tran_Eff(VSC, ISC, WSC):
    # Calculate ZSC
    ZSC = VSC / ISC
    # Calculate R1
    R1 = WSC / (ISC**2)
    X1 = math.sqrt((ZSC * 2) - (R1 * 2))
    return R1, X1

# Streamlit App
st.title("2205A21057-PS8")
st.header("Transformer Short Circuit Test Calculator")

# Input fields
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        VSC = st.number_input("Enter the short circuit voltage (VSC) in volts:", min_value=0.0, step=0.1)
        ISC = st.number_input("Enter the short circuit current (ISC) in amperes:", min_value=0.0, step=0.1)
        WSC = st.number_input("Enter the short circuit power (WSC) in watts:", min_value=0.0, step=0.1)
        calculate_button = st.button("Calculate")

with col2:
    if calculate_button:
        R1, X1 = Tran_Eff(VSC, ISC, WSC)
        if math.isnan(X1):
            st.write("Error: Unable to calculate X1 due to invalid values.")
        else:
            st.write(f"R1: {R1:.2f} Ω")
            st.write(f"X1: {X1:.2f} Ω")

st.write("Developed by Sabavath Naveen (Roll No: 2205A21057)")
