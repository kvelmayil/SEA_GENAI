import streamlit as st

# ---------------------- Quiz Data ----------------------
quiz_data = [
    {
        "question": "Which Indian standard covers the safety rules for the construction and installation of lifts?",
        "options": ["IS 17900", "IS 14665", "IS 875", "IS 456"],
        "answer": "IS 14665",
        "code": "IS 14665"
    },
    {
        "question": "IS 17900 is primarily associated with which of the following?",
        "options": [
            "Electric lift design specifications",
            "Installation of escalators",
            "Maintenance of elevators",
            "Safety code for lift usage and modernization"
        ],
        "answer": "Safety code for lift usage and modernization",
        "code": "IS 17900"
    },
    {
        "question": "Which IS code provides specifications for lift machine room requirements?",
        "options": ["IS 14665", "IS 17900", "IS 875", "IS 800"],
        "answer": "IS 14665",
        "code": "IS 14665"
    },
    {
        "question": "As per IS 17900, which aspect is emphasized most for modernization of elevators?",
        "options": ["Speed", "Aesthetics", "Safety", "Cost"],
        "answer": "Safety",
        "code": "IS 17900"
    },
    {
        "question": "Which IS code includes requirements for guide rails, counterweights, and buffers?",
        "options": ["IS 14665", "IS 17900", "IS 800", "IS 875"],
        "answer": "IS 14665",
        "code": "IS 14665"
    },
]

# ---------------------- App UI ----------------------
st.set_page_config(page_title="Elevator Quiz - IS14665 & IS17900", layout="centered")

st.title("🚀 Elevator Quiz")
st.markdown("Test your knowledge on IS14665 and IS17900 Elevator Codes")

# Session state to hold score and current question
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.answers = []

# ---------------------- Quiz Logic ----------------------
if st.session_state.q_index < len(quiz_data):
    q = quiz_data[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}: {q['question']}")
    user_answer = st.radio("Choose your answer:", q['options'], key=st.session_state.q_index)

    if st.button("Submit", key=f"submit_{st.session_state.q_index}"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: {q['answer']}")
        st.session_state.answers.append(user_answer)
        st.session_state.q_index += 1
        st.rerun()
else:
    st.success(f"🎉 Quiz Completed! Your Score: {st.session_state.score}/{len(quiz_data)}")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.answers = []
        st.rerun()

        
