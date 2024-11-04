import streamlit as st
import datetime

with st.form(key="profile_form"):

    # テキストボックス
    name = st.text_input("名前")
    addres = st.text_input("住所")

    # セレクトボックス
    
    list1 = ("子供(18才未満)","大人(18才以上)")
    list2 = ("スポーツ","読書","プログラミング","アニメ・映画","釣り","料理")

    # age_category = st.selectbox(
    #     "年齢層",
    #     list1
    # )
    age_category = st.radio(
        "年齢層",
        list1
    )

    hobby = st.multiselect(
        "趣味",
        list2
    )

    start_date = st.date_input(
        "開始日",
        datetime.date(2024,11,3)
    )

    start_time = st.time_input(
        "開始時間",
        datetime.time(11,11),
        help="時間を入力してね"
    )

    # ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")

    # print(f'submit_btn: {submit_btn}')
    # print(f'cancel_btn: {cancel_btn}')

    if submit_btn:
        st.text(f'ようこそ{name}さん！{addres}に書籍を送りました。')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味:{",".join(hobby)}')
