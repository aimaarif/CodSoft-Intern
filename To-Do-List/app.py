import streamlit as st
from datetime import datetime

def main():
    st.set_page_config(page_title="To-do-list", layout="wide", page_icon=":clipboard:") 
    st.title("📋 To Do List Manager")

    tasks = st.session_state.get('tasks', [])

    col1, col2, _ = st.columns([3, 4, 1])  

    with col1:
        st.header("Add your tasks here...")
        task_input = st.text_input("Enter your Task")
        due_date = st.date_input("Due Date", min_value=datetime.today())

        if st.button("Add Task", key="add_task_button"):
            if task_input:
                tasks.append({"task": task_input, "due_date": due_date, "done": False})
                st.session_state.tasks = tasks
                st.success("Task added successfully...")
            else:
                st.error("Please enter a task...")

    with col2:
        st.header("Your Tasks")
        if not tasks:
            st.write("No tasks...")
        else:
            for idx, task in enumerate(tasks, 1):
                task_done = st.checkbox(task["task"], value=task["done"], key=idx)
                tasks[idx - 1]["done"] = task_done
                st.write(f"**Due Date:** {task['due_date'].strftime('%Y-%m-%d')}")

        if st.button("Delete Completed Tasks"):
            tasks = [task for task in tasks if not task["done"]]
            st.session_state.tasks = tasks
            st.success("Completed tasks are deleted successfully...")

if __name__ == "__main__":
    main()

st.markdown("""<div style='padding-top: 20px; text-align: center;'>

</div>""", unsafe_allow_html=True)
