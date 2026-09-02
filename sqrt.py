import streamlit as st
st.title("Square Root Calculator")

st.write("This is a simple square root calculator. Enter a number below to calculate its square root.")


st.markdown("Enter a non-negative number in the input field.")
number=st.number_input("Enter a number:", min_value=0.0, step=0.1)

if st.button("Calculate Square Root"):
    if(number<0):
        st.error("Error: The square root of a negative number is not defined in the set of real numbers.")
        st.warning("Note: The square root of a negative number is not defined in the set of real numbers.")
    else:
        square_root = number ** 0.5
        st.write(f"The square root of {number}   is   {square_root}.")


st.write("Made by Hari Prabhat")

