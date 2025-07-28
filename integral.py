import streamlit as st
import sympy as sp

# Set up Streamlit page
st.set_page_config(page_title="Integral Calculator", page_icon="∫", layout="centered")
st.title("🧮 Integral Calculator")

# Integral type selection
integral_type = st.radio("Choose the type of integral:", ["Indefinite Integral", "Definite Integral"])

# Input function
equation_input = st.text_input("Enter the function (e.g., x^3 + ln(x) - 5/x):")

# Symbol definition
x = sp.Symbol('x')

# Function to safely parse equation
def parse_equation(eq_str):
    try:
        eq_str = eq_str.replace('^', '**')
        expr = sp.sympify(eq_str, locals={"ln": sp.ln, "log": sp.log})
        return expr
    except Exception as e:
        st.error(f"Invalid function input. Error: {e}")
        return None

# Definite Integral
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
                st.latex(rf"\int_{{{a}}}^{{{b}}} f(x)\, dx = {sp.latex(result)}")
            except Exception as e:
                st.error(f"Error in calculation: {e}")

# Indefinite Integral
else:
    if st.button("Calculate Indefinite Integral"):
        expr = parse_equation(equation_input)
        if expr is not None:
            try:
                result = sp.integrate(expr, x)
                st.latex(rf"\int f(x)\, dx = {sp.latex(result)} + C")
            except Exception as e:
                st.error(f"Error in calculation: {e}")
