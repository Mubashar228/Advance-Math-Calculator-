import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced Math Calculator", layout="wide")
st.title("🧮 Advanced Math Calculator by Mubashar Ul Hassan")

menu = st.sidebar.selectbox("Choose Operation", ["Basic Math", "Solve Equation", "Calculus", "Plot Graph"])

x = sp.Symbol('x')

if menu == "Basic Math":
    expr = st.text_input("Enter expression (e.g., 2 + 3 * (4 - 1))")
    if expr:
        try:
            result = eval(expr)
            st.success(f"Result: {result}")
        except:
            st.error("Invalid expression")

elif menu == "Solve Equation":
    equation = st.text_input("Enter equation (e.g., 2*x + 3 = 7)")
    if equation:
        try:
            lhs, rhs = equation.split('=')
            solution = sp.solve(sp.sympify(lhs) - sp.sympify(rhs), x)
            st.success(f"Solution: {solution}")
        except:
            st.error("Invalid equation format")

elif menu == "Calculus":
    calc_type = st.radio("Choose Operation", ["Derivative", "Integral"])
    func = st.text_input("Enter function of x (e.g., sin(x) + x**2)")

    if func:
        try:
            f = sp.sympify(func)
            if calc_type == "Derivative":
                st.success(f"f'(x) = {sp.diff(f, x)}")
            else:
                st.success(f"∫f(x) dx = {sp.integrate(f, x)} + C")
        except:
            st.error("Invalid function")

elif menu == "Plot Graph":
    func = st.text_input("Enter function of x to plot (e.g., sin(x), x**2 + 2*x)")
    if func:
        try:
            f = sp.lambdify(x, sp.sympify(func), "numpy")
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f(x_vals)

            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label=f"y = {func}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)
        except:
            st.error("Invalid function format")
