import streamlit as st
import random

# Config
st.set_page_config(page_title="Treasure Island", page_icon="🏝️", layout="centered")

# Initialize session state
if "level" not in st.session_state:
    st.session_state.level = 1
if "lives" not in st.session_state:
    st.session_state.lives = 3

# Styles
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
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# UI Header
st.title("🏝️ The Curse of the 10 Temples")
st.markdown(f"### Temple {st.session_state.level}/10")
st.progress((st.session_state.level - 1) / 10)
st.markdown(f"💖 Lives Left: {st.session_state.lives}")

# Restart
if st.button("🔄 Restart Game"):
    st.session_state.level = 1
    st.session_state.lives = 3
    st.experimental_rerun()

# Game over
def game_over(message):
    st.error(message)
    st.session_state.lives -= 1
    if st.session_state.lives <= 0:
        st.warning("💀 You've lost all your lives. The curse wins!")
        st.stop()
    st.experimental_rerun()

# Advance level
def advance(level_up):
    st.session_state.level = level_up
    st.experimental_rerun()

# Level 1
if st.session_state.level == 1:
    st.markdown("You're at a jungle crossroad 🌿. Which path do you take?")
    if st.button("⬅️ Left Path"):
        advance(2)
    elif st.button("➡️ Right Path"):
        game_over("A wild beast ambushes you!")

# Level 2
elif st.session_state.level == 2:
    st.markdown("You arrive at a lake 🐊. What do you do?")
    if st.button("⛵ Wait for the boat"):
        advance(3)
    elif st.button("🏊 Swim"):
        game_over("Crocodiles drag you under!")

# Level 3
elif st.session_state.level == 3:
    st.markdown("You find 4 glowing doors.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔴 Red Door"):
            game_over("Flames erupt! 🔥")
        if st.button("🟡 Yellow Door"):
            advance(4)
    with col2:
        if st.button("⚪ White Door"):
            game_over("You vanish into the void!")
        if st.button("🔵 Blue Door"):
            advance(2)

# Level 4
elif st.session_state.level == 4:
    st.markdown("Temple 4: 🪞 Puzzle of Mirrors")
    riddle = st.text_input("🧠 What speaks without a mouth and hears without ears?")
    if riddle:
        if riddle.strip().lower() == "echo":
            st.success("Correct! A secret door opens.")
            if st.button("➡️ Continue to next level"):
                advance(5)
        else:
            game_over("Wrong answer! The room collapses.")

# Level 5
elif st.session_state.level == 5:
    st.markdown("Temple 5: 🌉 Trapped Bridge")
    choice = st.radio("Choose a plank to step on:", ["Left", "Center", "Right"])
    safe = random.choice(["Left", "Center", "Right"])
    if st.button("Step Forward"):
        if choice == safe:
            st.success("You crossed safely.")
            advance(6)
        else:
            game_over("Plank breaks! You fall.")

# Level 6
elif st.session_state.level == 6:
    st.markdown("Temple 6: 🧭 Sand Maze")
    direction = st.selectbox("Choose a direction:", ["North", "East", "South", "West"])
    if st.button("🚶 Walk"):
        if direction == "North":
            advance(7)
        else:
            game_over("You got lost in the sands.")

# Level 7
elif st.session_state.level == 7:
    st.markdown("Temple 7: 🪨 Ancient Glyphs")
    glyph = st.radio("Choose the correct glyph:", ["🌀", "🔺", "⏳", "☠️"])
    if st.button("Place Glyph"):
        if glyph == "🔺":
            st.success("The gate opens!")
            advance(8)
        else:
            game_over("Wrong glyph! Poison gas fills the room.")

# Level 8
elif st.session_state.level == 8:
    st.markdown("Temple 8: 🔊 Cave of Echoes")
    pattern = st.text_input("Repeat the pattern: `boom clap boom boom clap`")
    if pattern:
        if pattern.strip().lower() == "boom clap boom boom clap":
            st.success("Perfect memory! The cave opens.")
            if st.button("🎵 Continue"):
                advance(9)
        else:
            game_over("Wrong pattern! The cave collapses.")

# Level 9
elif st.session_state.level == 9:
    st.markdown("Temple 9: ⚔️ The Final Duel")
    move = st.radio("Choose your move:", ["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    enemy = random.choice(["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    if st.button("Fight!"):
        if move == enemy:
            st.success("You matched the guardian’s move and passed!")
            advance(10)
        else:
            game_over(f"The guardian used {enemy}. You fall!")

# Level 10
elif st.session_state.level == 10:
    st.balloons()
    st.success("🏆 You've conquered all 10 temples!")
    st.markdown("🎉 The **Treasure of the Ancients** is yours!")
    st.markdown("🔁 Click **Restart Game** above to play again.")
