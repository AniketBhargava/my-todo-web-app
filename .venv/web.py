import streamlit as st
import functions
todos=functions.get_todos()

def add_todo():
    todo=st.session_state['new_todo']+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo List")

for idx, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo  )
    if checkbox:
        todos.pop(idx)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",placeholder="Add New Todo",
              on_change=add_todo,key="new_todo")