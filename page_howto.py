import streamlit as st

def page_howto():


    st.title("このサイトの使い方")
    st.subheader("ジョブの数を入力してください。")
    st.image("image/input_jobs.png")
    st.title("\u2193")
    st.subheader("各ジョブの各機械での処理時間を入力してください。")
    st.image("image/input_time.png")
    st.title("\u2193")
    st.subheader("「計算を実行してガントチャートを表示する」ボタンを押してください。")
    st.image("image/button.png")
    st.title("\u2193")
    st.subheader("メイクスパンが最小となるスケジュールのガントチャートとメイクスパンの値が表示されます。")
    st.image("image/result.png")

