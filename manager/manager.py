import streamlit as st
import pandas as pd
import PIL

global checkbox_num
if "checkbox_num" not in st.session_state:
    st.session_state.checkbox_num = 0

global event_title
if "event_title" not in st.session_state:
    st.session_state.event_title = []



def main(): 
    setup()
    button()
    checkbox()
    
    
# Sets up webpage
def setup():
    st.title("To-do List🚀")

def button():
    events = st.text_input("Event name 👇", placeholder = "+ Add Task", key = "event").strip()
    if events:
        st.session_state.event_title.append(events)
        st.session_state.checkbox_num += 1
        

                        
def checkbox():
    for i in range(st.session_state.checkbox_num):
        try:
            st.checkbox(st.session_state.event_title[i], key = f"task_{i}")
        except IndexError:
            pass

#
#def checked():
#    for j in range(st.session_state.checkbox_num):
#        if st.session_state[f"task_{j}"]:
#           st.session_state.visibility[j] = "hidden"
#
        

if __name__ == "__main__":
    main()


''' 
What to do:
1. Make it so that enter also clears the text box
2. Add maybe additional features, like editing a current item.
3. Add additional information, like date, time, ect....
4. If time, implment the CSV and txt's permenant memory.
5. Cool, random features, like a timer?
'''