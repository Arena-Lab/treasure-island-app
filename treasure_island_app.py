
import streamlit as st
import random

# Config
st.set_page_config(page_title="Treasure Island", page_icon="🏝️", layout="centered")

# Init session state
for key, default in {
    "level": 1,
    "lives": 3,
    "next_level": None,
    "game_over": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# --- HANDLE NEXT LEVEL ---
if st.session_state.next_level:
    st.session_state.level = st.session_state.next_level
    st.session_state.next_level = None
    st.rerun()

# --- HANDLE GAME OVER ---
if st.session_state.game_over:
    st.session_state.lives -= 1
    if st.session_state.lives <= 0:
        st.error("💀 All lives lost. The curse wins!")
        st.stop()
    else:
        st.error(f"⚠️ {st.session_state.game_over}")
    st.session_state.game_over = None
    st.rerun()

# --- FUNCTIONS ---
def advance(level):
    st.session_state.next_level = level

def fail(reason):
    st.session_state.game_over = reason

# --- UI STYLE ---
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

# --- HEADER ---
st.title("🏝️ The Curse of the 10 Temples")
st.markdown(f"### Temple {st.session_state.level}/10")
st.progress((st.session_state.level - 1) / 10)
st.markdown(f"💖 Lives Left: {st.session_state.lives}")

# --- RESTART BUTTON ---
if st.button("🔄 Restart Game"):
    st.session_state.level = 1
    st.session_state.lives = 3
    st.session_state.game_over = None
    st.session_state.next_level = None
    st.rerun()

# --- LEVELS ---
level = st.session_state.level

if level == 1:
    st.markdown("You're at a jungle crossroad 🌿. Which path do you take?")
    if st.button("⬅️ Left Path"):
        advance(2)
    elif st.button("➡️ Right Path"):
        fail("A wild beast ambushes you!")

elif level == 2:
    st.markdown("You arrive at a lake 🐊. What do you do?")
    if st.button("⛵ Wait for the boat"):
        advance(3)
    elif st.button("🏊 Swim"):
        fail("Crocodiles drag you under!")

elif level == 3:
    st.markdown("You find 4 glowing doors.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔴 Red Door"):
            fail("Flames erupt! 🔥")
        if st.button("🟡 Yellow Door"):
            advance(4)
    with col2:
        if st.button("⚪ White Door"):
            fail("You vanish into the void!")
        if st.button("🔵 Blue Door"):
            advance(2)

elif level == 4:
    st.markdown("Temple 4: 🪞 Puzzle of Mirrors")
    riddle = st.text_input("🧠 What speaks without a mouth and hears without ears?")
    if riddle:
        if riddle.strip().lower() == "echo":
            st.success("Correct! A secret door opens.")
            if st.button("➡️ Continue"):
                advance(5)
        else:
            fail("Wrong answer! The room collapses.")

elif level == 5:
    st.markdown("Temple 5: 🌉 Trapped Bridge")
    choice = st.radio("Choose a plank:", ["Left", "Center", "Right"])
    safe = random.choice(["Left", "Center", "Right"])
    if st.button("Step Forward"):
        if choice == safe:
            st.success("You crossed safely.")
            advance(6)
        else:
            fail("Plank breaks! You fall.")

elif level == 6:
    st.markdown("Temple 6: 🧭 Sand Maze")
    direction = st.selectbox("Choose a direction:", ["North", "East", "South", "West"])
    if st.button("🚶 Walk"):
        if direction == "North":
            advance(7)
        else:
            fail("You got lost in the sands.")

elif level == 7:
    st.markdown("Temple 7: 🪨 Ancient Glyphs")
    glyph = st.radio("Choose the correct glyph:", ["🌀", "🔺", "⏳", "☠️"])
    if st.button("Place Glyph"):
        if glyph == "🔺":
            st.success("The gate opens!")
            advance(8)
        else:
            fail("Wrong glyph! Poison gas fills the room.")

elif level == 8:
    st.markdown("Temple 8: 🔊 Cave of Echoes")
    pattern = st.text_input("Repeat this pattern: boom clap boom boom clap")
    if pattern:
        if pattern.strip().lower() == "boom clap boom boom clap":
            st.success("Perfect memory! The cave opens.")
            if st.button("🎵 Continue"):
                advance(9)
        else:
            fail("Wrong pattern! The cave collapses.")

elif level == 9:
    st.markdown("Temple 9: ⚔️ The Final Duel")
    move = st.radio("Choose your move:", ["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    enemy = random.choice(["Strike ⚔️", "Dodge 🌀", "Spell ✨"])
    if st.button("Fight!"):
        if move == enemy:
            st.success("You matched the guardian’s move and passed!")
            advance(10)
        else:
            fail(f"The guardian used {enemy}. You fall!")

elif level == 10:
    st.balloons()
    st.success("🏆 You've conquered all 10 temples!")
    st.markdown("🎉 The **Treasure of the Ancients** is yours!")
    st.markdown("🔁 Click **Restart Game** above to play again.")
