import random
import string
import streamlit as st

st.title("🔐 Secret Code Translator")

option = st.radio("Choose an action:", ["Encode", "Decode"])
message = st.text_input("Enter your message:")

if st.button("Translate"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        messages = message.split(" ")
        result = []

        if option == "Encode":
            for mess in messages:
                if len(mess) >= 3:
                    r1 = "".join(random.choices(string.ascii_lowercase, k=3))
                    r2 = "".join(random.choices(string.ascii_lowercase, k=3))
                    new_message = r1 + mess[1:] + mess[0] + r2
                    result.append(new_message)
                else:
                    result.append(mess[::-1])

        elif option == "Decode":
            for mess in messages:
                if len(mess) >= 3:
                    new_message = mess[3:-3]
                    new_message = new_message[-1] + new_message[:-1]
                    result.append(new_message)
                else:
                    result.append(mess[::-1])

        final_output = " ".join(result)
        st.success("Result:")
        st.code(final_output)
