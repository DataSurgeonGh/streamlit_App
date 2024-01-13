import streamlit as st

#st.title("The streamlit App")

#st.write("This is not my first app in streamlit")

#st.markdown("### This is a markdown")

# pick = input("Enter the names of your friends seperated by comma")

# name = pick.split(",")

# random_nos = random.randint(0,len(name))
# print(name)
# print(f'There are {len(name)} of you at the table, and {name[random_nos-1]} will pay the bill! ')
import random

def main():
    st.title("Who Pays the Bill?")

    pick = st.text_input("Enter the names of your friends separated by comma:")
    
    if st.button("Pick"):
        names = pick.split(",")
        random_choice = random.choice(names)

        st.write(f'There are {len(names)} of you at the table, and {random_choice} will pay the bill!')

if __name__ == "__main__":
    main()
