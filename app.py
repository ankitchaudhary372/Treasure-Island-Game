import streamlit as st

# title 

st.header("🏝️💎Welcome to Treasure Island🌴🏝️")
st.subheader("Your Mission is to Find the Treasure")
st.subheader("Choose The Path")
import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1


if st.session_state.step == 1:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Left"):
            st.session_state.step = 2

    with col2:
        if st.button("Right"):
            st.subheader("💀 Game Over: Fell into a hole")


if st.session_state.step == 2:
    col3, col4 = st.columns(2)

    with col3:
        if st.button("Swim"):
            st.subheader("💀 Attacked by Sharks")

    with col4:
        if st.button("Wait"):
            st.session_state.step = 3


if st.session_state.step == 3:
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        if st.button("Red"):
            st.subheader("🔥 Burned by fire")

    with col6:
        if st.button("Yellow"):
            st.subheader("🏆 You Found the Treasure!")

    with col7:
        if st.button("Blue"):
            st.subheader("💀 Eaten by beasts")

    with col8:
        if st.button("Anything Else"):
            st.subheader("💀 Wrong door")
            