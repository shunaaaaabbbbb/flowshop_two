import streamlit as st
import matplotlib.pyplot as plt
from solver import johnson_rule
from input import input_jobs
from input import input_time
from plot import gantt_chart



def page_main():
    st.title("このサイトは2機械の順列フローショップ・スケジューリング問題が解けるwebサイトです。")
    st.write("")
    st.subheader("「ジョブ数」、「各ジョブの各機械での処理時間」を入力すれば、メイクスパンが最小となるようなジョブスケジュールを教えてくれます。")


    ## データの入力
    num = input_jobs()  # ジョブ数を入力
    st.write("")
    st.write('各ジョブの各機械での処理時間を入力')
    df = input_time(num)  # ジョブ数に応じて処理時間を記入する表を作成
    edited_df = st.data_editor(df, num_rows="dynamic")  # 編集されたデータフレームを表示
    p = edited_df.T.values.tolist()
    ## 最適スケジュールを計算して結果を表示
    if st.button('計算を実行してガントチャートを表示する', key = "button"):
        optimal_schedule = johnson_rule(num,p[1:])
        gantt_chart(num,optimal_schedule, p[1:])

    st.write("")
    st.write("")
    st.write("")
    st.write("※順列フローショップとは全ての機械において処理するジョブの順番が同じフローショップのことです。順列フローショップでは、例えば機械1においてジョブ1→ジョブ2→ジョブ3の順番でジョブが処理されるとき、機械2でもジョブ1→ジョブ2→ジョブ3の順番でジョブが処理されます。")
    st.write("※ここではブロッキングが発生しないフローショップ・スケジューリング問題を考えています。")


