import streamlit as st
import sympy as sp

st.set_page_config(page_title="Integral Calculator", page_icon="∫", layout="centered")
st.title("🧮 Integral Calculator")

# Input section
integral_type = st.radio("Choose the type of integral:", ["Indefinite Integral", "Definite Integral"])

equation_input = st.text_input("Enter the function (e.g., x^3 + ln(x) - 5/x):")

x = sp.Symbol('x')

# Safely parse equation
def parse_equation(eq_str):
    try:
        eq_str = eq_str.replace('^', '**')
        expr = sp.sympify(eq_str, locals={"ln": sp.ln, "log": sp.log})
        return expr
    except Exception as e:
        st.error(f"Invalid function input. Error: {e}")
        return None

if integral_type == "Definite Integral":
    col1, col2 = st.columns(2)
    with col1:
        lower = st.text_input("Lower bound:")
    with col2:
        upper = st.text_input("Upper bound:")

    if st.button("Calculate Definite Integral"):
        expr = parse_equation(equation_input)
        if expr is not None and lower and upper:
            try:
                a = float(sp.sympify(lower))
                b = float(sp.sympify(upper))
                result = sp.integrate(expr, (x, a, b))
                st.success(f"∫ from {a} to {b} of f(x) dx = {result.evalf()}")
            except Exception as e:
                st.error(f"Error in calculation: {e}")

else:
    if st.button("Calculate Indefinite Integral"):
        expr = parse_equation(equation_input)
        if expr is not None:
            try:
                result = sp.integrate(expr, x)
                st.success(f"∫ f(x) dx = {result} + C")
            except Exception as e:
                st.error(f"Error in calculation: {e}")
