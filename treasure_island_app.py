import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️", layout="centered")

# Basic CSS to give it some style
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: #ffffff;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff512f, #dd2476);
        color: white;
        border-radius: 10px;
        padding: 0.75em 1.5em;
        font-size: 1.2em;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏝️ Welcome to Treasure Island")
st.markdown("### Your mission is to find the hidden treasure!")

if "step" not in st.session_state:
    st.session_state.step = 1

def reset_game():
    st.session_state.step = 1

if st.button("🔄 Restart Game"):
    reset_game()

# STEP 1
if st.session_state.step == 1:
    st.markdown("You're in the middle of a roadcross.")
    if st.button("Go Left"):
        st.session_state.step = 2
        st.experimental_rerun()
    if st.button("Go Right"):
        st.error("You fall into a hole. **Game Over!**")

# STEP 2
elif st.session_state.step == 2:
    st.markdown("You've reached a lake. What will you do?")
    if st.button("🏊 Swim"):
        st.error("You got attacked by a crocodile. **Game Over!**")
    if st.button("⛵ Wait for a Boat"):
        st.session_state.step = 3
        st.experimental_rerun()

# STEP 3
elif st.session_state.step == 3:
    st.markdown("A boat arrives. You reach an island with 4 magical doors.")
    st.markdown("Which one will you choose?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚪 Red"):
            st.error("Burned by fire. **Game Over!**")
        if st.button("🚪 Yellow"):
            st.success("🎉 You found the treasure! You win!")
            st.balloons()
    with col2:
        if st.button("🚪 White"):
            st.error("You opened Heaven's Gate and fell. **Game Over!**")
        if st.button("🚪 Blue"):
            st.session_state.step = 2
            st.info("You are sent back to the lake.")
            st.experimental_rerun()
