import streamlit as st
import random
import string


def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    st.title("Password Generator")

    length = st.number_input("Enter the length of the password:", min_value=4, max_value=50, step=1, value=8)
    complexity = st.selectbox("Select complexity level:", ['Low', 'Medium', 'High'])

    # Generate password on button click
    if st.button("Generate Password"):
        generated_password = generate_password(length, complexity)
        st.success(f"Generated Password: {generated_password}")

    st.markdown("---")

if __name__ == "__main__":
    main()
