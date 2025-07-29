import streamlit as st
import time
import random

# Setup
st.set_page_config(page_title="The Curse of the 10 Temples", page_icon="🏝️", layout="centered")

# Initialize session state
if "level" not in st.session_state:
    st.session_state.level = 1
if "message" not in st.session_state:
    st.session_state.message = ""
if "lives" not in st.session_state:
    st.session_state.lives = 3

# Restart Game
if st.button("🔁 Restart Game"):
    st.session_state.level = 1
    st.session_state.message = ""
    st.session_state.lives = 3

# Styles
st.markdown("""
    <style>
    html, body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(to right, #f7971e, #ffd200);
        color: black;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        margin-top: 10px;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    .emoji {
        font-size: 60px;
        text-align: center;
    }
    .center {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='center'>🏝️ The Curse of the 10 Temples</h1>", unsafe_allow_html=True)
st.markdown(f"### ⛩️ Temple {st.session_state.level} / 10")
st.progress((st.session_state.level - 1) / 10)
st.markdown(f"💖 Lives Remaining: {st.session_state.lives}")

# Game reset on Game Over
def game_over(msg):
    st.error(msg)
    st.session_state.lives -= 1
    if st.session_state.lives <= 0:
        st.markdown("💀 You've lost all your lives. The curse has claimed you!")
        st.stop()

# Level advancement
def next_level(level_up, msg=""):
    st.session_state.level = level_up
    st.session_state.message = msg
    time.sleep(1)
    st.experimental_rerun()

# LEVEL 1
if st.session_state.level == 1:
    st.markdown("You're at a jungle crossroad 🌿. Which path do you take?")
    if st.button("⬅️ Left (toward the mountains)"):
        next_level(2, "You reach a mysterious lake 🐊.")
    if st.button("➡️ Right (into the dark woods)"):
        game_over("A wild beast ambushes you!")

# LEVEL 2
elif st.session_state.level == 2:
    st.markdown("You arrive at a deep, still lake. There's no bridge.")
    if st.button("⛵ Wait for the boat"):
        next_level(3, "A boat quietly arrives.")
    if st.button("🏊 Swim across"):
        game_over("Crocodiles devour you!")

# LEVEL 3
elif st.session_state.level == 3:
    st.markdown("The boat takes you to a giant stone gate with 4 glowing doors.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔴 Red Door"):
            game_over("Fire trap! 🔥")
        if st.button("🟡 Yellow Door"):
            next_level(4, "You've entered the Puzzle Temple.")
    with col2:
        if st.button("⚪ White Door"):
            game_over("Fell into endless void.")
        if st.button("🔵 Blue Door"):
            next_level(2, "Portal sends you back to the lake.")

# LEVEL 4
elif st.session_state.level == 4:
    st.markdown("Temple 4: 🧠 Puzzle of Mirrors")
    st.markdown("Solve this riddle: _I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?_")
    answer = st.text_input("Your answer:")
    if answer.lower().strip() == "echo":
        next_level(5, "Correct! A hidden door opens.")
    elif answer:
        game_over("Incorrect answer! The room collapses.")

# LEVEL 5
elif st.session_state.level == 5:
    st.markdown("Temple 5: 🌉 Trapped Bridge")
    st.markdown("Cross the bridge, but choose carefully.")
    choice = st.radio("Choose a plank to step on:", ["Left", "Center", "Right"])
    safe = random.choice(["Left", "Center", "Right"])
    if st.button("Step!"):
        if choice == safe:
            next_level(6, "You crossed safely.")
        else:
            game_over("Plank breaks! You fall into spikes.")

# LEVEL 6
elif st.session_state.level == 6:
    st.markdown("Temple 6: 🧭 Sand Maze")
    direction = st.selectbox("Which direction do you take?", ["North", "East", "South", "West"])
    if st.button("Walk"):
        if direction == "North":
            next_level(7, "You escape the maze!")
        else:
            game_over("You get lost in the sandstorm.")

# LEVEL 7
elif st.session_state.level == 7:
    st.markdown("Temple 7: 🪨 Ancient Glyphs")
    st.markdown("Match the correct symbol to unlock the gate:")
    glyph = st.radio("Choose:", ["🌀", "🔺", "⏳", "☠️"])
    if st.button("Place glyph"):
        if glyph == "🔺":
            next_level(8, "Gate opens with rumble.")
        else:
            game_over("Wrong glyph! Gas fills the room.")

# LEVEL 8
elif st.session_state.level == 8:
    st.markdown("Temple 8: 🔊 Cave of Echoes")
    pattern = st.text_input("Repeat the sound pattern: `Boom Clap Boom Boom Clap`")
    if st.button("Echo it"):
        if pattern.lower().strip() == "boom clap boom boom clap":
            next_level(9, "Cave vibrates and reveals a path.")
        else:
            game_over("You sang the wrong tune!")

# LEVEL 9
elif st.session_state.level == 9:
    st.markdown("Temple 9: ⚔️ The Final Duel")
    st.markdown("Defeat the guardian. Choose your move:")
    move = st.radio("Attack Type:", ["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    guardian_move = random.choice(["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    if st.button("Fight!"):
        if move == guardian_move:
            next_level(10, "You matched the guardian’s move and passed!")
        else:
            game_over(f"The guardian used {guardian_move}. You failed!")

# LEVEL 10
elif st.session_state.level == 10:
    st.balloons()
    st.success("🏆 You have passed all 10 temples!")
    st.markdown("🎉 You found the **Hidden Treasure of the Ancients**.")
    st.markdown("💬 Want 100 levels? Let me know!")
