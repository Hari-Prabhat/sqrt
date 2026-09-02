import streamlit as st
st.title=("Square Root Calculator")

st.write("This is a simple square root calculator. Enter a number below to calculate its square root.")

st.number_input("Enter a number:", min_value=0.0, step=0.1, key="number")

if st.button("Calculate Square Root"):
    number = st.session_state.number
    if(number<0):
        st.error("Error: The square root of a negative number is not defined in the set of real numbers.")
    else:
        square_root = number ** 0.5
        st.write(f"The square root of {number} is {square_root}.")

st.write("Note: The square root of a negative number is not defined in the set of real numbers.")


