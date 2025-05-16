import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Add a description
st.write("This is a simple scientific calculator built with Streamlit.")

# Input for the user to enter an expression
expression = st.text_input("Enter a mathematical expression:")

# Handle the evaluation and display the result
if expression:
    try:
        # Safe evaluation of the expression using math functions
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        st.write(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Adding some scientific functions
st.subheader("Scientific Functions")

# Option to use trigonometric functions
angle = st.number_input("Enter angle (in degrees)", value=0)

# Convert angle to radians for trigonometric functions
radians = math.radians(angle)

# Calculate trigonometric values
sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

# Display trigonometric results
st.write(f"sin({angle}°) = {sin_val}")
st.write(f"cos({angle}°) = {cos_val}")
st.write(f"tan({angle}°) = {tan_val}")

# Option for logarithmic and exponential calculations
num = st.number_input("Enter a number for logarithm and exponentiation:", value=1.0)
base = st.number_input("Enter the base for logarithm:", value=10.0)

# Logarithm and exponential calculations
log_val = math.log(num, base)
exp_val = math.exp(num)

st.write(f"log({num}, {base}) = {log_val}")
st.write(f"exp({num}) = {exp_val}")

# Square root calculation
sqrt_val = math.sqrt(num)
st.write(f"sqrt({num}) = {sqrt_val}")

# Factorial calculation (only for non-negative integers)
if num.is_integer() and num >= 0:
    fact_val = math.factorial(int(num))
    st.write(f"{int(num)}! = {fact_val}")