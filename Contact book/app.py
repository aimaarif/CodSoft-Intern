import streamlit as st

# Function to initialize contact book
def initialize_contact_book():
    if 'contacts' not in st.session_state:
        st.session_state.contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    st.session_state.contacts.append(contact)
    st.success("Contact added successfully!")
    if st.success("Contact added successfully!"):
        st.session_state.add_contact_name = ""
        st.session_state.add_contact_phone = ""
        st.session_state.add_contact_email = ""
        st.session_state.add_contact_address = ""

# Function to display contact list
def view_contact_list():
    st.write("## Contact List")
    for i, contact in enumerate(st.session_state.contacts):
        st.write(f"**{i+1}. {contact['name']}**: {contact['phone']}")

# Function to search for a contact
def search_contact(query):
    results = []
    for contact in st.session_state.contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)
    return results

# Function to update a contact
def update_contact(index, name, phone, email, address):
    contact = st.session_state.contacts[index]
    contact['name'] = name
    contact['phone'] = phone
    contact['email'] = email
    contact['address'] = address
    st.success("Contact updated successfully!")

# Function to delete a contact
def delete_contact(index):
    del st.session_state.contacts[index]
    st.success("Contact deleted successfully!")

# Streamlit UI with styling and interactivity
def main():
    st.title("Contact Book")

    # Initialize contact book
    initialize_contact_book()

    # Sidebar menu
    menu = st.sidebar.selectbox("Menu", ['Add Contact', 'View Contact List', 'Search Contact', 'Update Contact', 'Delete Contact'])

    # Add Contact
    if menu == 'Add Contact':
        st.sidebar.write("## Add Contact")
        name = st.sidebar.text_input("Name")
        phone = st.sidebar.text_input("Phone")
        email = st.sidebar.text_input("Email")
        address = st.sidebar.text_area("Address")
        if st.sidebar.button("Add"):
            add_contact(name, phone, email, address)

    # View Contact List
    elif menu == 'View Contact List':
        view_contact_list()

    # Search Contact
    elif menu == 'Search Contact':
        st.sidebar.write("## Search Contact")
        query = st.sidebar.text_input("Search by name or phone number")
        if st.sidebar.button("Search"):
            results = search_contact(query)
            if results:
                st.write("## Search Results")
                for result in results:
                    st.write(f"**Name:** {result['name']}, **Phone:** {result['phone']}, **Email:** {result['email']}, **Address:** {result['address']}")
            else:
                st.warning("No contacts found.")

    # Update Contact
    elif menu == 'Update Contact':
        st.sidebar.write("## Update Contact")
        index = st.sidebar.number_input("Enter index of contact to update", min_value=1, max_value=len(st.session_state.contacts), step=1)
        if st.sidebar.button("Select"):
            contact = st.session_state.contacts[index - 1]
            name = st.sidebar.text_input("Name", contact['name'])
            phone = st.sidebar.text_input("Phone", contact['phone'])
            email = st.sidebar.text_input("Email", contact['email'])
            address = st.sidebar.text_area("Address", contact['address'])
            if st.sidebar.button("Update"):
                update_contact(index - 1, name, phone, email, address)

    # Delete Contact
    elif menu == 'Delete Contact':
        st.sidebar.write("## Delete Contact")
        index = st.sidebar.number_input("Enter index of contact to delete", min_value=1, max_value=len(st.session_state.contacts), step=1)
        if st.sidebar.button("Delete"):
            delete_contact(index - 1)

if __name__ == "__main__":
    main()
