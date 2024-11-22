import streamlit as st
import math

# Define the Tran_Eff function
def Tran_Eff(VSC, ISC, WSC):
    # Calculate ZSC
    ZSC = VSC / ISC
    # Calculate R1
    R1 = WSC / (ISC**2)
    # Calculate X1
    X1 = math.sqrt(ZSC*2 - R1*2)
    return R1, X1

# Streamlit App
st.title("2205A21057-PS8")

st.header("Transformer Short Circuit Test Calculator")

# Input fields
VSC = st.number_input("Enter the short circuit voltage (VSC) in volts:", min_value=0.0, step=0.1)
ISC = st.number_input("Enter the short circuit current (ISC) in amperes:", min_value=0.0, step=0.1)
WSC = st.number_input("Enter the short circuit power (WSC) in watts:", min_value=0.0, step=0.1)

if st.button("Calculate"):
    try:
        # Calculate R1 and X1
        R1, X1 = Tran_Eff(VSC, ISC, WSC)
        st.success(f"Winding Resistance (R1): {R1:.4f} Ω")
        st.success(f"Reactance (X1): {X1:.4f} Ω")
    except ValueError as e:
        st.error("Invalid input: Ensure that VSC, ISC, and WSC are positive, and ISC is not zero.")

# Footer
st.write("Developed by Sabavath Naveen (Roll No: 2205A21057)")