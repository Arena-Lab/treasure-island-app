import streamlit as st
import random

# Set page config
st.set_page_config(page_title="The Curse of the 10 Temples", page_icon="🏝️", layout="centered")

# Initialize game state
if "level" not in st.session_state:
    st.session_state.level = 1
if "message" not in st.session_state:
    st.session_state.message = ""
if "lives" not in st.session_state:
    st.session_state.lives = 3
if "pending_level" not in st.session_state:
    st.session_state.pending_level = None

# UI Theme
st.markdown("""
<style>
html, body {
    background: linear-gradient(to right, #1e2a38, #0f1117);
    color: white;
    font-family: 'Trebuchet MS', sans-serif;
}
.stButton>button {
    background: linear-gradient(to right, #f7971e, #ffd200);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.6em 1.5em;
}
</style>
""", unsafe_allow_html=True)

# Header & Restart
st.title("🏝️ The Curse of the 10 Temples")
st.markdown(f"### Temple {st.session_state.level}/10")
st.progress((st.session_state.level - 1) / 10)
st.markdown(f"💖 Lives Left: {st.session_state.lives}")

if st.button("🔄 Restart Game"):
    st.session_state.level = 1
    st.session_state.message = ""
    st.session_state.lives = 3

# Game flow control (safer than rerun)
if st.session_state.pending_level:
    st.session_state.level = st.session_state.pending_level
    st.session_state.pending_level = None

# Game over handler
def game_over(reason):
    st.error(reason)
    st.session_state.lives -= 1
    if st.session_state.lives <= 0:
        st.warning("💀 All lives lost. The curse has claimed you.")
        st.stop()

# ---- LEVELS ----

# Level 1
if st.session_state.level == 1:
    st.markdown("You're at a jungle crossroad 🌿. Which path do you take?")
    if st.button("⬅️ Left Path"):
        st.session_state.pending_level = 2
    elif st.button("➡️ Right Path"):
        game_over("A wild beast attacks from the trees!")

# Level 2
elif st.session_state.level == 2:
    st.markdown("You arrive at a lake 🐊. What do you do?")
    if st.button("⛵ Wait for boat"):
        st.session_state.pending_level = 3
    elif st.button("🏊 Swim"):
        game_over("Crocodiles drag you under!")

# Level 3
elif st.session_state.level == 3:
    st.markdown("You find 4 glowing doors in the temple.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔴 Red Door"):
            game_over("Flames erupt! 🔥")
        if st.button("🟡 Yellow Door"):
            st.session_state.pending_level = 4
    with col2:
        if st.button("⚪ White Door"):
            game_over("You vanish into the void!")
        if st.button("🔵 Blue Door"):
            st.session_state.pending_level = 2

# Level 4
elif st.session_state.level == 4:
    st.markdown("Temple 4: Puzzle of Mirrors 🪞")
    riddle = st.text_input("What speaks without a mouth and hears without ears?")
    if riddle.lower().strip() == "echo":
        st.success("Correct! A secret door slides open.")
        st.session_state.pending_level = 5
    elif riddle:
        game_over("Wrong answer! The room collapses.")

# Level 5
elif st.session_state.level == 5:
    st.markdown("Temple 5: 🌉 Trapped Bridge")
    choice = st.radio("Choose a plank:", ["Left", "Center", "Right"])
    safe = random.choice(["Left", "Center", "Right"])
    if st.button("Step forward"):
        if choice == safe:
            st.success("You crossed safely!")
            st.session_state.pending_level = 6
        else:
            game_over("Plank breaks! You fall.")

# Level 6
elif st.session_state.level == 6:
    st.markdown("Temple 6: 🧭 Sand Maze")
    direction = st.selectbox("Choose direction:", ["North", "South", "East", "West"])
    if st.button("Walk"):
        if direction == "North":
            st.session_state.pending_level = 7
        else:
            game_over("You wander endlessly.")

# Level 7
elif st.session_state.level == 7:
    st.markdown("Temple 7: 🪨 Ancient Glyphs")
    symbol = st.radio("Choose the correct glyph:", ["🌀", "🔺", "⏳", "☠️"])
    if st.button("Place glyph"):
        if symbol == "🔺":
            st.success("The gate unlocks!")
            st.session_state.pending_level = 8
        else:
            game_over("Gas fills the room!")

# Level 8
elif st.session_state.level == 8:
    st.markdown("Temple 8: Echo Chamber 🔊")
    code = st.text_input("Repeat this pattern: boom clap boom boom clap")
    if st.button("Echo"):
        if code.lower().strip() == "boom clap boom boom clap":
            st.session_state.pending_level = 9
        else:
            game_over("The walls close in...")

# Level 9
elif st.session_state.level == 9:
    st.markdown("Temple 9: ⚔️ Guardian Duel")
    player = st.radio("Choose your move:", ["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    enemy = random.choice(["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    if st.button("Attack!"):
        if player == enemy:
            st.success("Perfect counter!")
            st.session_state.pending_level = 10
        else:
            game_over(f"The guardian used {enemy}. You fall!")

# Level 10
elif st.session_state.level == 10:
    st.balloons()
    st.success("🎉 You've conquered the 10 temples!")
    st.markdown("🏆 The **Treasure of the Ancients** is yours.")
