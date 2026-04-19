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

global event_date
if "event_date" not in st.session_state:
    st.session_state.event_date = []

global priority
if "priority" not in st.session_state:
    st.session_state.priority = []

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
        dates = st.date_input("Event date 👇", format = "MM/DD/YYYY", key = "date")
        priorites = st.segmented_control("Priority⚠️", options = ["Low", "Medium", "High"], selection_mode = "single", key = "priority"), 
        if add_event and not len(st.session_state.event) == 0:
            with open("todo.txt", "a") as file:
                file.write(f"{events}\n")
            with open("date.txt", "a") as file:
                file.write(f"{dates}\n")
            with open("priority.txt", "a") as file:
                file.write(f"{priorites}\n")
            st.session_state.checkbox_num += 1
            st.toast("Your event has been added!", icon = "👍", duration = 1)
            

                        
    def checkbox():
        with open("todo.txt", "r") as file:
            st.session_state.event_title = file.readlines()
        with open("delete.txt", "r") as file:
            try:
                st.session_state.delete_list = file.readlines()
                st.session_state.delete_list = [int(item.strip()) for item in st.session_state.delete_list]
            except ValueError:
                pass
        with open("date.txt", "r") as file:
            st.session_state.event_date = file.readlines()
        with open("priority.txt", "r") as file:
            for line in file.readlines():
                if line == "Low":
                    st.session_state.priority.append("Low")
                elif line == "Medium":
                    st.session_state.priority.append("Medium")
                elif line == "High":
                    st.session_state.priority.append("High")
                else:
                    st.session_state.priority.append("Nothing")
        for i in range(st.session_state.checkbox_num):
            try:
                if i not in st.session_state.delete_list:
                    st.checkbox(f"{st.session_state.event_title[i]} :orange-badge[{st.session_state.event_date[i]}]", key = f"task_{i}", on_change = checked, args = (f"task_{i}", ))
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
        with open("date.txt", "r") as file:
            lines = file.readlines()
            lines[number] = f"\n"
        with open("date.txt", "w") as file:
            file.writelines(lines)
        with open("priority.txt", "r") as file:
            lines = file.readlines()
            lines[number] = f"\n"
        with open("priority.txt", "w") as file:
            file.writelines(lines)


if __name__ == "__main__":
    main()


