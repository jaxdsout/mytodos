import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

st.set_page_config(layout="wide")
def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    write_todos(todos)


st.title("MyToDo's")
st.subheader("This is my app for organizing my tasks")
st.write("...hopefully it increases productivity.")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(
    label=' ',
    placeholder="enter in a new todo...",
    on_change=add_todo,
    key='new_todo'
)
