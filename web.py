import streamlit as st
from Modules import functions as fn

todos = fn.get_todos()

def add_todo():
    new_todo = st.session_state["todo"]
    todos.append(new_todo + "\n")
    fn.write_todos(todos)


st.title("My Todo Web App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,  key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add todo", placeholder="Add new todo....",
              on_change=add_todo, key="todo")
