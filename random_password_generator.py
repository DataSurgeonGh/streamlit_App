import string
import random
import streamlit as st

# Generate lowercase & uppercase letters
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
#create empty list, append each member of upper and lowercase  into list
letter_ = [str(letters) for letters in lowercase_letters] + [str(letter) for letter in uppercase_letters]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','_','+']

st.title("PyPassword Generator")

number_of_letters = st.number_input('How many letters do you want in your password', min_value=1, step=1)
number_of_symbols = st.number_input('How many symbols do you want in your password', min_value=1, step=1)
number_of_numbers = st.number_input('How many numbers do you want in your password', min_value=1, step=1)

password = []

for _ in range(number_of_letters):
    password.append(random.choice(letter_))

for _ in range(number_of_symbols):
    password.append(random.choice(symbols))

for _ in range(number_of_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

password = "".join(password)


#st.write(f"Your generated password is: {password}")
#st.text_area("Generated Password:", value=password, height=1, max_chars=None)


# Add a button with text
if st.button('Click here to generate password'):
    st.text_area("Generated Password:", value=password, height=1, max_chars=None)
    st.write('Password generated successfully!')
