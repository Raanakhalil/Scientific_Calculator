import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.title("🧮 Scientific Calculator")

# Input section
expression = st.text_input("Enter a mathematical expression:", value="")

# Safe dictionary of allowed functions and constants
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
allowed_names.update({
    "abs": abs,
    "round": round
})

def evaluate_expression(expr):
    try:
        result = eval(expr, {"__builtins__": {}}, allowed_names)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if expression:
    result = evaluate_expression(expression)
    st.write("### Result:")
    st.success(result)

st.markdown("""
**Examples of valid inputs:**
- `2 + 3 * 4`
- `sin(0.5)`
- `log(100, 10)`
- `sqrt(16)`
- `factorial(5)`
""")
