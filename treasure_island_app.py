import streamlit as st

# Config
st.set_page_config(page_title="Treasure Island", page_icon="🏝️", layout="centered")

# Theme
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

# Title
st.title("🏝️ Treasure Island Adventure")
st.markdown("### Your mission is to find the hidden treasure!")

# Game state
if "step" not in st.session_state:
    st.session_state.step = 1
if "message" not in st.session_state:
    st.session_state.message = ""

# Reset game
if st.button("🔄 Restart Game"):
    st.session_state.step = 1
    st.session_state.message = ""

# Scene 1
if st.session_state.step == 1:
    st.markdown("You're in the middle of a roadcross.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go Left"):
            st.session_state.step = 2
    with col2:
        if st.button("Go Right"):
            st.session_state.message = "💀 You fall into a hole. **Game Over!**"
            st.session_state.step = 99

# Scene 2
elif st.session_state.step == 2:
    st.markdown("You've reached a lake. What will you do?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏊 Swim"):
            st.session_state.message = "🐊 Attacked by a crocodile. **Game Over!**"
            st.session_state.step = 99
    with col2:
        if st.button("⛵ Wait for a Boat"):
            st.session_state.step = 3

# Scene 3
elif st.session_state.step == 3:
    st.markdown("A boat arrives. You reach an island with 4 magical doors. Which one do you choose?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚪 Red"):
            st.session_state.message = "🔥 Burned by fire. **Game Over!**"
            st.session_state.step = 99
        if st.button("🚪 Yellow"):
            st.session_state.message = "🎉 You found the treasure! **You Win!**"
            st.balloons()
            st.session_state.step = 99
    with col2:
        if st.button("🚪 White"):
            st.session_state.message = "😇 You opened Heaven's Gate and fell. **Game Over!**"
            st.session_state.step = 99
        if st.button("🚪 Blue"):
            st.session_state.message = "🔁 You are sent back to the lake."
            st.session_state.step = 2

# Final screen
if st.session_state.step == 99:
    st.markdown("### " + st.session_state.message)
