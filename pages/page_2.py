import streamlit as st

with st.form(key="profile_form"):
    name = st.text_input("名前")
    address = st.text_input("住所")

    age_category = st.selectbox("年齢層", ("子供", "大人"))

    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")

    if submit_btn:
        st.text(f"ようこそ、{address}からお越しの{name}さん!")
        st.text(f"{age_category}料金になります")
