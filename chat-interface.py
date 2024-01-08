import streamlit as st

import hmac
import streamlit as st


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
with st.sidebar:
    possible_models = ["ChatGPT-4", "google bard", "?"]
    selected_model = st.selectbox("model_selector", possible_models, 0)

if "messages" not in st.session_state:
    messages = [{"role": "assistant", "message": "Hallo, wie kann ich dir helfen?"}]
    st.session_state["messages"] = messages


prompt = st.chat_input("Say something")
if prompt:
    st.session_state["messages"].append({"role": "user", "message": prompt})

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["message"])
