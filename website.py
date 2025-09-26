import streamlit as st
from datetime import datetime

# ---------- Page Setup ----------
st.set_page_config(
    page_title="Happy Birthday 💖",
    page_icon="🎂",
    layout="centered"
)

# ---------- Custom Styling ----------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #ffe6f0, #fff7e6);
    }
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    html, body, [class*="css"] {
        font-family: 'Pacifico', cursive;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Background Music ----------
# Local audio file path
audio_file = r"song.mp3"

# Open and play the audio
with open(audio_file, "rb") as f:
    audio_bytes = f.read()

st.audio(audio_bytes, format="audio/mp3")


# ---------- Main Content ----------
st.title("🎉 Happy Birthday, Bibiiiii! 💕")
st.balloons()

st.image(
    r"IMG-20250202-WA0028(1).jpg",
    caption="Wishing you the happiest day ever!",
    use_container_width=True
)
# Birthday message
st.markdown(
    """
    <div style="text-align: center; font-size: 22px; color: #fdfbd4;">
        <p>Heyluuuuu, 💖</p>
        <p>I just want to remind you how much you mean to me.</p>
        <p>You make my world brighter, happier, and more beautiful every single day. 🌸</p>
        <p>Your'e my whole andd your'e my everythingggggg. ✨</p>
        <p><b>Happy Birthday, Eektikaaa! 🎂🎁</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Countdown ----------
today = datetime.now().date()
next_birthday = datetime(2026, 9, 26).date()  # Replace with her actual birthday

if today > next_birthday:
    next_birthday = datetime(today.year + 1, 9, 27).date()

days_left = (next_birthday - today).days

# Centered countdown
st.markdown(
    f"""
    <div style="text-align: center; font-size: 24px; color: #ff4b6e;">
        🎈 Only {days_left} days until your next birthday! 🎈
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Footer ----------
st.markdown(
    """
    <hr>
    <div style="text-align: center; color: #888; font-size: 16px;">
        Made with ❤️ By yours and yours only
    </div>
    """,
    unsafe_allow_html=True
)


