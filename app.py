
import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('mental_model.pkl', 'rb'))

# Streamlit Page Settings
st.set_page_config(page_title="Mental Fitness Checker", layout="centered")
st.title("🧠 Mental Fitness Checker")
st.subheader("Find out how you're doing mentally based on your daily habits.")

# Input Sliders
sleep = st.slider("Sleep Hours (per day)", 0, 10, 6)
screen = st.slider("Screen Time (hours)", 0, 12, 4)
activity = st.selectbox("Physical Activity", [0, 1, 2], format_func=lambda x: ['None', 'Walk', 'Workout'][x])
stress = st.slider("Stress Level (1 = Low, 5 = High)", 1, 5, 3)
focus = st.slider("Focus Level (1 = Poor, 5 = Excellent)", 1, 5, 3)

# Predict button
if st.button("Check My Mental Status"):
    prediction = model.predict([[sleep, screen, activity, stress, focus]])
    status = prediction[0]

    if status == "Fine":
        st.success("✅ You're doing fine! Keep it up 😇")
    elif status == "Needs Break":
        st.warning("⚠️ You might need a short break. Try relaxing activities ☕")
    else:
        st.error("❌ You're feeling stressed. Consider rest and talk to someone 💬")

