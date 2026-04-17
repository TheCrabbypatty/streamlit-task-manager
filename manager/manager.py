import streamlit as st
import pandas as pd

global checkbox_num
if "checkbox_num" not in st.session_state:
    with open("todo.txt", "r") as file:
        l = file.readlines()
    st.session_state.checkbox_num = len(l)

global event_title
if "event_title" not in st.session_state:
    st.session_state.event_title = []

global delete_list
if "delete_list" not in st.session_state:
    st.session_state.delete_list = []


def main(): 
    setup()
    button()
    checkbox()
    
    
# Sets up webpage
def setup():
    st.title("To-do List🚀")

col1, col2 = st.columns(2)

with col1:
    def button():
        add_event = st.button("Add event!", key = "add")
        events = st.text_input("Event name 👇", placeholder = "+ Add Task", key = "event").strip()
        if add_event and not len(st.session_state.event) == 0:
            with open("todo.txt", "a") as file:
                file.write(f"{events}\n")
            st.session_state.checkbox_num += 1
            st.toast("Your event has been added!", icon = "👍", duration = 1)
            

                        
    def checkbox():
        with open("todo.txt", "r") as file:
            st.session_state.event_title = file.readlines()
        with open("delete.txt", "r") as file:
            st.session_state.delete_list = file.readlines()
            st.session_state.delete_list = [int(x.strip()) for x in file.readlines() if x.strip()]
        for i in range(st.session_state.checkbox_num):
            try:
                if i not in st.session_state.delete_list:
                    st.checkbox(st.session_state.event_title[i], key = f"task_{i}", on_change = checked, args = (f"task_{i}", ))
            except IndexError:
                pass
            

    def checked(key):
        letter, number = key.split("_")
        number = int(number)
        with open("delete.txt", "a") as file:
            file.write(f"{number}\n")
        with open("todo.txt", "r") as file:
            lines = file.readlines()    
            lines[number] = f"\n"
        with open("todo.txt", "w") as file:
            file.writelines(lines)


if __name__ == "__main__":
    main()


''' 
What to do:
1. ~Make it so that enter also clears the text box~
2. Add maybe additional features, like editing a current item.
3. Add additional information, like date, time, ect....
4. If time, implment the CSV and txt's permenant memory.
5. Cool, random features, like a timer?
'''