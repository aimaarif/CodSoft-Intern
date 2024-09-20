import streamlit as st

# Function to perform arithmetic operations
def perform_operation(num1, num2, operation):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

def main():
    st.title("Calculator")

    num1 = st.number_input("Enter the first number:", step=1, format="%d", key="num1")
    num2 = st.number_input("Enter the second number:", step=1, format="%d", key="num2")
    operation = st.selectbox("Select operation:", ['Addition', 'Subtraction', 'Multiplication', 'Division'])

    # Perform calculation on button click
    if st.button("Calculate", key="calculate_btn"):
        with st.spinner("Calculating..."):
            result = perform_operation(num1, num2, operation)
            st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
